"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

import json
import logging
from enum import Enum
from typing import Any, Callable, Coroutine, Dict, List, Optional, Union

import requests
from pydantic import BaseModel, model_validator

from jaxl.api._client import JaxlApiModule, jaxl_api_client
from jaxl.api.client.api.v1 import v1_calls_tts_create
from jaxl.api.client.models.call_tts_request_request import (
    CallTtsRequestRequest,
)
from jaxl.api.resources.ivrs import IVR_CTA_KEYS


logger = logging.getLogger(__name__)


class JaxlWebhookEvent(Enum):
    SETUP = 1
    OPTION = 2
    TEARDOWN = 3
    STREAM = 4


class JaxlOrg(BaseModel):
    name: str


class JaxlWebhookState(BaseModel):
    call_id: int
    from_number: str
    to_number: str
    direction: int
    org: Optional[JaxlOrg]
    metadata: Optional[Dict[str, Any]]
    greeting_message: Optional[str]


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


class JaxlWebhookResponse(BaseModel):
    prompt: List[str]
    num_characters: Union[int, str]


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


class BaseJaxlApp:

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

    # pylint: disable=no-self-use,unused-argument
    async def handle_teardown(self, req: JaxlWebhookRequest) -> HANDLER_RESPONSE:
        """Invoked when a call ends."""
        return None

    async def handle_speech_detection(self, speaking: bool) -> None:
        """Invoked when speech starts and ends."""
        return None

    async def handle_audio_chunk(
        self,
        req: JaxlStreamRequest,
        slin16: bytes,
    ) -> None:
        return None

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
                logger.warning(f"Unable to process ollama response: {exc}")

    async def tts(self, call_id: int, prompt: str) -> None:
        v1_calls_tts_create.sync_detailed(
            id=call_id,
            client=jaxl_api_client(JaxlApiModule.CALL),
            json_body=CallTtsRequestRequest(prompts=prompt.split(".")),
        )
