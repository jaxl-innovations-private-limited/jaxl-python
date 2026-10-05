"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

import argparse
from typing import Any, Dict, NamedTuple, Tuple, Type, Union

from jaxl.api._client import JaxlApiModule, jaxl_api_client
from jaxl.api.client.api.v1 import (
    v1_app_organizations_providers_list,
    v1_integrations_create,
)
from jaxl.api.client.models.exotel_auth_request_request import (
    ExotelAuthRequestRequest,
)
from jaxl.api.client.models.integrations_error_response import (
    IntegrationsErrorResponse,
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
from jaxl.api.client.models.invalid_provider_request import (
    InvalidProviderRequest,
)
from jaxl.api.client.models.kwik_engage_auth_request_request import (
    KwikEngageAuthRequestRequest,
)
from jaxl.api.client.models.nimbus_post_auth_request_request import (
    NimbusPostAuthRequestRequest,
)
from jaxl.api.client.models.paginated_organization_provider_list import (
    PaginatedOrganizationProviderList,
)
from jaxl.api.client.models.sales_max_auth_request_request import (
    SalesMaxAuthRequestRequest,
)
from jaxl.api.client.models.shiprocket_delivery_auth_request_request import (
    ShiprocketDeliveryAuthRequestRequest,
)
from jaxl.api.client.models.shopify_auth_request_request import (
    ShopifyAuthRequestRequest,
)
from jaxl.api.client.models.stripe_auth_request_request import (
    StripeAuthRequestRequest,
)
from jaxl.api.client.models.twilio_call_auth_request_request import (
    TwilioCallAuthRequestRequest,
)
from jaxl.api.client.types import UNSET, Response
from jaxl.api.resources._constants import DEFAULT_LIST_LIMIT
from jaxl.api.resources.orgs import first_org_id


class _Field(NamedTuple):
    name: str
    help: str
    required: bool = False
    type: Type[Any] = str


class _Provider(NamedTuple):
    # Provider gateway value expected by the backend
    gateway: IntegrationsRequestProviderEnum
    # Key under request "properties", also used as CLI flag prefix
    key: str
    model: Type[Any]
    fields: Tuple[_Field, ...]
    # Whether success/failure redirect urls are mandatory
    needs_redirect_urls: bool = False


_STRIPE_FIELDS = (
    _Field("publishable_key", "Stripe publishable key"),
    _Field("secret_key", "Stripe secret key"),
    _Field("webhook_signing_secret", "Stripe webhook signing secret"),
)

# Keep in sync with integration providers accepted by POST /v1/integrations/
PROVIDERS: Dict[str, _Provider] = {
    "shopify": _Provider(
        IntegrationsRequestProviderEnum.VALUE_26,
        "shopify",
        ShopifyAuthRequestRequest,
        (
            _Field(
                "shop_name",
                "Shopify shop domain. Example: my-store.myshopify.com",
                required=True,
            ),
        ),
        needs_redirect_urls=True,
    ),
    "shiprocket": _Provider(
        IntegrationsRequestProviderEnum.VALUE_27,
        "shiprocket",
        ShopifyAuthRequestRequest,
        (
            _Field(
                "shop_name",
                "URL of an already connected Shopify shop. "
                + "Example: https://my-store.myshopify.com",
            ),
        ),
    ),
    "shiprocket_delivery": _Provider(
        IntegrationsRequestProviderEnum.VALUE_36,
        "shiprocket_delivery",
        ShiprocketDeliveryAuthRequestRequest,
        (
            _Field("webhook_secret", "Shiprocket delivery webhook secret"),
            _Field(
                "shop_domain",
                "Domain of an already connected Shopify shop. "
                + "Example: my-store.myshopify.com",
            ),
        ),
    ),
    "exotel": _Provider(
        IntegrationsRequestProviderEnum.VALUE_14,
        "exotel",
        ExotelAuthRequestRequest,
        (
            _Field("api_key", "Exotel API key", required=True),
            _Field("api_token", "Exotel API token", required=True),
            _Field("tenant_id", "Exotel tenant ID", required=True),
            _Field("flow_id", "Exotel flow ID", required=True, type=int),
        ),
    ),
    "twilio": _Provider(
        IntegrationsRequestProviderEnum.VALUE_13,
        "twilio",
        TwilioCallAuthRequestRequest,
        (
            _Field("account_sid", "Twilio Account SID", required=True),
            _Field("auth_token", "Twilio Auth Token", required=True),
        ),
    ),
    "stripe": _Provider(
        IntegrationsRequestProviderEnum.VALUE_2,
        "stripe",
        StripeAuthRequestRequest,
        _STRIPE_FIELDS,
    ),
    "stripe_subscription": _Provider(
        IntegrationsRequestProviderEnum.VALUE_6,
        "stripe",
        StripeAuthRequestRequest,
        _STRIPE_FIELDS,
    ),
    "salesmax": _Provider(
        IntegrationsRequestProviderEnum.VALUE_32,
        "salesmax",
        SalesMaxAuthRequestRequest,
        (
            _Field(
                "endpoint_url",
                "Client-specific SalesMax integration URL",
                required=True,
            ),
        ),
    ),
    "nimbuspost": _Provider(
        IntegrationsRequestProviderEnum.VALUE_33,
        "nimbuspost",
        NimbusPostAuthRequestRequest,
        (
            _Field("api_key", "NimbusPost API key", required=True),
            _Field("api_secret", "NimbusPost API secret", required=True),
            _Field("webhook_secret", "NimbusPost webhook secret"),
        ),
    ),
    "kwik_engage": _Provider(
        IntegrationsRequestProviderEnum.VALUE_34,
        "kwik_engage",
        KwikEngageAuthRequestRequest,
        (
            _Field("api_key", "Kwik Engage API key", required=True),
            _Field("merchant_id", "Kwik Engage merchant ID", required=True),
            _Field("waba_id", "WhatsApp Business Account ID", required=True),
            _Field("phone_number_id", "WhatsApp phone number ID", required=True),
            _Field("webhook_secret", "Kwik Engage webhook secret"),
        ),
    ),
}


def _flag(key: str) -> str:
    return "--" + key.replace("_", "-")


def integrations_list(
    args: Dict[str, Any],
) -> Response[Union[Any, InvalidProviderRequest, PaginatedOrganizationProviderList]]:
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


def integrations_create(
    args: Dict[str, Any],
) -> Response[Union[IntegrationsResponse, IntegrationsErrorResponse]]:
    name = args.get("provider")
    if name not in PROVIDERS:
        raise NotImplementedError(
            f"Unknown provider {name}, must be one of {', '.join(PROVIDERS)}"
        )
    provider = PROVIDERS[name]
    success_url = args.get("success_url")
    failure_url = args.get("failure_url")
    if provider.needs_redirect_urls and not (success_url and failure_url):
        raise ValueError("Both success_url and failure_url should be provided.")
    values = {
        field.name: args.get(f"{provider.key}_{field.name}")
        for field in provider.fields
    }
    missing = [
        _flag(f"{provider.key}_{field.name}")
        for field in provider.fields
        if field.required and values[field.name] is None
    ]
    if missing:
        raise ValueError(f"{', '.join(missing)} are required for {name}.")
    properties = IntegrationsPropertiesRequest(
        **{
            provider.key: provider.model(
                **{k: v for k, v in values.items() if v is not None}
            )
        }
    )
    return v1_integrations_create.sync_detailed(
        client=jaxl_api_client(
            JaxlApiModule.ACCOUNT,
            credentials=args.get("credentials", None),
            auth_token=args.get("auth_token", None),
        ),
        json_body=IntegrationsRequestRequest(
            provider=provider.gateway,
            properties=properties,
            success_url=success_url if success_url is not None else UNSET,
            failure_url=failure_url if failure_url is not None else UNSET,
        ),
    )


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
        choices=list(PROVIDERS),
        help="Integration provider.",
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
    arg_keys = ["provider", "success_url", "failure_url"]
    for name, provider in PROVIDERS.items():
        for field in provider.fields:
            key = f"{provider.key}_{field.name}"
            if key in arg_keys:
                # Providers sharing a properties key share their flags
                continue
            arg_keys.append(key)
            integration_create_parser.add_argument(
                _flag(key),
                type=field.type,
                required=False,
                help=f"{field.help} ({'required' if field.required else 'optional'}"
                + f" when provider is '{name}').",
            )
    integration_create_parser.set_defaults(
        func=integrations_create,
        _arg_keys=arg_keys,
    )


class JaxlIntegrationsSDK:
    # pylint: disable=no-self-use
    def list(
        self, **kwargs: Any
    ) -> Response[
        Union[Any, InvalidProviderRequest, PaginatedOrganizationProviderList]
    ]:
        return integrations_list(kwargs)

    # pylint: disable=no-self-use
    def create(
        self, **kwargs: Any
    ) -> Response[Union[IntegrationsResponse, IntegrationsErrorResponse]]:
        return integrations_create(kwargs)
