"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

import argparse
import importlib
from typing import TYPE_CHECKING, Any, Dict, cast

from jaxl.api.base import (
    HANDLER_RESPONSE,
    BaseJaxlApp,
    JaxlWebhookEvent,
    JaxlWebhookRequest,
    JaxlWebhookResponse,
)


if TYPE_CHECKING:
    from fastapi import FastAPI

DUMMY_RESPONSE = JaxlWebhookResponse(prompt=[" . "], num_characters=0)


def _start_server(app: BaseJaxlApp) -> "FastAPI":
    from fastapi import FastAPI, Request, WebSocket

    server = FastAPI()

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
        if response is not None:
            return response
        raise NotImplementedError(f"Unhandled event {req.event}")

    @server.websocket("/stream/")
    async def stream(ws: WebSocket) -> None:
        """Jaxl Streaming Unidirectional Websockets Endpoint."""
        await ws.accept()
        while True:
            data = await ws.receive_text()
            await ws.send_text(f"Echo: {data}")

    return server


def _load_app(dotted_path: str) -> BaseJaxlApp:
    module_name, class_name = dotted_path.split(":")
    module = importlib.import_module(module_name)
    app_cls = getattr(module, class_name)
    return cast(BaseJaxlApp, app_cls())


def apps_run(args: Dict[str, Any]) -> str:
    app = _start_server(_load_app(args["app"]))

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
    apps_run_parser.set_defaults(func=apps_run, _arg_keys=["app", "host", "port"])
