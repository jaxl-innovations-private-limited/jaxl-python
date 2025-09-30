"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

import argparse
import uuid
from typing import Any, Dict, List, Optional, Tuple, cast

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
from jaxl.api.resources.ivrs import (
    IVR_CTA_KEYS,
    IVR_INPUTS,
    ivrs_create,
    ivrs_options_create,
)
from jaxl.api.resources.payments import payments_get_total_recharge


def calls_usage(args: Dict[str, Any]) -> Response[CallUsageResponse]:
    return v1_calls_usage_retrieve.sync_detailed(
        client=jaxl_api_client(JaxlApiModule.CALL),
        currency=args.get("currency", DEFAULT_CURRENCY),
    )


def ivrs_create_adhoc(
    message: str,
    inputs: Optional[Dict[str, Tuple[str, str, str]]] = None,
    hangup: bool = False,
) -> int:
    if (hangup is True and inputs is not None) or (hangup is False and inputs is None):
        raise ValueError("One of hangup or inputs is required")
    rcreate = ivrs_create({"message": message, "hangup": hangup})
    if rcreate.status_code != 201 or rcreate.parsed is None:
        raise ValueError(
            f"Unable to create adhoc IVR, status code {rcreate.status_code}"
        )
    if inputs:
        for input_ in inputs:
            name, cta, value = inputs[input_]
            roption = ivrs_options_create(
                {
                    "ivr": rcreate.parsed.id,
                    "input_": input_,
                    "message": name,
                    cta: value,
                }
            )
            if roption.status_code != 201:
                raise ValueError(
                    f"Unable to create adhoc IVR option, status code {roption.status_code}"
                )
    return rcreate.parsed.id


def calls_create(args: Dict[str, Any]) -> Response[CallTokenResponse]:
    """Create a new call"""
    total_recharge = payments_get_total_recharge({"currency": 2})
    if total_recharge.status_code != 200 or total_recharge.parsed is None:
        raise ValueError("Unable to fetch total recharge")
    to_numbers = args["to"]
    ivr_id = None
    if len(to_numbers) != 1:
        raise NotImplementedError(
            "To start a conference call provide an IVR ID with phone CTA key"
        )
    else:
        # Ensure we have an IVR ID, otherwise what will even happen once the user picks the call?
        ivr_id = args.get("ivr", None)
        if ivr_id is None:
            # Well we also allow users to create adhoc IVRs when placing an outgoing call.
            # Example, suppose user wants to connect 2 cellular users, here is how they can proceed:
            # 1) Place call with initial `--to` value
            # 2) When this callee picks up the call, they enter provided IVR which speaks a
            #    greeting message, prompts them to press a key when ready.
            # 3) Once user presses the key, CTA type can be a phone number
            # 4) System will place the call to provided CTA phone number
            # 5) While the call is in action, original `--to` callee will hear a ringtone
            # 6) If CTA phone number answers the call, system will brigde the two callee together
            # 7) Once the call ends, IVR may continue and provide further flow specification, OR
            #    by default we simply hangup the call when either party hang up the call.
            # 8) To enable reachability and connectivity, after the call we can ask the callee
            #    whether call has ended or whether they want to reconnect with the other side again.
            message = cast(Optional[str], args.get("message", None))
            options = cast(Optional[List[str]], args.get("option", None))
            if message is None or options is None:
                raise ValueError(
                    "--ivr or --message/--option is required to route this call somewhere "
                    + "once callee answers the call"
                )
            # Create adhoc IVR
            assert message is not None and options is not None
            inputs = {}
            for option in options:
                parts = option.split(":", 1)
                input_, name = parts[0].split("=", 1)
                cta, value = parts[1].split("=", 1)
                if cta not in IVR_CTA_KEYS or input_ not in IVR_INPUTS:
                    raise ValueError(f"Invalid CTA key {cta} or input {input_}")
                inputs[input_] = (name, cta, value)
            ivr_id = ivrs_create_adhoc(message, inputs)
            if ivr_id is None:
                raise ValueError("Unable to create ad-hoc IVR")
    to_number = to_numbers[0]
    return v1_calls_token_create.sync_detailed(
        client=jaxl_api_client(JaxlApiModule.CALL),
        json_body=CallTokenRequest(
            from_number=args["from_"],
            to_number=to_number,
            call_type=CallTypeEnum.VALUE_2,
            session_id=str(uuid.uuid4()).upper(),
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
    return v1_calls_list.sync_detailed(
        client=jaxl_api_client(JaxlApiModule.CALL),
        currency=args.get("currency", DEFAULT_CURRENCY),
        limit=args.get("limit", DEFAULT_LIST_LIMIT),
    )


# def calls_hangup(args: Optional[Dict[str, Any]] = None) -> Response[PaginatedCallList]:
#     pass


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
    ivr_group = calls_create_parser.add_mutually_exclusive_group(required=True)
    ivr_group.add_argument(
        "--ivr",
        required=False,
        help="IVR ID to route this call once picked by recipient",
    )
    ivr_group.add_argument(
        "--message",
        help="Ad-hoc IVR message (if no --ivr provided, this will create one)",
    )
    calls_create_parser.add_argument(
        "--option",
        action="append",
        help="Configure IVR options, at-least 1-required when using --message flag. "
        + "Example: --option 0:phone=+919249903400 --option 1:devices=123,124,135.  "
        + "See `ivrs options configure -h` for all possible CTA options",
    )
    calls_create_parser.set_defaults(
        func=calls_create,
        _arg_keys=["to", "from_", "ivr", "message", "option"],
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
    calls_list_parser.add_argument(
        "--active",
        action="store_true",
        required=False,
        help="Use this flag to only list active calls",
    )
    calls_list_parser.set_defaults(
        func=calls_list, _arg_keys=["currency", "limit", "active"]
    )

    # hangup
    # calls_hangup_parser = subparsers.add_parser("hangup", help="Hangup calls")
    # calls_hangup_parser.set_defaults(func=calls_hangup, _arg_keys=[])

    # transfer

    # add
    # remove

    # mute/unmute
    # hold/unhold

    # play
    # say

    # ivr (send active call into an ivr)

    # recording stop/pause/resume/start
    # transcription list/get/search/summary/sentiment

    # stream audio (unidirectional raw audio callbacks)
    # stream speech (unidirectional speech segment callbacks)
    # stream stt (unidirectional speech segment to stt and callbacks)
    #


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
