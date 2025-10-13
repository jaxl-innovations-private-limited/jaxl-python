"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

import argparse
from typing import Any, Dict

from jaxl.api._client import JaxlApiModule, jaxl_api_client
from jaxl.api.client.api.v1 import v1_kyc_list
from jaxl.api.client.models.paginated_kyc_list import PaginatedKycList
from jaxl.api.client.types import Response
from jaxl.api.resources._constants import DEFAULT_LIST_LIMIT


def kycs_list(args: Dict[str, Any]) -> Response[PaginatedKycList]:
    return v1_kyc_list.sync_detailed(
        client=jaxl_api_client(
            JaxlApiModule.CALL,
            credentials=args.get("credentials", None),
            auth_token=args.get("auth_token", None),
        ),
        iso_country=None,
        limit=args.get("limit", DEFAULT_LIST_LIMIT),
        offset=None,
        provider_status=None,
        resource=None,
        status=None,
    )


def _subparser(parser: argparse.ArgumentParser) -> None:
    """Manage KYCs"""
    subparsers = parser.add_subparsers(dest="action", required=True)

    # list
    kyc_list_parser = subparsers.add_parser("list", help="List all KYCs")
    kyc_list_parser.add_argument(
        "--limit",
        default=DEFAULT_LIST_LIMIT,
        type=int,
        required=False,
        help="KYC page size. Defaults to 1.",
    )
    kyc_list_parser.set_defaults(func=kycs_list, _arg_keys=["limit"])


class JaxlKYCsSDK:
    # pylint: disable=no-self-use
    def list(self, **kwargs: Any) -> Response[PaginatedKycList]:
        return kycs_list(kwargs)
