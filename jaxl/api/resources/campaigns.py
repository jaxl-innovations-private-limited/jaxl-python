"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

import argparse
import io
from pathlib import Path
from typing import Any, Dict

from jaxl.api._client import JaxlApiModule, encrypt, jaxl_api_client
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
from jaxl.api.client.types import UNSET, File, Response
from jaxl.api.resources._constants import DEFAULT_LIST_LIMIT
from jaxl.api.resources.orgs import first_org_id
from jaxl.api.resources.payments import payments_get_total_recharge


def campaigns_create(args: Dict[str, Any]) -> Response[Campaign]:
    currency = 2
    total_recharge = payments_get_total_recharge({"currency": currency})
    if total_recharge.status_code != 200 or total_recharge.parsed is None:
        raise ValueError("Unable to fetch total recharge")

    # content_type
    content_type = ContentTypeEnum.CSV

    # type
    ttype: CampaignUploadTypeEnum
    if args["type"] == "ai":
        ttype = CampaignUploadTypeEnum.AIAGENT
    elif args["type"] == "ivr":
        ttype = CampaignUploadTypeEnum.MARKETPLACE
    elif args["type"] == "team":
        ttype = CampaignUploadTypeEnum.ORGANIZATION_GROUP
    elif args["type"] == "member":
        ttype = CampaignUploadTypeEnum.ORGANIZATION_EMPLOYEE
    else:
        raise ValueError("Invalid type")

    # type options
    if ttype == CampaignUploadTypeEnum.AIAGENT and args.get("ai_id") is None:
        raise ValueError("Must use --ai-id with type=ai")
    if ttype == CampaignUploadTypeEnum.MARKETPLACE and args.get("ivr_id") is None:
        raise ValueError("Must use --ivr-id with type=ivr")
    if (
        ttype == CampaignUploadTypeEnum.ORGANIZATION_GROUP
        and args.get("team_id") is None
    ):
        raise ValueError("Must use --team-id with type=team")
    if (
        ttype == CampaignUploadTypeEnum.ORGANIZATION_EMPLOYEE
        and args.get("email") is None
    ):
        raise ValueError("Must use --email with type=member")

    # jaxl_id
    jaxl_id: Dict[str, Any]
    if ttype == CampaignUploadTypeEnum.AIAGENT:
        jaxl_id = {"o": "aiagent", "i": args["ai_id"], "oid": first_org_id()}
    else:
        raise ValueError("Not implemented")

    # specification
    spec_path = Path(args["path"])
    payload = io.BytesIO(spec_path.read_bytes())
    payload.seek(0)
    specification = File(
        payload=payload,
        file_name=spec_path.name,
        mime_type="text/csv",
    )

    return v1_campaign_upload_create.sync_detailed(
        client=jaxl_api_client(
            JaxlApiModule.CALL,
            credentials=args.get("credentials", None),
            auth_token=args.get("auth_token", None),
        ),
        multipart_data=CampaignUploadRequest(
            specification=specification,
            content_type=content_type,
            type=ttype,
            jaxl_id=encrypt(jaxl_id),
            run_at=UNSET,
            recharge=total_recharge.parsed.signed,
            currency=currency,
            template=UNSET,
            window=CampaignWindowRequest(
                start=args["start_time"],
                end=args["end_time"],
                tz=args["timezone"],
            ),
            auto_retry=args["auto_retry"],
            cc=args["country_code"],
            options=CampaignUploadRequestOptions(),
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
    campaign_create_parser.add_argument(
        "--country-code",
        type=str,
        required=True,
        help="Default country code. "
        + "Used when phone number does not contain a country code. e.g. IN, US, ...",
    )
    campaign_create_parser.add_argument(
        "--auto-retry",
        action="store_true",
        help="Automatically retry missed, failed and no-response targets",
    )
    campaign_create_parser.add_argument(
        "--start-time",
        type=str,
        default="09:00",
        help="Campaign window start time",
    )
    campaign_create_parser.add_argument(
        "--end-time",
        type=str,
        default="19:00",
        help="Campaign window end time",
    )
    campaign_create_parser.add_argument(
        "--timezone",
        type=str,
        default="Asia/Kolkata",
        help="Campaign window timezone",
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
    campaign_create_parser.set_defaults(
        func=campaigns_create,
        _arg_keys=[
            "path",
            "type",
            "ai_id",
            "ivr_id",
            "team_id",
            "email",
            "country_code",
            "auto_retry",
            "start_time",
            "end_time",
            "timezone",
        ],
    )


class JaxlCampaignsSDK:

    # pylint: disable=no-self-use
    def create(self, **kwargs: Any) -> Response[Campaign]:
        return campaigns_create(kwargs)

    # pylint: disable=no-self-use
    def list(self, **kwargs: Any) -> Response[PaginatedCampaignResponseList]:
        return campaigns_list(kwargs)
