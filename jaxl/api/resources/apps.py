"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

import argparse
import asyncio
import base64
import importlib
import json
import logging
import os
import shutil
import sys
import tempfile
import uuid
import warnings
import wave
from collections import deque
from typing import TYPE_CHECKING, Any, Deque, Dict, List, Optional, cast

from fastapi.websockets import WebSocketState
from starlette.websockets import WebSocketDisconnect

from jaxl.api.base import (
    HANDLER_RESPONSE,
    BaseJaxlApp,
    JaxlStreamRequest,
    JaxlWebhookEvent,
    JaxlWebhookRequest,
    JaxlWebhookResponse,
)
from jaxl.api.client.models.call_tag_response import CallTagResponse
from jaxl.api.client.types import Response
from jaxl.api.resources.accounts import accounts_me
from jaxl.api.resources.calls import calls_hangup, calls_tag_add
from jaxl.api.resources.silence import SilenceDetector


if TYPE_CHECKING:
    from fastapi import FastAPI


DUMMY_RESPONSE = JaxlWebhookResponse(prompt=[" . "], num_characters=0)

logger = logging.getLogger(__name__)

warnings.filterwarnings(
    "ignore",
    message="FP16 is not supported on CPU; using FP32 instead",
)
warnings.filterwarnings(
    "ignore",
    message="pkg_resources is deprecated as an API",
)


