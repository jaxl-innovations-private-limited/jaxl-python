"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from jaxl.api.base import (
    HANDLER_RESPONSE,
    BaseJaxlApp,
    JaxlStreamRequest,
    JaxlWebhookRequest,
    JaxlWebhookResponse,
)


class JaxlAppStreamingAudioChunk(BaseJaxlApp):

    async def handle_setup(self, req: JaxlWebhookRequest) -> HANDLER_RESPONSE:
        return JaxlWebhookResponse(
            prompt=["Welcome to streaming audio chunk demo"],
            # Since we expect no input from the user, use -1
            num_characters=-1,
        )

    async def handle_audio_chunk(
        self,
        req: JaxlStreamRequest,
        slin16: bytes,
    ) -> None:
        print(f"Received {len(slin16)} bytes of raw audio")
        return None
