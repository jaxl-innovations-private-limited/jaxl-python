"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

import asyncio
# pylint: disable=deprecated-module
import audioop
import os
import wave
from pathlib import Path
from typing import Dict

from jaxl.api.base import (
    HANDLER_RESPONSE,
    BaseJaxlApp,
    JaxlWebhookRequest,
    JaxlWebhookResponse,
)


SAMPLE_RATE = 8000
SAMPLE_WIDTH = 2
CHANNELS = 1
FRAME_MS = 20
FRAME_BYTES = SAMPLE_RATE * SAMPLE_WIDTH * FRAME_MS // 1000
SEND_INTERVAL_S = 0.010  # Send faster than real-time to avoid SIP jitter.


def load_wav_as_slin16_8k_mono(path: str) -> bytes:
    with wave.open(path, "rb") as wav:
        audio = wav.readframes(wav.getnframes())
        sample_width = wav.getsampwidth()
        channels = wav.getnchannels()
        sample_rate = wav.getframerate()

    if channels != CHANNELS:
        audio = audioop.tomono(audio, sample_width, 0.5, 0.5)
        channels = CHANNELS
    if sample_width != SAMPLE_WIDTH:
        audio = audioop.lin2lin(audio, sample_width, SAMPLE_WIDTH)
        sample_width = SAMPLE_WIDTH
    if sample_rate != SAMPLE_RATE:
        audio, _ = audioop.ratecv(
            audio,
            sample_width,
            channels,
            sample_rate,
            SAMPLE_RATE,
            None,
        )
    return audio


class JaxlAppStreamingWavFile(BaseJaxlApp):
    """Minimal incoming-call app that streams one WAV file over the live stream."""

    def __init__(self) -> None:
        self._playback_tasks: Dict[int, asyncio.Task[None]] = {}
        self._wav_path = os.environ.get("JAXL_STREAMING_WAV_PATH", "example.wav")
        self._audio = load_wav_as_slin16_8k_mono(self._wav_path)

    async def handle_setup(self, req: JaxlWebhookRequest) -> HANDLER_RESPONSE:
        return JaxlWebhookResponse(prompt=[], num_characters=-1)

    async def handle_teardown(self, req: JaxlWebhookRequest) -> HANDLER_RESPONSE:
        assert req.state is not None
        self._cancel_playback(req.state.call_id)
        return None

    async def on_stream_connect(self, call_id: int) -> None:
        self._cancel_playback(call_id)
        self._playback_tasks[call_id] = asyncio.create_task(self._stream_wav(call_id))

    async def on_stream_disconnect(self, call_id: int) -> None:
        self._cancel_playback(call_id)

    def _cancel_playback(self, call_id: int) -> None:
        task = self._playback_tasks.pop(call_id, None)
        if task is not None:
            task.cancel()

    async def _stream_wav(self, call_id: int) -> None:
        print(f"Streaming {Path(self._wav_path)} to call {call_id}")
        for offset in range(0, len(self._audio), FRAME_BYTES):
            chunk = self._audio[offset : offset + FRAME_BYTES]
            if len(chunk) < FRAME_BYTES:
                chunk += b"\x00" * (FRAME_BYTES - len(chunk))
            if not await self.send_audio(call_id, chunk):
                break
            await asyncio.sleep(SEND_INTERVAL_S)
