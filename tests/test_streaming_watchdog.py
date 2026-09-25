"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

# F-193 (2026-09-25): a new SDK user followed the README, registered a plain
# webhook IVR, ran the streaming examples and got "no sound, no error". The
# app now tells them: streaming handlers are implemented but Jaxl never
# opened `/stream/` → add `?stream` to the IVR URL. This pins the detection.

from typing import Any, Dict, Optional

import unittest

from jaxl.api.base import BaseJaxlApp, JaxlStreamMeta, JaxlStreamRequest
from jaxl.api.resources.apps import (
    STREAMING_HANDLERS,
    streaming_handlers_overridden,
)


class _WebhookOnlyApp(BaseJaxlApp):
    pass


class _StreamingApp(BaseJaxlApp):
    async def handle_audio_chunk(
        self,
        req: JaxlStreamRequest,
        slin16: bytes,
        meta: Optional[JaxlStreamMeta] = None,
    ) -> None:
        return None


class _TranscribingApp(BaseJaxlApp):
    async def on_stream_connect(self, call_id: int) -> None:
        return None

    async def handle_transcription(
        self,
        req: JaxlStreamRequest,
        transcription: Dict[str, Any],
        num_inflight_transcribe_requests: int,
    ) -> None:
        return None


class TestStreamingHandlersOverridden(unittest.TestCase):
    def test_every_watched_hook_exists_on_the_base_class(self) -> None:
        for name in STREAMING_HANDLERS:
            self.assertTrue(hasattr(BaseJaxlApp, name), name)

    def test_webhook_only_app_needs_no_stream(self) -> None:
        self.assertEqual(streaming_handlers_overridden(_WebhookOnlyApp()), [])

    def test_audio_app_is_detected(self) -> None:
        self.assertEqual(
            streaming_handlers_overridden(_StreamingApp()), ["handle_audio_chunk"]
        )

    def test_multiple_overrides_reported_in_declaration_order(self) -> None:
        self.assertEqual(
            streaming_handlers_overridden(_TranscribingApp()),
            ["on_stream_connect", "handle_transcription"],
        )


if __name__ == "__main__":
    unittest.main()
