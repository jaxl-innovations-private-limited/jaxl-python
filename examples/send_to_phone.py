"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

import os

from jaxl.api.base import (
    HANDLER_RESPONSE,
    BaseJaxlApp,
    JaxlCtaResponse,
    JaxlPhoneCta,
    JaxlWebhookRequest,
)


class JaxlAppSendToCellular(BaseJaxlApp):
    """This Jaxl App example bridges the user with another cellular user."""

    async def handle_setup(self, req: JaxlWebhookRequest) -> HANDLER_RESPONSE:
        # As soon as someone calls this call flow,
        # place another outgoing call and bridge them together.
        return JaxlCtaResponse(
            phone=JaxlPhoneCta(
                to_number=os.environ.get(
                    "JAXL_SDK_PLACEHOLDER_CTA_PHONE",
                    "+YYXXXXXXXXXX",
                ),
                from_number=None,
            )
        )
