"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from typing import Optional

from jaxl.api.base import BaseJaxlApp, JaxlWebhookRequest, JaxlWebhookResponse


GREETING_MESSAGE = JaxlWebhookResponse(
    prompt=["Please enter your code followed by star sign"],
    num_characters="*",
    stream=None,
)


class JaxlAppRequestCodeAndSendToCellular(BaseJaxlApp):
    """This Jaxl App example requests user to enter a numeric code and then bridge them
    together with another cellular user.

    Modify this code to fetch cellular number from your database based upon
    the user's phone number and code they enters.
    """

    async def handle_configure(
        self, req: JaxlWebhookRequest
    ) -> Optional[JaxlWebhookResponse]:
        print(f"[{req.pk}] not a real call setup event")
        return GREETING_MESSAGE

    async def handle_setup(
        self, req: JaxlWebhookRequest
    ) -> Optional[JaxlWebhookResponse]:
        assert req.state
        print(f"[{req.pk}.{req.state.call_id}] setup event received")
        return GREETING_MESSAGE

    async def handle_user_data(
        self, req: JaxlWebhookRequest
    ) -> Optional[JaxlWebhookResponse]:
        assert req.state and req.data and req.data.endswith("*")
        print(f"[{req.pk}.{req.state.call_id}] user data received")
        code = req.data[:-1]
        return JaxlWebhookResponse(
            prompt=["Thank you.", f"Your code is {code}"],
            num_characters=0,
            stream=None,
        )


class JaxlAppSendToCellular(BaseJaxlApp):
    """This Jaxl App example bridges the user with another cellular user."""

    async def handle_configure(
        self, req: JaxlWebhookRequest
    ) -> Optional[JaxlWebhookResponse]:
        print(f"[{req.pk}] not a real call setup event")
        return GREETING_MESSAGE

    async def handle_setup(
        self, req: JaxlWebhookRequest
    ) -> Optional[JaxlWebhookResponse]:
        assert req.state
        print(f"[{req.pk}.{req.state.call_id}] setup event received")
        return GREETING_MESSAGE

    # async def handle_option(
    #     self, req: JaxlWebhookRequest
    # ) -> Optional[JaxlWebhookResponse]:
    #     assert req.state
    #     print(f"[{req.pk}.{req.state.call_id}] ivr option {req.option} chosen event")
    #     return JaxlWebhookResponse(
    #         prompt=["Thank you and bye"],
    #         num_characters=0,
    #         stream=None,
    #     )

    # async def handle_teardown(
    #     self, req: JaxlWebhookRequest
    # ) -> Optional[JaxlWebhookResponse]:
    #     assert req.state
    #     print(f"[{req.pk}.{req.state.call_id}] teardown event received")
    #     return JaxlWebhookResponse(
    #         prompt=["Hello", "World"],
    #         num_characters=1,
    #         stream=None,
    #     )
