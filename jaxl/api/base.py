"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

import json
import logging
from enum import Enum
from typing import (
    Any,
    Awaitable,
    Callable,
    Coroutine,
    Dict,
    List,
    Optional,
    Tuple,
    Union,
)

import requests
from fastapi import WebSocket
from fastapi.responses import Response as FastApiResponse
from pydantic import BaseModel, model_validator

from jaxl.api.client.models.call_tag_response import CallTagResponse
from jaxl.api.client.types import Response
from jaxl.api.resources.calls import calls_tts
from jaxl.api.resources.ivrs import IVR_CTA_KEYS


logger = logging.getLogger(__name__)


class JaxlWebhookEvent(Enum):
    SETUP = 1
    OPTION = 2
    TEARDOWN = 3
    STREAM = 4
    MARK = 5


class JaxlOrg(BaseModel):
    id: Optional[int] = None
    name: str


class JaxlWebhookState(BaseModel):
    call_id: int
    from_number: str
    to_number: str
    direction: int
    org: Optional[JaxlOrg]
    metadata: Optional[Dict[str, Any]]
    greeting_message: Optional[str]
    options: Optional[Dict[str, Any]]


class JaxlWebhookRequest(BaseModel):
    # IVR ID
    pk: int
    # Type of webhook event received
    event: JaxlWebhookEvent
    # Webhook state
    state: Optional[JaxlWebhookState]
    # DTMF inputs
    option: Optional[str]
    # Extra data
    data: Optional[str]
    # Present only with mark event
    mark: Optional[str] = None


class JaxlWebhookResponse(BaseModel):
    prompt: List[str]
    num_characters: Union[int, str]
    mark: Optional[str] = None


class JaxlStreamRequest(BaseModel):
    # IVR ID
    pk: int
    # Webhook state
    state: Optional[JaxlWebhookState]


class JaxlPhoneCta(BaseModel):
    to_number: str
    from_number: Optional[str]


class JaxlCtaResponse(BaseModel):
    next: Optional[int] = None
    phone: Optional[JaxlPhoneCta] = None
    devices: Optional[List[int]] = None
    appusers: Optional[List[int]] = None
    teams: Optional[List[int]] = None

    @model_validator(mode="after")
    def ensure_only_one_key(self) -> "JaxlCtaResponse":
        non_null_keys = [k for k, v in self.__dict__.items() if v is not None]
        if len(non_null_keys) == 0:
            raise ValueError(f"At least one of {IVR_CTA_KEYS} must be provided")
        if len(non_null_keys) > 1:
            raise ValueError(
                f"Only one of {IVR_CTA_KEYS} can be non-null, got {non_null_keys}"
            )
        if non_null_keys[0] == "phone":
            if not (
                self.phone is not None
                and self.phone.to_number is not None
                and self.phone.to_number.startswith("+")
                and self.phone.to_number.split("+")[1].isdigit()
                and (
                    self.phone.from_number is None
                    or (
                        self.phone.from_number.startswith("+")
                        and self.phone.from_number.split("+")[1].isdigit()
                    )
                )
            ):
                raise ValueError("Invalid phone value, provide e164")
        return self


HANDLER_RESPONSE = Optional[Union[JaxlWebhookResponse, JaxlCtaResponse]]

ApiRouteConfig = Tuple[str, List[str], Optional[BaseModel]]
ApiRouteFunc = Union[
    Callable[[BaseModel], Coroutine[Any, Any, Union[BaseModel, FastApiResponse]]],
    Callable[[], Coroutine[Any, Any, Union[BaseModel, FastApiResponse]]],
]
WebsocketRouteFunc = Callable[[WebSocket], Awaitable[None]]


