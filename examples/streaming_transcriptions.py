"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Any, Dict, cast

from jaxl.api.base import (
    HANDLER_RESPONSE,
    BaseJaxlApp,
    JaxlStreamRequest,
    JaxlWebhookRequest,
    JaxlWebhookResponse,
)


class JaxlAppStreamingTranscription(BaseJaxlApp):

    async def handle_setup(self, req: JaxlWebhookRequest) -> HANDLER_RESPONSE:
        return JaxlWebhookResponse(
            prompt=["Hello, I am a echo bot, I will repeat after you, try me out."],
            # Since we expect no input from the user, use -1
            num_characters=-1,
        )

    async def handle_speech_detection(self, call_id: int, speaking: bool) -> None:
        print("🎙️" if speaking else "🤐")

    async def handle_transcription(
        self,
        req: JaxlStreamRequest,
        transcription: Dict[str, Any],
        num_inflight_transcribe_requests: int,
    ) -> None:
        assert req.state
        text = cast(str, transcription["text"]).strip()
        if len(text) == 0:
            print(
                f"🫙 Empty transcription received, {num_inflight_transcribe_requests}"
            )
            return None
        print(f"📝 {text}, {num_inflight_transcribe_requests}")
        await self.tts(req.state.call_id, prompt=text)
        return None
