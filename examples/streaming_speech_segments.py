"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

import logging
from typing import List

from jaxl.api.base import (
    HANDLER_RESPONSE,
    BaseJaxlApp,
    JaxlStreamRequest,
    JaxlWebhookRequest,
    JaxlWebhookResponse,
)


class JaxlAppStreamingSpeechSegment(BaseJaxlApp):

    async def handle_setup(self, req: JaxlWebhookRequest) -> HANDLER_RESPONSE:
        return JaxlWebhookResponse(
            prompt=["Welcome to streaming speech audio segments demo"],
            num_characters=-1,
        )

    async def handle_speech_segment(
        self,
        req: JaxlStreamRequest,
        slin16s: List[bytes],
    ) -> None:
        logging.info(f"Received {len(slin16s)} chunks in speech segment")
        return None
