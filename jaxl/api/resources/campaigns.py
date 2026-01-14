"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

import argparse
from typing import Any, Dict

from jaxl.api._client import JaxlApiModule, jaxl_api_client
from jaxl.api.client.api.v1 import v1_campaign_list, v1_campaign_upload_create
from jaxl.api.client.models.campaign import Campaign
from jaxl.api.client.models.campaign_upload_request import (
    CampaignUploadRequest,
)
from jaxl.api.client.models.campaign_upload_request_options import (
    CampaignUploadRequestOptions,
)
from jaxl.api.client.models.campaign_upload_type_enum import (
    CampaignUploadTypeEnum,
)
from jaxl.api.client.models.campaign_window_request import (
    CampaignWindowRequest,
)
from jaxl.api.client.models.content_type_enum import ContentTypeEnum
from jaxl.api.client.models.paginated_campaign_response_list import (
    PaginatedCampaignResponseList,
)
from jaxl.api.client.types import File, Response
from jaxl.api.resources._constants import DEFAULT_LIST_LIMIT
from jaxl.api.resources.payments import payments_get_total_recharge


def campaigns_create(args: Dict[str, Any]) -> Response[Campaign]:
    total_recharge = payments_get_total_recharge({"currency": 2})
    if total_recharge.status_code != 200 or total_recharge.parsed is None:
        raise ValueError("Unable to fetch total recharge")
    return v1_campaign_upload_create.sync_detailed(
        client=jaxl_api_client(
            JaxlApiModule.CALL,
            credentials=args.get("credentials", None),
            auth_token=args.get("auth_token", None),
        ),
        multipart_data=CampaignUploadRequest(
            specification=File(),
            content_type=ContentTypeEnum.CSV,
            type=CampaignUploadTypeEnum.AIAGENT,
            jaxl_id="",
            run_at=None,
            recharge=total_recharge.parsed.signed,
            currency=2,
            template="",
            window=CampaignWindowRequest(start="0900", end="1900", tz=""),
            auto_retry=True,
            cc=None,
            option=CampaignUploadRequestOptions(),
        ),
    )


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

    # create
    campaign_create_parser = subparsers.add_parser("create", help="Create campaign")
    campaign_create_parser.add_argument(
        "--path",
        type=str,
        required=True,
        help="Path to campaign CSV/JSON/YAML file containing targets & metadata",
    )
    campaign_create_parser.add_argument(
        "--type",
        type=str,
        required=True,
        choices=["ai", "ivr", "team", "member"],
        help="Type of campaign to run.  One of the below flag must be provided accordingly",
    )
    group = campaign_create_parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--ai-id",
        type=str,
        required=False,
        choices=["cod", "ndr", "acart", "feedback"],
        help="AI Agent ID",
    )
    group.add_argument(
        "--ivr-id", type=str, required=False, choices=["cod", "ndr"], help="IVR ID"
    )
    group.add_argument(
        "--team-id",
        type=int,
        required=False,
        help="Team ID to whom this CSV must be assigned as tasks",
    )
    group.add_argument(
        "--email",
        type=str,
        required=False,
        help="Member Email ID to whom this CSV must be assigned as tasks",
    )
    campaign_create_parser.set_defaults(func=campaigns_create, _arg_keys=["path"])


class JaxlCampaignsSDK:

    # pylint: disable=no-self-use
    def create(self, **kwargs: Any) -> Response[Campaign]:
        return campaigns_create(kwargs)

    # pylint: disable=no-self-use
    def list(self, **kwargs: Any) -> Response[PaginatedCampaignResponseList]:
        return campaigns_list(kwargs)
