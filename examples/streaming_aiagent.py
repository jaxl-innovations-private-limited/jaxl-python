"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from jaxl.api.base import HANDLER_RESPONSE, BaseJaxlApp, JaxlStreamRequest


class JaxlAppStreamingAIAgent(BaseJaxlApp):

    async def handle_transcription(
        self,
        req: JaxlStreamRequest,
        transcription: str,
        num_inflight_transcribe_requests: int,
    ) -> HANDLER_RESPONSE:
        # OpenAI, standard banaya hai, world ke saare LLM wahi specification follow karte hai
        return None
