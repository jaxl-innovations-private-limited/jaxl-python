"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Dict

from jaxl.api.base import (
    HANDLER_RESPONSE,
    BaseJaxlApp,
    JaxlWebhookRequest,
    JaxlWebhookResponse,
)


ASK_FOR_CODE_RESPONSE = JaxlWebhookResponse(
    prompt=["Please enter your code followed by star sign"],
    num_characters="*",
)


def _ask_for_confirmation_response(code: str) -> JaxlWebhookResponse:
    return JaxlWebhookResponse(
        prompt=[
            f"You entered {code}.",
            "Press 1 to confirm.",
            "Press 2 to re-enter your code.",
        ],
        num_characters=1,
    )


def _thankyou_response(code: str) -> JaxlWebhookResponse:
    return JaxlWebhookResponse(
        prompt=[
            "Thank you.",
            f"We have successfully received your code {code}",
        ],
        num_characters=0,
    )


class JaxlAppRequestCodeAndSendToCellular(BaseJaxlApp):
    """This Jaxl App example requests user to enter a numeric code and then bridge them
    together with another cellular user.

    Modify this code to fetch cellular number from your database based upon
    the user's phone number and code they enters.
    """

    def __init__(self) -> None:
        self._codes: Dict[int, str] = {}

    async def handle_configure(self, req: JaxlWebhookRequest) -> HANDLER_RESPONSE:
        return ASK_FOR_CODE_RESPONSE

    async def handle_setup(self, req: JaxlWebhookRequest) -> HANDLER_RESPONSE:
        return ASK_FOR_CODE_RESPONSE

    async def handle_user_data(self, req: JaxlWebhookRequest) -> HANDLER_RESPONSE:
        assert req.state and req.data and req.data.endswith("*")
        self._codes[req.state.call_id] = req.data[:-1]
        return _ask_for_confirmation_response(self._codes[req.state.call_id])

    async def handle_option(self, req: JaxlWebhookRequest) -> HANDLER_RESPONSE:
        assert req.state
        if req.option == "1":
            return _thankyou_response(self._codes[req.state.call_id])
            # TODO: Fetch target number from your database
            # return JaxlCtaResponse(phone="+YYXXXXXXXXXX")
        # For any other input than "1" we simply take user to re-enter code flow.
        return ASK_FOR_CODE_RESPONSE


class JaxlAppSendToCellular(BaseJaxlApp):
    """This Jaxl App example bridges the user with another cellular user."""

    async def handle_configure(self, req: JaxlWebhookRequest) -> HANDLER_RESPONSE:
        print(f"[{req.pk}] not a real call setup event")
        return ASK_FOR_CODE_RESPONSE

    async def handle_setup(self, req: JaxlWebhookRequest) -> HANDLER_RESPONSE:
        assert req.state
        print(f"[{req.pk}.{req.state.call_id}] setup event received")
        return ASK_FOR_CODE_RESPONSE

    # async def handle_teardown(
    #     self, req: JaxlWebhookRequest
    # ) -> HANDLER_RESPONSE:
    #     assert req.state
    #     print(f"[{req.pk}.{req.state.call_id}] teardown event received")
    #     return JaxlWebhookResponse(
    #         prompt=["Hello", "World"],
    #         num_characters=1,
    #         stream=None,
    #     )
