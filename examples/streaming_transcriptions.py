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


class JaxlAppStreamingTranscription(BaseJaxlApp):

    async def handle_setup(self, req: JaxlWebhookRequest) -> HANDLER_RESPONSE:
        return JaxlWebhookResponse(
            prompt=["Welcome to streaming transcriptions demo"],
            num_characters=1,
        )
