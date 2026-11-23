"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

import argparse
from typing import Any, Dict, List, Optional

from jaxl.api._client import JaxlApiModule, jaxl_api_client
from jaxl.api.client.api.v2 import v2_app_organizations_employees_list
from jaxl.api.client.models.paginated_organization_employee_list import (
    PaginatedOrganizationEmployeeList,
)
from jaxl.api.client.models.v2_app_organizations_employees_list_status_item import (
    V2AppOrganizationsEmployeesListStatusItem,
)
from jaxl.api.client.types import Response
from jaxl.api.resources._utils import sha256_hexdigest
from jaxl.api.resources.orgs import first_org_id


def _email_hashes(emails: Optional[List[str]]) -> List[str]:
    """Real emails in, sha256 hex digests out (the API filters on hashes).

    Jaxl only accepts lowercase email IDs, so the email ID is hashed
    exactly as given. An empty list fetches every member.
    """
    hashes: List[str] = []
    for email in emails or []:
        digest = sha256_hexdigest(email.strip())
        if digest not in hashes:
            hashes.append(digest)
    return hashes


def members_list(
    args: Dict[str, Any],
) -> Response[PaginatedOrganizationEmployeeList]:
    statuses = []
    for status in list(set(args.get("status", ["accepted"]))):
        statuses.append(V2AppOrganizationsEmployeesListStatusItem[status.upper()])
    return v2_app_organizations_employees_list.sync_detailed(
        org_id=str(first_org_id()),
        client=jaxl_api_client(
            JaxlApiModule.ACCOUNT,
            credentials=args.get("credentials", None),
            auth_token=args.get("auth_token", None),
        ),
        status=statuses,
        email_hash=_email_hashes(args.get("member_email")),
    )


def _subparser(parser: argparse.ArgumentParser) -> None:
    """Manage Members"""
    subparsers = parser.add_subparsers(dest="action", required=True)

    # list
    members_list_parser = subparsers.add_parser("list", help="List all members")
    members_list_parser.add_argument(
        "--email",
        dest="member_email",
        type=str,
        action="append",
        help="Member Email IDs. Can be specified multiple times.",
    )
    members_list_parser.add_argument(
        "--status",
        choices=["canceled", "accepted", "invited", "rejected", "removed"],
        default=["accepted"],
        action="append",
        help="Member statuses. Can be specified multiple times. Default: accepted.",
    )
    members_list_parser.set_defaults(
        func=members_list, _arg_keys=["status", "member_email"]
    )


class JaxlMembersSDK:
    # pylint: disable=no-self-use
    def list(self, **kwargs: Any) -> Response[PaginatedOrganizationEmployeeList]:
        return members_list(kwargs)
