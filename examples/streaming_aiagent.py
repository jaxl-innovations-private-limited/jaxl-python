"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

import asyncio
import logging
import os
from typing import Any, Dict, List, Optional

from jaxl.api.base import (
    HANDLER_RESPONSE,
    BaseJaxlApp,
    JaxlStreamRequest,
    JaxlWebhookRequest,
    JaxlWebhookResponse,
)


logger = logging.getLogger(__name__)


def _get_system_prompt(brand_name: str, domain: str) -> str:
    return (
        "You are a concise and precise virtual assistant "
        f"for the domain {domain}, "
        f"representing the brand '{brand_name}'. "
        "Always reply in plain text."
        "\n\n"
        f"User may mispronounce '{brand_name}'. "
        "Try to infer the mispronunciations and treat all such variants "
        f"as references to '{brand_name}' and "
        f"always refer to the name correctly as '{brand_name}' in your responses."
        "\n\n"
        "Keep your responses short (one or two sentences) "
        "and to the point, unless the user asks for more details. "
        "Avoid unnecessary elaboration. When appropriate, follow this template: "
        "provide a brief answer, and ask a clarifying question. "
        "Your primary goal is to be concise, precise, clear and efficient."
        "\n\n"
        "Use the system role context in following messages to answer queries related "
        f"to {domain}."
    )


class JaxlAppStreamingAIAgent(BaseJaxlApp):

    def __init__(self) -> None:
        self._ctask: Optional[asyncio.Task[None]] = None
        self._messages = [
            {
                "role": "system",
                "content": _get_system_prompt("Example Company", "example.com"),
            },
        ]
        self._chunks: List[str] = []

    async def handle_setup(self, req: JaxlWebhookRequest) -> HANDLER_RESPONSE:
        return JaxlWebhookResponse(
            prompt=["Welcome to AI agent demo"],
            num_characters=-1,
        )

    async def handle_teardown(self, req: JaxlWebhookRequest) -> HANDLER_RESPONSE:
        if self._ctask is not None:
            self._ctask.cancel()
            self._ctask = None
        return None

    async def handle_transcription(
        self,
        req: JaxlStreamRequest,
        transcription: Dict[str, Any],
        num_inflight_transcribe_requests: int,
    ) -> None:
        logging.debug(
            "📝 %s %d",
            transcription["text"],
            num_inflight_transcribe_requests,
        )
        if self._ctask is not None:
            # TODO: Ideally we should also carry forward previous
            # speech phrase transcription into the next chat with agent task.
            logger.debug(
                "😢 %s",
                "Canceling previous agent chat due to new transcription event",
            )
            self._ctask.cancel()
            self._ctask = None
        self._ctask = asyncio.create_task(
            self._chat_with_llm(req, transcription["text"])
        )
        return None

    async def _chat_with_llm(self, req: JaxlStreamRequest, transcription: str) -> None:
        url = os.environ.get("JAXL_OLLAMA_URL", None)
        assert url is not None
        self._messages.append({"role": "user", "content": transcription})

        async def _on_llm_response_chunk(response: Optional[Dict[str, Any]]) -> None:
            await self._on_llm_response_chunk(req, response)

        logger.debug("💬 %s", transcription)
        await self.chat_with_ollama(
            on_response_chunk_callback=_on_llm_response_chunk,
            url=url,
            messages=self._messages,
        )

    async def _on_llm_response_chunk(
        self,
        req: JaxlStreamRequest,
        response: Optional[Dict[str, Any]],
    ) -> None:
        assert req.state
        if response is None:
            logger.warning("❌ %s", "Unable to get agent response")
            self._ctask = None
            return
        if response["done"]:
            logger.debug("🎭 %s", "End of agent response")
            self._ctask = None
            reply = "".join(self._chunks)
            await self.tts(req.state.call_id, prompts=[reply])
            self._chunks = []
            return
        self._chunks.append(response["message"]["content"])
