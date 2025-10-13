"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

import argparse
from typing import Any, Dict

from jaxl.api._client import JaxlApiModule, jaxl_api_client
from jaxl.api.client.api.v1 import v1_customer_consumables_retrieve
from jaxl.api.client.api.v3 import v3_orders_subscriptions_list
from jaxl.api.client.models.customer_consumable_total import (
    CustomerConsumableTotal,
)
from jaxl.api.client.models.paginated_customer_order_subscriptions_serializer_v2_list import (
    PaginatedCustomerOrderSubscriptionsSerializerV2List,
)
from jaxl.api.client.models.v1_customer_consumables_retrieve_currency import (
    V1CustomerConsumablesRetrieveCurrency,
)
from jaxl.api.client.types import Response
from jaxl.api.resources._constants import DEFAULT_CURRENCY, DEFAULT_LIST_LIMIT


def payments_get_total_recharge(
    args: Dict[str, Any],
) -> Response[CustomerConsumableTotal]:
    return v1_customer_consumables_retrieve.sync_detailed(
        client=jaxl_api_client(
            JaxlApiModule.PAYMENT,
            credentials=args.get("credentials", None),
            auth_token=args.get("auth_token", None),
        ),
        currency=V1CustomerConsumablesRetrieveCurrency[f"VALUE_{args['currency']}"],
    )


def payments_subscriptions_list(
    args: Dict[str, Any],
) -> Response[PaginatedCustomerOrderSubscriptionsSerializerV2List]:
    return v3_orders_subscriptions_list.sync_detailed(
        client=jaxl_api_client(
            JaxlApiModule.PAYMENT,
            credentials=args.get("credentials", None),
            auth_token=args.get("auth_token", None),
        ),
        currency=args.get("currency", None),
        item=None,
        status=None,
        limit=args.get("limit", DEFAULT_LIST_LIMIT),
    )


def _subscriptions_subparser(parser: argparse.ArgumentParser) -> None:
    """Returns ivr options resource subparser."""
    subparsers = parser.add_subparsers(dest="action", required=True)

    list_subscriptions = subparsers.add_parser(
        "list",
        help="List active subscriptions",
    )
    list_subscriptions.add_argument(
        "--limit",
        default=DEFAULT_LIST_LIMIT,
        type=int,
        required=False,
        help="Subscriptions page size. Defaults to 1.",
    )
    list_subscriptions.set_defaults(
        func=payments_subscriptions_list,
        _arg_keys=["limit"],
    )


def _consumables_subparser(parser: argparse.ArgumentParser) -> None:
    """Returns ivr options resource subparser."""
    subparsers = parser.add_subparsers(dest="action", required=True)

    total_consumables = subparsers.add_parser(
        "total",
        help="Fetch sum of all successful consumable purchases i.e. total recharge",
    )
    total_consumables.add_argument(
        "--currency",
        default=DEFAULT_CURRENCY,
        type=int,
        required=False,
        help="Call usage currency. Defaults to INR value 2.",
    )
    total_consumables.set_defaults(
        func=payments_get_total_recharge,
        _arg_keys=["currency"],
    )


def _subparser(parser: argparse.ArgumentParser) -> None:
    """Manage Payments"""
    subparsers = parser.add_subparsers(dest="action", required=True)

    # subscriptions
    _subscriptions_subparser(
        subparsers.add_parser(
            "subscriptions",
            help="Manage Subscriptions",
        )
    )

    # consumables
    _consumables_subparser(
        subparsers.add_parser(
            "consumables",
            help="Manage Consumables",
        )
    )


class JaxlPaymentSubscriptionsSDK:
    # pylint: disable=no-self-use
    def list(
        self, **kwargs: Any
    ) -> Response[PaginatedCustomerOrderSubscriptionsSerializerV2List]:
        return payments_subscriptions_list(kwargs)


class JaxlPaymentConsumablesSDK:
    # pylint: disable=no-self-use
    def total(self, **kwargs: Any) -> Response[CustomerConsumableTotal]:
        return payments_get_total_recharge(kwargs)


class JaxlPaymentsSDK:
    def __init__(self) -> None:
        self.subscriptions = JaxlPaymentSubscriptionsSDK()
        self.consumables = JaxlPaymentConsumablesSDK()
