"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from enum import Enum
from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel, model_validator

from jaxl.api.resources.ivrs import IVR_CTA_KEYS


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


class JaxlCtaResponse(BaseModel):
    next: Optional[int] = None
    phone: Optional[str] = None
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
