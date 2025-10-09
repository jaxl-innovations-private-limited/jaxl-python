"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

import asyncio
import os
from typing import Any, Dict, List, Optional, TypedDict, cast

from jaxl.api.base import (
    HANDLER_RESPONSE,
    BaseJaxlApp,
    JaxlStreamRequest,
    JaxlWebhookRequest,
    JaxlWebhookResponse,
)


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


GREETING = "Welcome to AI agent demo"


class AIAgentCallState(TypedDict):
    ctask: Optional[asyncio.Task[None]]
    messages: List[Dict[str, Any]]
    chunks: List[str]


class JaxlAppStreamingAIAgent(BaseJaxlApp):

    def __init__(self) -> None:
        # A single instance of JaxlAppStreamingAIAgent is created which handles
        # all the calls.  Hence, we manage states in a dictionary keyed by call id.
        self._states: Dict[int, AIAgentCallState] = {}

    async def handle_setup(self, req: JaxlWebhookRequest) -> HANDLER_RESPONSE:
        assert req.state
        # Initialize state for this call
        self._states[req.state.call_id] = AIAgentCallState(
            ctask=None,
            messages=[
                {
                    "role": "system",
                    "content": _get_system_prompt("Example Company", "example.com"),
                },
                {
                    "role": "assistant",
                    "content": GREETING,
                },
            ],
            chunks=[],
        )
        return JaxlWebhookResponse(
            prompt=[GREETING],
            num_characters=-1,
        )

    async def handle_teardown(self, req: JaxlWebhookRequest) -> HANDLER_RESPONSE:
        assert req.state
        # Cleanup pending tasks
        if self._states[req.state.call_id]["ctask"] is not None:
            ctask = self._states[req.state.call_id]["ctask"]
            assert ctask is not None
            ctask.cancel()
            self._states[req.state.call_id]["ctask"] = None
        # Cleanup internal state
        if req.state.call_id in self._states:
            del self._states[req.state.call_id]
        return None

    async def handle_speech_detection(self, speaking: bool) -> None:
        print("🎙️" if speaking else "🤐")

    async def handle_transcription(
        self,
        req: JaxlStreamRequest,
        transcription: Dict[str, Any],
        num_inflight_transcribe_requests: int,
    ) -> None:
        text = cast(str, transcription["text"]).strip()
        if len(text) == 0:
            print(
                f"🫙 Empty transcription received, {num_inflight_transcribe_requests}"
            )
            return None
        print(
            f"📝 {text} {num_inflight_transcribe_requests}",
        )
        assert req.state
        if self._states[req.state.call_id]["ctask"] is not None:
            # TODO: Ideally we should also carry forward previous
            # speech phrase transcription into the next chat with agent task.
            print("😢 Canceling previous agent chat due to new transcription event")
            ctask = self._states[req.state.call_id]["ctask"]
            assert ctask is not None
            ctask.cancel()
            self._states[req.state.call_id]["ctask"] = None
        self._states[req.state.call_id]["ctask"] = asyncio.create_task(
            self._chat_with_llm(req, text)
        )
        return None

    async def _chat_with_llm(self, req: JaxlStreamRequest, transcription: str) -> None:
        url = os.environ.get("JAXL_OLLAMA_URL", None)
        assert url is not None and req.state
        self._states[req.state.call_id]["messages"].append(
            {"role": "user", "content": transcription}
        )

        async def _on_llm_response_chunk(response: Optional[Dict[str, Any]]) -> None:
            await self._on_llm_response_chunk(req, response)

        await self.chat_with_ollama(
            on_response_chunk_callback=_on_llm_response_chunk,
            url=url,
            messages=self._states[req.state.call_id]["messages"],
        )

    async def _on_llm_response_chunk(
        self,
        req: JaxlStreamRequest,
        response: Optional[Dict[str, Any]],
    ) -> None:
        assert req.state
        if response is None:
            print("❌ Unable to get agent response")
            self._states[req.state.call_id]["ctask"] = None
            return
        if response["done"]:
            # print("🎭 End of agent response")
            self._states[req.state.call_id]["ctask"] = None
            reply = "".join(self._states[req.state.call_id]["chunks"])
            print(f"💬 {reply}")
            self._states[req.state.call_id]["messages"].append(
                {"role": "assistant", "content": reply}
            )
            await self.tts(req.state.call_id, prompt=reply)
            self._states[req.state.call_id]["chunks"] = []
            return
        self._states[req.state.call_id]["chunks"].append(response["message"]["content"])
