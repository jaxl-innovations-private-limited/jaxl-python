"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

import argparse
import importlib
from typing import Any, Dict, Optional, cast

import uvicorn
from fastapi import FastAPI, WebSocket

from jaxl.api.base import (
    BaseJaxlApp,
    JaxlWebhookEvent,
    JaxlWebhookRequest,
    JaxlWebhookResponse,
)


def _start_server(app: BaseJaxlApp) -> FastAPI:
    server = FastAPI()

    @server.post("/webhook", response_model=JaxlWebhookResponse)
    async def webhook(req: JaxlWebhookRequest) -> JaxlWebhookResponse:
        """Jaxl Webhook IVR Endpoint."""
        response: Optional[JaxlWebhookResponse] = None
        if req.event == JaxlWebhookEvent.SETUP:
            response = await app.handle_setup(req)
        elif req.event == JaxlWebhookEvent.OPTION:
            response = await app.handle_option(req)
        elif req.event == JaxlWebhookEvent.TEARDOWN:
            response = await app.handle_teardown(req)
        if response is not None:
            return response
        raise NotImplementedError(f"Unhandled event {req.event}")

    @server.websocket("/stream")
    async def stream(ws: WebSocket) -> None:
        """Jaxl Streaming Unidirectional Websockets Endpoint."""
        await ws.accept()
        while True:
            data = await ws.receive_text()
            await ws.send_text(f"Echo: {data}")

    return server


def _load_app(dotted_path: str) -> BaseJaxlApp:
    module_name, class_name = dotted_path.split(":")
    module = importlib.import_module(module_name)
    app_cls = getattr(module, class_name)
    return cast(BaseJaxlApp, app_cls())


def apps_run(args: Dict[str, Any]) -> str:
    app = _start_server(_load_app(args["app"]))
    uvicorn.run(app, host=args["host"], port=args["port"])
    return "Bbye"


def _subparser(parser: argparse.ArgumentParser) -> None:
    """Manage Apps for Webhooks and Streaming audio/speech/transcriptions."""
    subparsers = parser.add_subparsers(dest="action", required=True)

    # run
    apps_run_parser = subparsers.add_parser(
        "run",
        help="Run Jaxl SDK App for webhooks and streams",
    )
    apps_run_parser.add_argument(
        "--app",
        help="Dotted path to Jaxl SDK App module to run e.g. examples.app:JaxlApp",
    )
    apps_run_parser.add_argument(
        "--host",
        default="127.0.0.1",
        help="Defaults to 127.0.0.1",
    )
    apps_run_parser.add_argument(
        "--port",
        type=int,
        default=9919,
        help="Defaults to 9919",
    )
    apps_run_parser.set_defaults(func=apps_run, _arg_keys=["app", "host", "port"])