def _start_server(
    app: BaseJaxlApp,
    transcribe: bool = False,
    transcribe_model_size: str = "small",
    transcribe_language: str = "en",
    transcribe_device: str = "cpu",
    transcribe_temperature: float = 0.3,
) -> "FastAPI":
    from fastapi import FastAPI, Request, WebSocket

    server = FastAPI()

    # Transcription tasks
    model: Optional["whisper.Whisper"] = None
    mlock = asyncio.Lock()
    ttasks: Dict[str, asyncio.Task[Dict[str, Any]]] = {}

    if transcribe:
        import whisper

        model = whisper.load_model(transcribe_model_size, device=transcribe_device)

    def _save_raw_audio_as_wav(slin16s: List[bytes]) -> str:
        """Stores raw chunks to a wav file on disk"""
        audio_data = b"".join(slin16s)
        # pylint: disable=consider-using-with
        wav_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
        with wave.open(wav_file, "wb") as wf:
            # pylint: disable=no-member
            wf.setnchannels(1)
            wf.setsampwidth(2)
            wf.setframerate(8000)
            wf.writeframes(audio_data)
        return wav_file.name

    async def _transcribe(slin16s: List[bytes]) -> Dict[str, Any]:
        assert model is not None
        wav_path: Optional[str] = None
        try:
            async with mlock:
                wav_path = _save_raw_audio_as_wav(slin16s)
                return cast(
                    Dict[str, Any],
                    model.transcribe(
                        audio=wav_path,
                        language=transcribe_language,
                        temperature=transcribe_temperature,
                    ),
                )
        finally:
            if wav_path:
                os.unlink(wav_path)

    async def _ttask_done_callback_async(
        req: JaxlStreamRequest,
        ttask: asyncio.Task[Dict[str, Any]],
        tsid: str,
    ) -> None:
        try:
            await app.handle_transcription(req, ttask.result(), len(ttasks) - 1)
        # pylint: disable=broad-exception-caught
        except Exception as exc:
            logger.warning(f"Transcription task failed: {exc}")
        finally:
            del ttasks[tsid]

    def _ttask_done_callback(
        req: JaxlStreamRequest,
        task: asyncio.Task[Dict[str, Any]],
        tsid: str,
    ) -> None:
        asyncio.create_task(_ttask_done_callback_async(req, task, tsid))

    wss: Dict[int, WebSocket] = {}

    async def _add_tag(call_id: int, tag: str) -> Response[CallTagResponse]:
        return calls_tag_add({"call_id": call_id, "tag": tag})

    async def _hangup(call_id: int) -> Response[Any]:
        return calls_hangup({"call_id": call_id})

    async def _clear_audio(call_id: int) -> bool:
        try:
            await wss[call_id].send_text(json.dumps({"event": "clear"}))
            return True
        # pylint: disable=broad-exception-caught
        except Exception as exc:
            logger.warning(f"⚠️ clear_audio failure: {exc}")
            return False

    async def _send_audio(call_id: int, slin16: bytes) -> bool:
        try:
            await wss[call_id].send_text(
                json.dumps(
                    {
                        "event": "media",
                        "media": {
                            "payload": base64.b64encode(slin16).decode("ascii"),
                        },
                    }
                )
            )
            return True
        # pylint: disable=broad-exception-caught
        except Exception as exc:
            logger.warning(f"⚠️ send_audio failure: {exc}")
            return False

    app.send_audio = _send_audio  # type: ignore[method-assign]
    app.clear_audio = _clear_audio  # type: ignore[method-assign]
    app.add_tag = _add_tag  # type: ignore[method-assign]
    app.hangup = _hangup  # type: ignore[method-assign]

    @server.api_route(
        "/webhook/",
        methods=["POST", "DELETE"],
        response_model=HANDLER_RESPONSE,
    )
    async def webhook(req: JaxlWebhookRequest, request: Request) -> HANDLER_RESPONSE:
        """Jaxl Webhook IVR Endpoint."""
        response: HANDLER_RESPONSE = None
        if req.event == JaxlWebhookEvent.SETUP:
            assert request.method == "POST"
            if req.state is None:
                response = await app.handle_configure(req)
                if response is None:
                    # Configure event is used to prewarm TTS for your IVR.
                    # But its not absolutely essential to prewarm if you wish to do so.
                    # Mock dummy response for now, allowing module developers
                    # to not override handle_teardown if they wish not to use it.
                    response = DUMMY_RESPONSE
            elif req.data:
                response = await app.handle_user_data(req)
            else:
                response = await app.handle_setup(req)
        elif req.event == JaxlWebhookEvent.OPTION:
            assert request.method == "POST"
            if req.data:
                response = await app.handle_user_data(req)
            else:
                response = await app.handle_option(req)
        elif req.event == JaxlWebhookEvent.TEARDOWN:
            assert request.method == "DELETE"
            response = await app.handle_teardown(req)
            if response is None:
                # Teardown request doesn't really expect any response,
                # atleast currently its not even being processed at Jaxl servers.
                # Just mock a dummy response for now, allowing module developers
                # to not override handle_teardown if they wish not to use it.
                response = DUMMY_RESPONSE
        elif req.event == JaxlWebhookEvent.MARK:
            assert request.method == "POST"
            response = await app.handle_mark(req)
        if response is not None:
            return response
        # logger.warning(f"Unhandled event {req.event} or handler returned None")
        return None

    @server.websocket("/stream/")
    async def stream(ws: WebSocket) -> None:
        """Jaxl Streaming Unidirectional Websockets Endpoint."""
        _ivr_id = ws.query_params.get("ivr_id")
        _state = ws.query_params.get("state")
        if _state is None or _ivr_id is None:
            await ws.close(code=1008)
            return

        ivr_id = int(_ivr_id)
        state = json.loads(base64.b64decode(_state))

        # Speech detector, Speech state & Segment buffer
        sdetector = SilenceDetector()
        speaking: bool = False
        buffer: Deque[bytes] = deque(maxlen=sdetector.speech_frame_threshold)
        slin16s: List[bytes] = []

        await ws.accept()
        wss[state["call_id"]] = ws

        # pylint: disable=too-many-nested-blocks
        try:
            while True:
                data = json.loads(await ws.receive_text())
                ev = data["event"]
                if ev == "media":
                    req = JaxlStreamRequest(pk=ivr_id, state=state)
                    slin16 = base64.b64decode(data[ev]["payload"])
                    # Invoke audio chunk handlers
                    await app.handle_audio_chunk(req, slin16)
                    # Detect start/end of speech
                    buffer.append(slin16)
                    change = sdetector.process(slin16)
                    # Manage speech segments
                    if change is True:
                        speaking = change
                        await app.handle_speech_detection(state["call_id"], speaking)
                        if len(slin16s) == 0:
                            # Silence just got detected, copy over
                            # last speech_frame_threshold of frames
                            slin16s = list(buffer)
                            if len(slin16s) > 0:
                                await app.handle_speech_chunks(req, slin16s)
                            # print("💿")
                        # print("🎙️")
                        slin16s.append(slin16)
                        await app.handle_speech_chunks(req, [slin16])
                    elif change is False:
                        speaking = change
                        await app.handle_speech_chunks(req, [slin16])
                        await app.handle_speech_detection(state["call_id"], speaking)
                        # print("🤐")
                        if len(slin16s) > 0:
                            # Invoke speech segment handlers
                            await app.handle_speech_segment(req, slin16s)
                            if model:
                                tsid = uuid.uuid4().hex
                                ttask = asyncio.create_task(_transcribe(slin16s))
                                ttasks[tsid] = ttask
                                ttask.add_done_callback(
                                    lambda task: _ttask_done_callback(
                                        req,
                                        task,
                                        tsid,
                                    )
                                )
                        slin16s = []
                    else:
                        assert change is None
                        if speaking is True:
                            await app.handle_speech_chunks(req, [slin16])
                            slin16s.append(slin16)
                        else:
                            assert speaking is False
                elif ev == "connected":
                    pass
                else:
                    logger.warning(f"UNHANDLED STREAMING EVENT {ev}")
        except WebSocketDisconnect:
            pass
        finally:
            if state["call_id"] in wss:
                del wss[state["call_id"]]
            if ws.client_state != WebSocketState.DISCONNECTED:
                await ws.close()

    for config, func in app.api_routes():
        server.add_api_route(
            path=config[0],
            methods=config[1],
            response_model=config[2],
            endpoint=func,
        )

    for path, wfunc in app.websocket_routes():
        server.add_websocket_route(path, wfunc)

    return server


