"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

import argparse
from typing import Any, Dict, Union

from jaxl.api._client import JaxlApiModule, jaxl_api_client
from jaxl.api.client.api.v1 import (
    v1_ivr_create,
    v1_ivr_list,
    v1_ivr_options_create,
    v1_ivr_options_list,
    v1_ivr_options_partial_update,
)
from jaxl.api.client.models.cta_request import CTARequest
from jaxl.api.client.models.id_enum import IdEnum
from jaxl.api.client.models.ivr_collection_request import IVRCollectionRequest
from jaxl.api.client.models.ivr_menu_request import IVRMenuRequest
from jaxl.api.client.models.ivr_menu_response import IVRMenuResponse
from jaxl.api.client.models.ivr_options_invalid_response import (
    IVROptionsInvalidResponse,
)
from jaxl.api.client.models.ivr_options_request import IVROptionsRequest
from jaxl.api.client.models.ivr_options_response import IVROptionsResponse
from jaxl.api.client.models.next_or_cta_request import NextOrCTARequest
from jaxl.api.client.models.paginated_ivr_menu_response_list import (
    PaginatedIVRMenuResponseList,
)
from jaxl.api.client.models.patched_ivr_options_update_request import (
    PatchedIVROptionsUpdateRequest,
)
from jaxl.api.client.models.v1_ivr_list_duration import V1IvrListDuration
from jaxl.api.client.types import Response
from jaxl.api.resources._constants import DEFAULT_LIST_LIMIT


def ivrs_list(args: Dict[str, Any]) -> Response[PaginatedIVRMenuResponseList]:
    return v1_ivr_list.sync_detailed(
        client=jaxl_api_client(
            JaxlApiModule.CALL,
            credentials=args.get("credentials", None),
            auth_token=args.get("auth_token", None),
        ),
        assigned=args.get("assigned", False),
        duration=V1IvrListDuration.ONE_WEEK,
        limit=args.get("limit", DEFAULT_LIST_LIMIT),
        offset=args.get("offset", None),
    )


def ivrs_create(args: Dict[str, Any]) -> Response[IVRMenuResponse]:
    return v1_ivr_create.sync_detailed(
        client=jaxl_api_client(
            JaxlApiModule.CALL,
            credentials=args.get("credentials", None),
            auth_token=args.get("auth_token", None),
        ),
        json_body=IVRMenuRequest(
            name=args["message"],
            hangup=args.get("hangup", False),
        ),
    )


def create_next_or_cta(args: Dict[str, Any]) -> NextOrCTARequest:
    return (
        NextOrCTARequest(next_=args["next_"], cta=None)
        if args.get("next_", None) is not None
        else NextOrCTARequest(
            next_=None,
            cta=CTARequest(
                phone_number=args.get("phone"),
                devices=args.get("devices"),
                appusers=args.get("appusers"),
                collections=(
                    IVRCollectionRequest(
                        type=IdEnum.VALUE_2,
                        collection_ids=args["teams"],
                    )
                    if args.get("teams")
                    else None
                ),
                webhook=args.get("webhook"),
            ),
        )
    )


def ivrs_options_create(
    args: Dict[str, Any],
) -> Response[Union[IVROptionsInvalidResponse, IVROptionsResponse]]:
    client = jaxl_api_client(
        JaxlApiModule.CALL,
        credentials=args.get("credentials", None),
        auth_token=args.get("auth_token", None),
    )
    next_or_cta = create_next_or_cta(args)

    # Check whether this args["input_"] is already configured for IVR.
    # Accordingly, either patch or create.
    options_response = v1_ivr_options_list.sync_detailed(
        menu_id=args["ivr"],
        client=client,
    )
    if options_response.status_code != 200 or options_response.parsed is None:
        raise ValueError(
            f"Unable to fetch existing options for IVR#{args['ivr']}, please try again"
        )
    existing_option_id = None
    for option in options_response.parsed.results:
        if option.input_ == args["input_"]:
            existing_option_id = option.id
            break

    return (
        v1_ivr_options_partial_update.sync_detailed(
            id=existing_option_id,
            menu_id=args["ivr"],
            client=client,
            json_body=PatchedIVROptionsUpdateRequest(
                name=args["message"],
                enabled=args.get("enabled", True),
                next_or_cta=next_or_cta,
                # When needs_data_prompt is enabled, we need a message to speak out
                needs_data_prompt=None,
                # When needs_data_prompt is enabled, enabling confirmation will speak back the
                # input to the user for double confirmation
                confirmation=None,
            ),
        )
        if existing_option_id is not None
        else v1_ivr_options_create.sync_detailed(
            menu_id=args["ivr"],
            client=client,
            json_body=IVROptionsRequest(
                name=args["message"],
                input_=args["input_"],
                next_or_cta=next_or_cta,
                enabled=args.get("enabled", True),
                # When needs_data_prompt is enabled, we need a message to speak out
                needs_data_prompt=None,
                # When needs_data_prompt is enabled, enabling confirmation will speak back the
                # input to the user for double confirmation
                confirmation=None,
            ),
        )
    )


