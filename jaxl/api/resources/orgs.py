"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

import argparse
import functools
from typing import Any, Dict, Optional

from jaxl.api._client import JaxlApiModule, jaxl_api_client
from jaxl.api.client.api.v1 import v1_app_organizations_list
from jaxl.api.client.models.paginated_organization_list import (
    PaginatedOrganizationList,
)
from jaxl.api.client.models.v1_app_organizations_list_status_item import (
    V1AppOrganizationsListStatusItem,
)
from jaxl.api.client.types import Response


@functools.lru_cache(maxsize=1)
def first_org_id() -> int:
    response = orgs_list({"set_org_id": False})
    if response.status_code != 200 or response.parsed is None:
        raise ValueError("Unable to fetch org list")
    return response.parsed.results[0].id


def orgs_list(
    args: Optional[Dict[str, Any]] = None,
) -> Response[PaginatedOrganizationList]:
    args = args or {}
    return v1_app_organizations_list.sync_detailed(
        client=jaxl_api_client(
            JaxlApiModule.ACCOUNT,
            credentials=args.get("credentials", None),
            auth_token=args.get("auth_token", None),
            set_org_id=args.get("set_org_id", True),
        ),
        status=[V1AppOrganizationsListStatusItem.ACCEPTED],
    )


def _subparser(parser: argparse.ArgumentParser) -> None:
    """Manage Organizations"""
    subparsers = parser.add_subparsers(dest="action", required=True)

    orgs_list_parser = subparsers.add_parser("list", help="List organizations")
    orgs_list_parser.set_defaults(
        func=orgs_list,
        _arg_keys=[],
    )


class JaxlOrgsSDK:

    # pylint: disable=no-self-use
    def list(self, **kwargs: Any) -> Response[PaginatedOrganizationList]:
        return orgs_list(kwargs)
