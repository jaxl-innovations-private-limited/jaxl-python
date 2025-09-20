"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from jaxl.api.base import (
    HANDLER_RESPONSE,
    BaseJaxlApp,
    JaxlCtaResponse,
    JaxlWebhookRequest,
)


class JaxlAppSendToCellular(BaseJaxlApp):
    """This Jaxl App example bridges the user with another cellular user."""

    async def handle_setup(self, req: JaxlWebhookRequest) -> HANDLER_RESPONSE:
        return JaxlCtaResponse(phone="+YYXXXXXXXXXX")