class BaseJaxlApp:

    # pylint: disable=no-self-use,unused-argument
    def api_routes(self) -> List[Tuple[ApiRouteConfig, ApiRouteFunc]]:
        return []

    def websocket_routes(self) -> List[Tuple[str, WebsocketRouteFunc]]:
        return []

    # pylint: disable=no-self-use,unused-argument
    async def handle_configure(self, req: JaxlWebhookRequest) -> HANDLER_RESPONSE:
        """Invoked when a phone number gets assigned to IVR."""
        return None

    # pylint: disable=no-self-use,unused-argument
    async def handle_setup(self, req: JaxlWebhookRequest) -> HANDLER_RESPONSE:
        """Invoked when IVR starts."""
        return None

    # pylint: disable=no-self-use,unused-argument
    async def handle_user_data(self, req: JaxlWebhookRequest) -> HANDLER_RESPONSE:
        """Invoked when IVR has received multiple character user input
        ending in a specified character."""
        return None

    # pylint: disable=no-self-use,unused-argument
    async def handle_option(self, req: JaxlWebhookRequest) -> HANDLER_RESPONSE:
        """Invoked when IVR option is chosen."""
        return None

    async def handle_mark(self, req: JaxlWebhookRequest) -> HANDLER_RESPONSE:
        """Invoked once TTS has finished.  Only invoked if a marker was provided to tts function"""
        return None

    # pylint: disable=no-self-use,unused-argument
    async def handle_teardown(self, req: JaxlWebhookRequest) -> HANDLER_RESPONSE:
        """Invoked when a call ends."""
        return None

    async def handle_speech_detection(self, call_id: int, speaking: bool) -> None:
        """Invoked when speech starts and ends."""
        return None

    async def handle_audio_chunk(
        self,
        req: JaxlStreamRequest,
        slin16: bytes,
    ) -> None:
        return None

    async def handle_speech_chunks(
        self,
        req: JaxlStreamRequest,
        slin16s: List[bytes],
    ) -> None:
        pass

    async def handle_speech_segment(
        self,
        req: JaxlStreamRequest,
        slin16s: List[bytes],
    ) -> None:
        return None

    async def handle_transcription(
        self,
        req: JaxlStreamRequest,
        transcription: Dict[str, Any],
        num_inflight_transcribe_requests: int,
    ) -> None:
        return None

    async def chat_with_ollama(
        self,
        on_response_chunk_callback: Callable[..., Coroutine[Any, Any, Any]],
        url: str,
        messages: List[Dict[str, Any]],
        model: str = "gemma3:1b",
        stream: bool = True,
        timeout: int = 270,
        # Model tuning params
        #
        # Controls the randomness of the model's output.
        # A lower value (e.g., 0.0) makes the model more deterministic,
        # while a higher value (e.g., 1.0) introduces more randomness.
        # This is often used to control creativity vs. coherence.
        temperature: float = 0.7,
        # Defines the maximum number of tokens (words or characters)
        # the model can generate in the response. If not provided,
        # the model will typically generate as much as it can.
        # max_tokens: int = 150,
        # (Nucleus Sampling) (top_p): This parameter uses nucleus sampling
        # to control the diversity of the output. Setting top_p to a value
        # between 0 and 1 helps restrict the choices the model can make to
        # a smaller, higher-probability set of options.
        top_p: float = 1.0,
        # Reduces the likelihood of the model repeating the same phrases.
        # A higher value means less repetition.
        frequency_penalty: float = 0.5,
        # Encourages the model to talk about new topics by penalizing repeated ideas or concepts.
        presence_penalty: float = 0.5,
    ) -> None:
        payload = {
            "model": model,
            "messages": messages,
            "stream": stream,
            "temperature": temperature,
            # "max_tokens": max_tokens,
            "top_p": top_p,
            "frequency_penalty": frequency_penalty,
            "presence_penalty": presence_penalty,
        }
        response = requests.post(url, json=payload, timeout=timeout)
        if response.status_code != 200:
            await on_response_chunk_callback(None)
        # Parse streaming ollama response
        for chunk in response.iter_lines(decode_unicode=True):
            chunk = chunk.strip()
            if not chunk:
                continue
            try:
                await on_response_chunk_callback(json.loads(chunk))
            # pylint: disable=broad-exception-caught
            except Exception as exc:
                logger.warning(f"Unable to process ollama response: {exc}, {chunk}")

    async def tts(
        self,
        call_id: int,
        prompt: str,
        mark: Optional[str] = None,
        **kwargs: Any,
    ) -> Response[Any]:
        return calls_tts({"call_id": call_id, "prompt": prompt, "mark": mark})

    async def send_audio(self, call_id: int, slin16: bytes) -> bool:
        """Send raw audio.

        Only available with bidirectional streams.
        """
        return False

    async def clear_audio(self, call_id: int) -> bool:
        """Clear any buffered audio."""
        return False

    async def hangup(self, call_id: int) -> Optional[Response[Any]]:
        """Hangup call by ID"""
        return None

    async def add_tag(
        self, call_id: int, tag: str
    ) -> Optional[Response[CallTagResponse]]:
        """Add tag to a call by ID."""
        return None