def _load_app(dotted_path: str) -> BaseJaxlApp:
    module_name, class_name = dotted_path.split(":")
    module = importlib.import_module(module_name)
    app_cls = getattr(module, class_name)
    return cast(BaseJaxlApp, app_cls())


def apps_run(args: Dict[str, Any]) -> str:
    account = accounts_me()
    if account.status_code != 200:
        raise ValueError("Unable to authenticate")

    if args["transcribe"]:
        # Ensure ffmpeg is in path
        name = "ffmpeg"
        if shutil.which(name) is None:
            sys.exit(
                f"❌ {name} not found. Please install {name} and ensure it's in your PATH."
            )

    app = _start_server(
        _load_app(args["app"]),
        transcribe=args["transcribe"],
        transcribe_model_size=args["transcribe_model_size"],
        transcribe_language=args["transcribe_language"],
        transcribe_device=args["transcribe_device"],
    )

    import uvicorn

    uvicorn.run(app, host=args["host"], port=args["port"])

    return "Bbye"


def _subparser(parser: argparse.ArgumentParser) -> None:
    """Manage Apps for Webhooks and Streaming audio/speech/transcriptions."""
    subparsers = parser.add_subparsers(dest="action", required=True)

    # run
    apps_run_parser = subparsers.add_parser(
        "run",
        help="Run Jaxl SDK App for webhooks and streams",
    )
    apps_run_parser.add_argument(
        "--app",
        help="Dotted path to Jaxl SDK App module to run e.g. examples.app:JaxlApp",
    )
    apps_run_parser.add_argument(
        "--host",
        default="127.0.0.1",
        help="Defaults to 127.0.0.1",
    )
    apps_run_parser.add_argument(
        "--port",
        type=int,
        default=9919,
        help="Defaults to 9919",
    )
    apps_run_parser.add_argument(
        "--transcribe",
        action="store_true",
        required=False,
        help="This flag is required to enable realtime transcription pipeline",
    )
    apps_run_parser.add_argument(
        "--transcribe-model-size",
        type=str,
        default="small",
        help="Options are: tiny, base, small, medium, large",
    )
    apps_run_parser.add_argument(
        "--transcribe-language",
        type=str,
        default="en",
        help="Options are: auto, ar, bg, bn, cs, da, de, el, en, es, et, fi, fil, "
        "fr, gu, he, hi, hr, hu, id, it, ja, kn, ko, lt, lv, ml, mr, nl, no, "
        "pa, pl, pt, ro, ru, sk, sl, sr, sv, ta, te, th, tr, uk, ur, vi, zh",
    )
    apps_run_parser.add_argument(
        "--transcribe-device",
        type=str,
        default="cpu",
        help="Options are: auto, cpu, cuda, cuda:N, mps",
    )
    apps_run_parser.set_defaults(
        func=apps_run,
        _arg_keys=[
            "app",
            "host",
            "port",
            "transcribe",
            "transcribe_model_size",
            "transcribe_language",
            "transcribe_device",
        ],
    )


class JaxlAppsSDK:
    # pylint: disable=no-self-use
    def run(self, **kwargs: Any) -> str:
        return apps_run(kwargs)
