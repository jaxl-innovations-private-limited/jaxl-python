"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

import argparse
import time
import uuid
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional, Tuple, Union, cast

from jaxl.api._client import JaxlApiModule, encrypt, jaxl_api_client
from jaxl.api.client.api.v1 import (
    v1_calls_add_create,
    v1_calls_audio_retrieve,
    v1_calls_hangup_retrieve,
    v1_calls_list,
    v1_calls_messages_create,
    v1_calls_retrieve,
    v1_calls_tags_create,
    v1_calls_token_create,
    v1_calls_transfer_create,
    v1_calls_tts_create,
    v1_calls_usage_retrieve,
)
from jaxl.api.client.models.call import Call
from jaxl.api.client.models.call_add_request_request import (
    CallAddRequestRequest,
)
from jaxl.api.client.models.call_audio_reason import CallAudioReason
from jaxl.api.client.models.call_message_request_request import (
    CallMessageRequestRequest,
)
from jaxl.api.client.models.call_message_request_type_enum import (
    CallMessageRequestTypeEnum,
)
from jaxl.api.client.models.call_tag_request import CallTagRequest
from jaxl.api.client.models.call_tag_response import CallTagResponse
from jaxl.api.client.models.call_token_request import CallTokenRequest
from jaxl.api.client.models.call_token_response import CallTokenResponse
from jaxl.api.client.models.call_transfer_request_request import (
    CallTransferRequestRequest,
)
from jaxl.api.client.models.call_tts_request_request import (
    CallTtsRequestRequest,
)
from jaxl.api.client.models.call_type_enum import CallTypeEnum
from jaxl.api.client.models.call_usage_response import CallUsageResponse
from jaxl.api.client.models.paginated_call_list import PaginatedCallList
from jaxl.api.client.models.why_enum import WhyEnum
from jaxl.api.client.types import Response, Unset
from jaxl.api.resources._constants import DEFAULT_CURRENCY, DEFAULT_LIST_LIMIT
from jaxl.api.resources.ivrs import (
    IVR_CTA_KEYS,
    IVR_INPUTS,
    add_next_or_cta_flags,
    create_next_or_cta,
    ivrs_create,
    ivrs_options_create,
)
from jaxl.api.resources.payments import payments_get_total_recharge


def calls_usage(args: Dict[str, Any]) -> Response[CallUsageResponse]:
    return v1_calls_usage_retrieve.sync_detailed(
        client=jaxl_api_client(
            JaxlApiModule.CALL,
            credentials=args.get("credentials", None),
            auth_token=args.get("auth_token", None),
        ),
        currency=args.get("currency", DEFAULT_CURRENCY),
    )


