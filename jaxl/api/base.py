"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from enum import Enum
from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel


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
    stream: Optional[float]


class BaseJaxlApp:

    # pylint: disable=no-self-use
    async def handle_configure(
        self,
        # pylint: disable=unused-argument
        req: JaxlWebhookRequest,
    ) -> Optional[JaxlWebhookResponse]:
        """Invoked when a phone number gets assigned to IVR."""
        return None

    # pylint: disable=no-self-use
    async def handle_setup(
        self,
        # pylint: disable=unused-argument
        req: JaxlWebhookRequest,
    ) -> Optional[JaxlWebhookResponse]:
        """Invoked when IVR starts or when user
        input was requested just after the greeting message."""
        return None

    async def handle_user_data(
        self,
        # pylint: disable=unused-argument
        req: JaxlWebhookRequest,
    ) -> Optional[JaxlWebhookResponse]:
        """Invoked when IVR has received user input ending in a
        character during the greeting phase."""
        return None

    # pylint: disable=no-self-use
    async def handle_option(
        self,
        # pylint: disable=unused-argument
        req: JaxlWebhookRequest,
    ) -> Optional[JaxlWebhookResponse]:
        """Invoked when IVR option is chosen and when IVR option data has been received."""
        return None

    # pylint: disable=no-self-use
    async def handle_teardown(
        self,
        # pylint: disable=unused-argument
        req: JaxlWebhookRequest,
    ) -> Optional[JaxlWebhookResponse]:
        """Invoked when a call ends."""
        return None
