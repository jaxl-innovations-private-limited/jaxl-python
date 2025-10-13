"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

import argparse
import hashlib
from typing import Any, Dict

from jaxl.api._client import JaxlApiModule, jaxl_api_client
from jaxl.api.client.api.v1 import v1_messages_list
from jaxl.api.client.models.paginated_dh_message_list import (
    PaginatedDHMessageList,
)
from jaxl.api.client.types import Response
from jaxl.api.resources._constants import DEFAULT_LIST_LIMIT


def _sha256(data: str) -> str:
    key = hashlib.sha256()
    key.update(data.encode())
    return key.hexdigest()


def messages_list(args: Dict[str, Any]) -> Response[PaginatedDHMessageList]:
    return v1_messages_list.sync_detailed(
        client=jaxl_api_client(
            JaxlApiModule.MESSAGE,
            credentials=args.get("credentials", None),
            auth_token=args.get("auth_token", None),
        ),
        limit=args.get("limit", DEFAULT_LIST_LIMIT),
        okey=[_sha256(member_email) for member_email in args.get("member_email", [])],
        mid=None,
        offset=None,
    )


def _subparser(parser: argparse.ArgumentParser) -> None:
    """Manage Messages (SMS, WA, RCS, Email, App-to-App)"""
    subparsers = parser.add_subparsers(dest="action", required=True)

    # list
    messages_list_parser = subparsers.add_parser("list", help="List all Messages")
    messages_list_parser.add_argument(
        "--member-email",
        type=str,
        required=True,
        action="append",
        help="Member Email IDs",
    )
    messages_list_parser.add_argument(
        "--limit",
        default=DEFAULT_LIST_LIMIT,
        type=int,
        required=False,
        help="Message page size. Defaults to 1.",
    )
    messages_list_parser.set_defaults(
        func=messages_list, _arg_keys=["limit", "member_email"]
    )


class JaxlMessagesSDK:
    # pylint: disable=no-self-use
    def list(self, **kwargs: Any) -> Response[PaginatedDHMessageList]:
        return messages_list(kwargs)
