"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

import base64
import json
import sys
import types
from typing import List

import unittest

from fastapi.testclient import TestClient

from jaxl.api.base import BaseJaxlApp, JaxlStreamRequest
from jaxl.api.resources.apps import _start_server
from jaxl.api.resources.silence import SilenceDetector


class _FakeVad:
    def __init__(self, aggressiveness: int):
        self._aggressiveness = aggressiveness

    def is_speech(self, frame: bytes, sample_rate: int) -> bool:
        return frame.startswith(b"\x01")


class _StreamingCaptureApp(BaseJaxlApp):
    def __init__(self) -> None:
        self.speech_detection_events: List[bool] = []
        self.speech_chunk_batches: List[List[bytes]] = []

    async def handle_speech_detection(self, call_id: int, speaking: bool) -> None:
        self.speech_detection_events.append(speaking)

    async def handle_speech_chunks(
        self,
        req: JaxlStreamRequest,
        slin16s: List[bytes],
    ) -> None:
        self.speech_chunk_batches.append(list(slin16s))


def _install_fake_webrtcvad() -> None:
    sys.modules["webrtcvad"] = types.SimpleNamespace(Vad=_FakeVad)


def _media_event(payload: bytes) -> dict:
    return {
        "event": "media",
        "media": {
            "payload": base64.b64encode(payload).decode("ascii"),
        },
    }


class StreamingVadTest(unittest.TestCase):
    def setUp(self) -> None:
        _install_fake_webrtcvad()

    def test_silence_detector_uses_faster_speech_start_threshold(self) -> None:
        detector = SilenceDetector()

        changes = [detector.process(b"\x01" * 320) for _ in range(4)]
        self.assertEqual(changes, [None, None, None, None])

        change = detector.process(b"\x01" * 320)
        self.assertTrue(change)

    def test_streaming_vad_preserves_preroll_with_earlier_speech_start(self) -> None:
        """When speech-start fires the pipeline must forward at least the
        speech_frame_threshold trigger frames. Previously a rolling
        deque(maxlen=4) clipped the very first speech frame; the silence
        detector now exposes its own preroll covering ALL trigger frames.
        """
        app = _StreamingCaptureApp()
        server = _start_server(app, vad_speech_frame_threshold=5)
        state = {
            "call_id": 99,
            "from_number": "+911111111111",
            "to_number": "+922222222222",
            "direction": 1,
            "org": None,
            "metadata": None,
            "greeting_message": None,
            "options": None,
            "voice": None,
            "campaign_id": None,
            "campaign_type": None,
        }
        encoded_state = base64.urlsafe_b64encode(
            json.dumps(state).encode("utf-8")
        ).decode("ascii")

        with TestClient(server) as client:
            with client.websocket_connect(
                f"/stream/?ivr_id=1&state={encoded_state}"
            ) as websocket:
                for _ in range(5):
                    websocket.send_text(json.dumps(_media_event(b"\x01" * 320)))
                for _ in range(12):
                    websocket.send_text(json.dumps(_media_event(b"\x00" * 320)))

        self.assertEqual(app.speech_detection_events[:2], [True, False])
        self.assertGreaterEqual(len(app.speech_chunk_batches), 1)
        # The first batch is the silence detector's preroll (concatenated
        # PCM16 bytes covering all 5 trigger frames). It is delivered as a
        # single bytes-list entry rather than per-frame, but must contain
        # ALL 5 trigger frames worth of audio.
        first_batch = app.speech_chunk_batches[0]
        first_batch_bytes = b"".join(first_batch)
        # 5 frames * 320 bytes/frame = 1600 bytes — the full trigger window.
        self.assertGreaterEqual(len(first_batch_bytes), 5 * 320)
        # Every byte in the preroll must come from the speech tone (0x01),
        # not from earlier silence frames.
        self.assertTrue(
            all(byte == 0x01 for byte in first_batch_bytes),
            f"preroll contained non-speech bytes: {first_batch_bytes[:40]!r}",
        )


if __name__ == "__main__":
    unittest.main()