def ivrs_create_adhoc(
    message: str,
    inputs: Optional[Dict[str, Tuple[str, str, Union[List[str], str]]]] = None,
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
                inputs[input_] = (
                    name,
                    cta,
                    (
                        value.split(",")
                        if cta
                        in (
                            "devices",
                            "appusers",
                            "teams",
                        )
                        else value
                    ),
                )
            ivr_id = ivrs_create_adhoc(message, inputs)
            if ivr_id is None:
                raise ValueError("Unable to create ad-hoc IVR")
    to_number = to_numbers[0]
    return v1_calls_token_create.sync_detailed(
        client=jaxl_api_client(
            JaxlApiModule.CALL,
            credentials=args.get("credentials", None),
            auth_token=args.get("auth_token", None),
        ),
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


def calls_get(args: Optional[Dict[str, Any]] = None) -> Response[Call]:
    """Get a call"""
    args = args or {}
    return v1_calls_retrieve.sync_detailed(
        id=args["call_id"],
        client=jaxl_api_client(
            JaxlApiModule.CALL,
            credentials=args.get("credentials", None),
            auth_token=args.get("auth_token", None),
        ),
        currency=args.get("currency", DEFAULT_CURRENCY),
    )


def calls_list(args: Optional[Dict[str, Any]] = None) -> Response[PaginatedCallList]:
    """List calls"""
    args = args or {}
    return v1_calls_list.sync_detailed(
        client=jaxl_api_client(
            JaxlApiModule.CALL,
            credentials=args.get("credentials", None),
            auth_token=args.get("auth_token", None),
        ),
        currency=args.get("currency", DEFAULT_CURRENCY),
        limit=args.get("limit", DEFAULT_LIST_LIMIT),
    )


def calls_add(args: Dict[str, Any]) -> Response[Any]:
    return v1_calls_add_create.sync_detailed(
        id=args["call_id"],
        client=jaxl_api_client(
            JaxlApiModule.CALL,
            credentials=args.get("credentials", None),
            auth_token=args.get("auth_token", None),
        ),
        json_body=CallAddRequestRequest(
            e164=args.get("e164", Unset),
            email=args.get("email", Unset),
            from_e164=args.get("from_e164", Unset),
        ),
    )


def calls_tts(args: Dict[str, Any]) -> Response[Any]:
    return v1_calls_tts_create.sync_detailed(
        id=args["call_id"],
        client=jaxl_api_client(
            JaxlApiModule.CALL,
            credentials=args.get("credentials", None),
            auth_token=args.get("auth_token", None),
        ),
        json_body=CallTtsRequestRequest(
            prompts=[pro for pro in args["prompt"].split(".") if len(pro.strip()) > 0],
            mark=args.get("mark", None),
        ),
    )


def calls_tag_add(args: Dict[str, Any]) -> Response[CallTagResponse]:
    return v1_calls_tags_create.sync_detailed(
        call_id=args["call_id"],
        client=jaxl_api_client(
            JaxlApiModule.CALL,
            credentials=args.get("credentials", None),
            auth_token=args.get("auth_token", None),
        ),
        json_body=CallTagRequest(name=args["tag"]),
    )


def calls_hangup(args: Dict[str, Any]) -> Response[Any]:
    return v1_calls_hangup_retrieve.sync_detailed(
        id=args["call_id"],
        client=jaxl_api_client(
            JaxlApiModule.CALL,
            credentials=args.get("credentials", None),
            auth_token=args.get("auth_token", None),
        ),
    )


def calls_transfer(args: Dict[str, Any]) -> Response[Any]:
    return v1_calls_transfer_create.sync_detailed(
        id=args["call_id"],
        client=jaxl_api_client(
            JaxlApiModule.CALL,
            credentials=args.get("credentials", None),
            auth_token=args.get("auth_token", None),
        ),
        json_body=CallTransferRequestRequest(next_or_cta=create_next_or_cta(args)),
    )


def calls_message(args: Dict[str, Any]) -> Response[Any]:
    return v1_calls_messages_create.sync_detailed(
        id=args["call_id"],
        client=jaxl_api_client(
            JaxlApiModule.CALL,
            credentials=args.get("credentials", None),
            auth_token=args.get("auth_token", None),
        ),
        json_body=CallMessageRequestRequest(
            text=encrypt(args["text"]),
            timestamp=datetime.fromtimestamp(
                args.get("epoch", None) or time.time(),
                tz=timezone.utc,
            ),
            why=WhyEnum[cast(str, args["direction"]).upper()],
            type=(
                CallMessageRequestTypeEnum.VALUE_1
                if args["type"] == "chat"
                else CallMessageRequestTypeEnum.VALUE_10
            ),
        ),
    )


def calls_audio(args: Dict[str, Any]) -> Response[Any | CallAudioReason]:
    assert "call_id" in args and "path" in args
    response = v1_calls_audio_retrieve.sync_detailed(
        id=args["call_id"],
        client=jaxl_api_client(
            JaxlApiModule.CALL,
            credentials=args.get("credentials", None),
            auth_token=args.get("auth_token", None),
        ),
    )
    if response.status_code != 200:
        return response
    with open(args["path"], "wb+") as recording:
        recording.write(response.content)
    return response


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

    # add
    calls_add_parser = subparsers.add_parser(
        "add", help="Add a phone number or email ID to an existing calls"
    )
    calls_add_parser.add_argument(
        "--call-id",
        type=int,
        required=True,
        help="Current call ID",
    )
    group = calls_add_parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--e164",
        type=str,
        help="Phone number that must be called and merged with ongoing call",
    )
    group.add_argument(
        "--email",
        type=str,
        help="Org member that must be called and merged with ongoing call",
    )
    calls_add_parser.add_argument(
        "--from-e164",
        type=str,
        required=False,
        help="Optionally, provide a number that must be used to place outgoing call to --e164",
    )
    calls_add_parser.set_defaults(
        func=calls_add,
        _arg_keys=[
            "e164",
            "email",
            "from_e164",
            "call_id",
        ],
    )

    calls_tts_parser = subparsers.add_parser(
        "tts", help="Send text prompts in an active call"
    )
    calls_tts_parser.add_argument(
        "--call-id",
        type=int,
        required=True,
        help="Call ID",
    )
    calls_tts_parser.add_argument(
        "--prompt",
        type=str,
        required=True,
    )
    calls_tts_parser.set_defaults(func=calls_tts, _arg_keys=["call_id", "prompt"])

    calls_get_parser = subparsers.add_parser("get", help="Get a call detail")
    calls_get_parser.add_argument(
        "--call-id",
        type=int,
        required=True,
        help="Call ID",
    )
    calls_get_parser.set_defaults(func=calls_get, _arg_keys=["call_id"])

    # hangup
    calls_hangup_parser = subparsers.add_parser("hangup", help="Hangup call")
    calls_hangup_parser.add_argument(
        "--call-id",
        type=int,
        required=True,
        help="Call ID",
    )
    calls_hangup_parser.set_defaults(func=calls_hangup, _arg_keys=["call_id"])

    # transfer
    calls_transfer_parser = subparsers.add_parser("transfer", help="Transfer call")
    calls_transfer_parser.add_argument(
        "--call-id",
        type=int,
        required=True,
        help="Call ID",
    )
    _group = add_next_or_cta_flags(calls_transfer_parser)
    calls_transfer_parser.set_defaults(
        func=calls_transfer,
        _arg_keys=["call_id"] + IVR_CTA_KEYS,
    )

    # message
    calls_message_parser = subparsers.add_parser("message", help="Add message to call")
    calls_message_parser.add_argument(
        "--call-id",
        type=int,
        required=True,
        help="Call ID",
    )
    calls_message_parser.add_argument(
        "--text",
        type=str,
        required=True,
        help="Message text",
    )
    calls_message_parser.add_argument(
        "--type",
        type=str,
        choices=["chat", "note"],
        required=True,
        help="Message type",
    )
    calls_message_parser.add_argument(
        "--direction",
        type=str,
        choices=["sent", "rcvd"],
        required=True,
        help="Message direction",
    )
    calls_message_parser.add_argument(
        "--epoch",
        type=float,
        required=False,
        help="Provide timestamp when this message was originally generated.  "
        + "If not provided, current epoch will be used",
    )
    calls_message_parser.set_defaults(
        func=calls_message,
        _arg_keys=[
            "call_id",
            "text",
            "type",
            "direction",
            "epoch",
        ],
    )

    # audio
    calls_audio_parser = subparsers.add_parser("audio", help="Download call recording")
    calls_audio_parser.add_argument(
        "--call-id",
        type=int,
        required=True,
        help="Call ID",
    )
    calls_audio_parser.add_argument(
        "--path",
        type=str,
        required=True,
        help="WAV recording download path",
    )
    calls_audio_parser.set_defaults(func=calls_audio, _arg_keys=["call_id", "path"])

    # add
    # remove

    # mute/unmute
    # hold/unhold

    # play

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


class JaxlCallsSDK:

    # pylint: disable=no-self-use
    def create(self, **kwargs: Any) -> Response[CallTokenResponse]:
        return calls_create(kwargs)

    def list(self, **kwargs: Any) -> Response[PaginatedCallList]:
        return calls_list(kwargs)

    def add(self, **kwargs: Any) -> Response[Any]:
        return calls_add(kwargs)

    def tts(self, **kwargs: Any) -> Response[Any]:
        return calls_tts(kwargs)

    def get(self, **kwargs: Any) -> Response[Call]:
        return calls_get(kwargs)

    def add_tag(self, **kwargs: Any) -> Response[CallTagResponse]:
        return calls_tag_add(kwargs)

    def hangup(self, **kwargs: Any) -> Response[Any]:
        return calls_hangup(kwargs)

    def message(self, **kwargs: Any) -> Response[Any]:
        return calls_message(kwargs)

    def audio(self, **kwargs: Any) -> Response[Any | CallAudioReason]:
        return calls_audio(kwargs)
