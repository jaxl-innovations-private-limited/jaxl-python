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


class JaxlWebhookResponse(BaseModel):
    prompt: List[str]
    num_characters: Union[int, str]
    stream: Optional[float]


class BaseJaxlApp:
    async def handle_setup(self, req: JaxlWebhookRequest) -> JaxlWebhookResponse:
        pass

    async def handle_option(self, req: JaxlWebhookRequest) -> JaxlWebhookResponse:
        pass

    async def handle_teardown(self, req: JaxlWebhookRequest) -> JaxlWebhookResponse:
        pass