IVR_CTA_KEYS = [
    "next_",
    "phone",
    "devices",
    "appusers",
    "teams",
    "webhook",
]

IVR_INPUTS = (
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "*",
    "#",
)


def add_next_or_cta_flags(
    parser: argparse.ArgumentParser,
) -> argparse._MutuallyExclusiveGroup:
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--phone", type=str, help="Send to a phone number")
    group.add_argument("--devices", type=int, nargs="+", help="Send to devices")
    group.add_argument("--appusers", type=int, nargs="+", help="Send to app users")
    group.add_argument("--teams", type=int, nargs="+", help="Send to teams")
    group.add_argument("--webhook", type=str, help="Send to a webhook URL")
    group.add_argument("--next", type=int, dest="next_", help="Next IVR ID")
    return group


def _options_subparser(parser: argparse.ArgumentParser) -> None:
    """Returns ivr options resource subparser."""
    subparsers = parser.add_subparsers(dest="action", required=True)

    options_configure_ivr = subparsers.add_parser(
        "configure",
        help="Configure IVR options",
    )
    options_configure_ivr.add_argument(
        "--ivr",
        required=True,
        type=int,
        help="IVR for which this option needs to be created",
    )
    options_configure_ivr.add_argument(
        "--input",
        dest="input_",
        type=str,
        required=True,
        help="Expected DTMF input from the user",
    )
    options_configure_ivr.add_argument(
        "--message",
        required=True,
        type=str,
        help="Message to speak when referencing this option",
    )
    _group = add_next_or_cta_flags(options_configure_ivr)
    options_configure_ivr.set_defaults(
        func=ivrs_options_create,
        _arg_keys=[
            "input_",
            "ivr",
            "message",
        ]
        + IVR_CTA_KEYS,
    )


def _subparser(parser: argparse.ArgumentParser) -> None:
    """Manage IVRs (Interactive Voice Response)"""
    subparsers = parser.add_subparsers(dest="action", required=True)

    # list ivr
    ivrs_list_parser = subparsers.add_parser(
        "list",
        help="List IVRs",
    )
    ivrs_list_parser.add_argument(
        "--assigned",
        action="store_true",
        required=False,
        help="Use this flag to only list IVRs assigned to atleast 1 Phone Number",
    )
    ivrs_list_parser.add_argument(
        "--limit",
        default=DEFAULT_LIST_LIMIT,
        required=False,
        help="List page size",
    )
    ivrs_list_parser.add_argument(
        "--offset",
        default=None,
        required=False,
        help="List page offset",
    )
    ivrs_list_parser.set_defaults(
        func=ivrs_list,
        _arg_keys=["assigned", "limit", "offset"],
    )

    # create ivr
    ivrs_create_parser = subparsers.add_parser(
        "create",
        help="Create a new IVR",
    )
    ivrs_create_parser.add_argument(
        "--message",
        required=True,
        help="Message to speak when user connects to this IVR",
    )
    ivrs_create_parser.add_argument(
        "--hangup",
        action="store_true",
        help="Whether to hangup after speaking out the message. Default: False.",
    )
    ivrs_create_parser.set_defaults(
        func=ivrs_create,
        _arg_keys=["message", "hangup"],
    )

    # create ivr options subparser
    _options_subparser(subparsers.add_parser("options", help="Manage IVR Options"))


class JaxlIVROptionsSDK:
    # pylint: disable=no-self-use
    def configure(
        self, **kwargs: Any
    ) -> Response[Union[IVROptionsInvalidResponse, IVROptionsResponse]]:
        return ivrs_options_create(kwargs)


class JaxlIVRsSDK:

    def __init__(self) -> None:
        self.options = JaxlIVROptionsSDK()

    # pylint: disable=no-self-use
    def create(self, **kwargs: Any) -> Response[IVRMenuResponse]:
        return ivrs_create(kwargs)

    # pylint: disable=no-self-use
    def list(self, **kwargs: Any) -> Response[PaginatedIVRMenuResponseList]:
        return ivrs_list(kwargs)
