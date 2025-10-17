"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

import argparse
from typing import Any, Dict

from jaxl.api._client import JaxlApiModule, jaxl_api_client
from jaxl.api.client.api.v1 import v1_app_organizations_providers_list
from jaxl.api.client.models.integrations_request_provider_enum import (
    IntegrationsRequestProviderEnum,
)
from jaxl.api.resources._constants import DEFAULT_LIST_LIMIT
from jaxl.api.resources.orgs import first_org_id


def integrations_list(args: Dict[str, Any]) -> Any:
    print(args)
    return v1_app_organizations_providers_list.sync_detailed(
        client=jaxl_api_client(
            JaxlApiModule.ACCOUNT,
            credentials=args.get("credentials", None),
            auth_token=args.get("auth_token", None),
        ),
        org_id=str(first_org_id()),
        limit=args.get("limit", DEFAULT_LIST_LIMIT),
        offset=None,
    )


def integrations_create(args: Dict[str, Any]) -> str:
    print(args)
    return "Output of create"


def _subparser(parser: argparse.ArgumentParser) -> None:
    """Manage Integrations"""
    subparsers = parser.add_subparsers(dest="action", required=True)

    # list
    integration_list_parser = subparsers.add_parser(
        "list", help="List all Integrations"
    )
    integration_list_parser.add_argument(
        "--limit",
        default=DEFAULT_LIST_LIMIT,
        type=int,
        required=False,
        help="Integration page size. Defaults to 1.",
    )
    integration_list_parser.set_defaults(func=integrations_list, _arg_keys=["limit"])

    # create
    integration_create_parser = subparsers.add_parser("create", help="Add integration")
    integration_create_parser.add_argument(
        "--provider",
        required=True,
        choices=[
            IntegrationsRequestProviderEnum.VALUE_14,
            IntegrationsRequestProviderEnum.VALUE_26,
        ],
        help="Integration provider. Example: 'shopify' or 'exotel'.",
    )
    integration_create_parser.add_argument(
        "--success-url",
        required=False,
        help="URL to redirect upon successful integration setup.",
    )
    integration_create_parser.add_argument(
        "--failure-url",
        required=False,
        help="URL to redirect upon failed integration setup.",
    )

    # Nested: Shopify
    integration_create_parser.add_argument(
        "--shopify-shop-name",
        required=False,
        help="Shopify shop name (if provider is 'shopify').",
    )

    # Nested: Exotel
    integration_create_parser.add_argument(
        "--exotel-api-key",
        required=False,
        help="Exotel API key (if provider is 'exotel').",
    )
    integration_create_parser.add_argument(
        "--exotel-api-token",
        required=False,
        help="Exotel API token (if provider is 'exotel').",
    )
    integration_create_parser.add_argument(
        "--exotel-tenant-id",
        required=False,
        help="Exotel tenant ID (if provider is 'exotel').",
    )
    integration_create_parser.add_argument(
        "--exotel-flow-id",
        type=int,
        required=False,
        help="Exotel flow ID (integer, if provider is 'exotel').",
    )

    integration_create_parser.set_defaults(
        func=integrations_create,
        _arg_keys=[
            "provider",
            "success_url",
            "failure_url",
            "shopify_shop_name",
            "exotel_api_key",
            "exotel_api_token",
            "exotel_tenant_id",
            "exotel_flow_id",
        ],
    )


class JaxlIntegrationsSDK:
    # pylint: disable=no-self-use
    def list(self, **kwargs: Any) -> str:
        return integrations_list(kwargs)
