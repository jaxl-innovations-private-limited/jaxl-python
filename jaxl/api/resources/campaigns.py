"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

import argparse
from typing import Any, Dict

from jaxl.api._client import JaxlApiModule, jaxl_api_client
from jaxl.api.client.api.v1 import v1_campaign_list
from jaxl.api.client.models.paginated_campaign_response_list import (
    PaginatedCampaignResponseList,
)
from jaxl.api.client.types import Response
from jaxl.api.resources._constants import DEFAULT_LIST_LIMIT


def campaigns_list(args: Dict[str, Any]) -> Response[PaginatedCampaignResponseList]:
    return v1_campaign_list.sync_detailed(
        client=jaxl_api_client(
            JaxlApiModule.CALL,
            credentials=args.get("credentials", None),
            auth_token=args.get("auth_token", None),
        ),
        limit=args.get("limit", DEFAULT_LIST_LIMIT),
        offset=None,
        status=None,
    )


def _subparser(parser: argparse.ArgumentParser) -> None:
    """Manage Campaigns"""
    subparsers = parser.add_subparsers(dest="action", required=True)

    # list
    campaign_list_parser = subparsers.add_parser("list", help="List all Campaigns")
    campaign_list_parser.add_argument(
        "--limit",
        default=DEFAULT_LIST_LIMIT,
        type=int,
        required=False,
        help="Campaign page size. Defaults to 1.",
    )
    campaign_list_parser.set_defaults(func=campaigns_list, _arg_keys=["limit"])


class JaxlCampaignsSDK:

    # pylint: disable=no-self-use
    def list(self, **kwargs: Any) -> Response[PaginatedCampaignResponseList]:
        return campaigns_list(kwargs)
