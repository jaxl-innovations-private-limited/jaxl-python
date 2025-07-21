"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

import argparse
from typing import Any, Dict

from jaxl.api._client import JaxlApiModule, jaxl_api_client
from jaxl.api.client.api.v2 import v2_app_organizations_groups_list
from jaxl.api.client.models.paginated_organization_group_response_list import (
    PaginatedOrganizationGroupResponseList,
)
from jaxl.api.client.types import Response


def teams_list(
    args: Dict[str, Any],
) -> Response[PaginatedOrganizationGroupResponseList]:
    return v2_app_organizations_groups_list.sync_detailed(
        org_id="0",
        client=jaxl_api_client(JaxlApiModule.ACCOUNT),
        empty=args.get("empty", True),
    )


def _subparser(parser: argparse.ArgumentParser) -> None:
    """Manage Teams (Managers, Phones)"""
    subparsers = parser.add_subparsers(dest="action", required=True)

    # list
    teams_list_parser = subparsers.add_parser("list", help="List all teams")
    teams_list_parser.add_argument(
        "--empty",
        action="store_true",
        help="Whether to also list empty teams",
    )
    teams_list_parser.set_defaults(func=teams_list, _arg_keys=["empty"])
