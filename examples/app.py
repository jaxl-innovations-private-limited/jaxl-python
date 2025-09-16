"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from jaxl.api.base import BaseJaxlApp, JaxlWebhookRequest, JaxlWebhookResponse


class JaxlApp(BaseJaxlApp):
    async def handle_setup(self, req: JaxlWebhookRequest) -> JaxlWebhookResponse:
        if req.state is None:
            print(f"[{req.pk}] not a real call setup event")
        else:
            print(f"[{req.pk}] setup event received")
        return JaxlWebhookResponse(
            prompt=["Hello", "World"],
            num_characters=1,
            stream=None,
        )

    async def handle_option(self, req: JaxlWebhookRequest) -> JaxlWebhookResponse:
        print(f"[{req.pk}] dtmf input event")
        return JaxlWebhookResponse(
            prompt=["Hello", "World"],
            num_characters=1,
            stream=None,
        )

    async def handle_teardown(self, req: JaxlWebhookRequest) -> JaxlWebhookResponse:
        print(f"[{req.pk}] teardown event received")
        return JaxlWebhookResponse(
            prompt=["Hello", "World"],
            num_characters=1,
            stream=None,
        )
