"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from jaxl.api.base import (
    HANDLER_RESPONSE,
    BaseJaxlApp,
    JaxlWebhookRequest,
    JaxlWebhookResponse,
)


class JaxlAppStreamingAudioChunk(BaseJaxlApp):

    async def handle_setup(self, req: JaxlWebhookRequest) -> HANDLER_RESPONSE:
        return JaxlWebhookResponse(
            prompt=["Welcome to streaming audio chunk demo"],
            num_characters=1,
        )

    async def handle_audio_chunk(self, slin16: bytes) -> None:
        # print(slin16)
        pass
