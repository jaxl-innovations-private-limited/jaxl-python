"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

import argparse
import uuid
from typing import Any, Dict, Optional

from jaxl.api._client import JaxlApiModule, jaxl_api_client
from jaxl.api.client.api.v1 import (
    v1_calls_list,
    v1_calls_token_create,
    v1_calls_usage_retrieve,
)
from jaxl.api.client.models.call_token_request import CallTokenRequest
from jaxl.api.client.models.call_token_response import CallTokenResponse
from jaxl.api.client.models.call_type_enum import CallTypeEnum
from jaxl.api.client.models.call_usage_response import CallUsageResponse
from jaxl.api.client.models.paginated_call_list import PaginatedCallList
from jaxl.api.client.types import Response
from jaxl.api.resources._constants import DEFAULT_CURRENCY, DEFAULT_LIST_LIMIT
from jaxl.api.resources.payments import payments_get_total_recharge


def calls_usage(args: Dict[str, Any]) -> Response[CallUsageResponse]:
    return v1_calls_usage_retrieve.sync_detailed(
        client=jaxl_api_client(JaxlApiModule.CALL),
        currency=args.get("currency", DEFAULT_CURRENCY),
    )


def calls_create(args: Dict[str, Any]) -> Response[CallTokenResponse]:
    """Create a new call"""
    total_recharge = payments_get_total_recharge({"currency": 2})
    if total_recharge.status_code != 200 or total_recharge.parsed is None:
        raise ValueError("Unable to fetch total recharge")
    to_numbers = args["to"]
    ivr_id = None
    if len(to_numbers) != 1:
        raise NotImplementedError("Conference calls not yet supported from CLI")
    else:
        # Ensure we have an IVR ID, otherwise what will even happen once the user picks the call?
        ivr_id = args.get("ivr", None)
        if ivr_id is None:
            raise ValueError(
                "--ivr is required to proceed with the call once receiver picks up"
            )
    to_number = to_numbers[0]
    return v1_calls_token_create.sync_detailed(
        client=jaxl_api_client(JaxlApiModule.CALL),
        json_body=CallTokenRequest(
            from_number=args["from_"],
            to_number=to_number,
            call_type=CallTypeEnum.VALUE_2,
            session_id=uuid.uuid4().hex,
            currency="INR",
            total_recharge=total_recharge.parsed.signed,
            balance="0",
            ivr_id=ivr_id,
            provider=None,
            cid=None,
        ),
    )


def calls_list(args: Optional[Dict[str, Any]] = None) -> Response[PaginatedCallList]:
    """List calls"""
    args = args or {}
    # print("Listing calls...", args)
    return v1_calls_list.sync_detailed(
        client=jaxl_api_client(JaxlApiModule.CALL),
        currency=args.get("currency", DEFAULT_CURRENCY),
        limit=args.get("limit", DEFAULT_LIST_LIMIT),
    )


def _subparser(parser: argparse.ArgumentParser) -> None:
    """Manage Calls (Domestic & International Cellular, App-to-App)"""
    subparsers = parser.add_subparsers(dest="action", required=True)

    # create
    calls_create_parser = subparsers.add_parser(
        "create",
        help="Start or schedule a new call",
    )
    calls_create_parser.add_argument(
        "--to",
        action="extend",
        type=_unique_comma_separated,
        required=True,
        help="Recipient identity. Use multiple times or comma-separated for a conference call.",
    )
    calls_create_parser.add_argument(
        "--from",
        dest="from_",
        required=False,
        help="Caller identity",
    )
    calls_create_parser.add_argument(
        "--ivr",
        required=False,
        help="IVR ID to route this call once picked by recipient",
    )
    calls_create_parser.set_defaults(
        func=calls_create,
        _arg_keys=["to", "from_", "ivr"],
    )
    # list
    calls_list_parser = subparsers.add_parser("list", help="List all calls")
    calls_list_parser.add_argument(
        "--currency",
        default=DEFAULT_CURRENCY,
        type=int,
        required=False,
        help="Call usage currency. Defaults to INR value 2.",
    )
    calls_list_parser.add_argument(
        "--limit",
        default=DEFAULT_LIST_LIMIT,
        type=int,
        required=False,
        help="Call page size. Defaults to 1.",
    )
    calls_list_parser.set_defaults(func=calls_list, _arg_keys=["currency", "limit"])


def _unique_comma_separated(value: str) -> list[str]:
    items = [v.strip() for v in value.split(",") if v.strip()]
    seen = set()
    unique_items = []
    for item in items:
        if item in seen:
            raise argparse.ArgumentTypeError(f"Duplicate recipient: '{item}'")
        seen.add(item)
        unique_items.append(item)
    return unique_items
