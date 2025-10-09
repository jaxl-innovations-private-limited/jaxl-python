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
    JaxlWebhookResponse,
)


ASK_FOR_CODE_RESPONSE = JaxlWebhookResponse(
    prompt=["Please enter your code followed by star sign"],
    # Because we expect user to end their input with a star sign,
    # we will use num_characters="*".  Only other option is "#".
    num_characters="*",
)


def resolve_code_to_target_phone_number(_code: str) -> str:
    """Returns a target phone number for provided code.

    TODO: Please complete me with real implementation.
    """
    return os.environ.get(
        "JAXL_SDK_PLACEHOLDER_CTA_PHONE",
        "+YYXXXXXXXXXX",
    )


class JaxlAppRequestCodeAndSendToCellular(BaseJaxlApp):
    """This Jaxl App example requests user to enter a numeric code and then bridge them
    together with another cellular user.

    Modify this code to fetch cellular number from your database based upon
    the user's phone number and code they enters.
    """

    async def handle_setup(self, req: JaxlWebhookRequest) -> HANDLER_RESPONSE:
        return ASK_FOR_CODE_RESPONSE

    async def handle_user_data(self, req: JaxlWebhookRequest) -> HANDLER_RESPONSE:
        assert req.state and req.data and req.data.endswith("*")
        return JaxlCtaResponse(
            phone=JaxlPhoneCta(
                to_number=resolve_code_to_target_phone_number(req.data[:-1]),
                from_number=None,
            )
        )
