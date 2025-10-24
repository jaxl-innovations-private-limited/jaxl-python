"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

import argparse
from typing import Any, Dict

from jaxl.api._client import JaxlApiModule, jaxl_api_client
from jaxl.api.client.api.v1 import (
    v1_app_organizations_providers_list,
    v1_integrations_create,
)
from jaxl.api.client.models.exotel_auth_request_request import (
    ExotelAuthRequestRequest,
)
from jaxl.api.client.models.integrations_properties_request import (
    IntegrationsPropertiesRequest,
)
from jaxl.api.client.models.integrations_request_provider_enum import (
    IntegrationsRequestProviderEnum,
)
from jaxl.api.client.models.integrations_request_request import (
    IntegrationsRequestRequest,
)
from jaxl.api.client.models.integrations_response import IntegrationsResponse
from jaxl.api.client.models.paginated_organization_provider_list import (
    PaginatedOrganizationProviderList,
)
from jaxl.api.client.models.shopify_auth_request_request import (
    ShopifyAuthRequestRequest,
)
from jaxl.api.client.types import Response
from jaxl.api.resources._constants import DEFAULT_LIST_LIMIT
from jaxl.api.resources.orgs import first_org_id


def integrations_list(
    args: Dict[str, Any],
) -> Response[PaginatedOrganizationProviderList]:
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


def integrations_create(args: Dict[str, Any]) -> Response[IntegrationsResponse]:
    print(args)
    success_url = args.get("success_url")
    failure_url = args.get("failure_url")
    print(f"{success_url=} {failure_url=}")
    if args.get("provider") == "shopify":
        properties = IntegrationsPropertiesRequest(
            shopify=ShopifyAuthRequestRequest(shop_name=args.get("shopify_shop_name"))
        )
        provider = IntegrationsRequestProviderEnum.VALUE_26
        if not success_url or not failure_url:
            raise ValueError("Both success_url and failure_url should be provided.")
    elif args.get("provider") == "exotel":
        api_key = args.get("exotel_api_key")
        api_token = args.get("exotel_api_token")
        tenant_id = args.get("exotel_tenant_id")
        flow_id = args.get("exotel_flow_id")
        print(api_key, api_token, tenant_id, flow_id)
        if not (api_key or api_token or tenant_id or flow_id):
            raise ValueError("api_key, api_token, tenant_id, flow_id are required.")
        properties = IntegrationsPropertiesRequest(
            exotel=ExotelAuthRequestRequest(
                api_key=api_key,
                api_token=api_token,
                tenant_id=tenant_id,
                flow_id=flow_id,
            )
        )
        provider = IntegrationsRequestProviderEnum.VALUE_14
    else:
        raise NotImplementedError()
    response = v1_integrations_create.sync_detailed(
        client=jaxl_api_client(
            JaxlApiModule.ACCOUNT,
            credentials=args.get("credentials", None),
            auth_token=args.get("auth_token", None),
        ),
        json_body=IntegrationsRequestRequest(
            provider=provider,
            properties=properties,
            success_url=success_url,
            failure_url=failure_url,
        ),
    )
    print(response.status_code)
    return response


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
        choices=["shopify", "exotel"],
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
    def list(self, **kwargs: Any) -> Response[PaginatedOrganizationProviderList]:
        return integrations_list(kwargs)
