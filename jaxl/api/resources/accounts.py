"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

import argparse
from typing import Any, Dict, Optional, Tuple, cast

from jaxl.api._client import JaxlApiModule, jaxl_api_client
from jaxl.api.client.api.v1 import v1_appusers_me_retrieve
from jaxl.api.client.models.app_user import AppUser
from jaxl.api.client.types import Response
from jaxl.api.resources._constants import DEFAULT_CURRENCY
from jaxl.api.resources.calls import calls_usage
from jaxl.api.resources.payments import payments_get_total_recharge


def accounts_me(args: Optional[Dict[str, Any]] = None) -> Response[AppUser]:
    args = args or {}
    return v1_appusers_me_retrieve.sync_detailed(
        client=jaxl_api_client(
            JaxlApiModule.ACCOUNT,
            credentials=args.get("credentials", None),
            auth_token=args.get("auth_token", None),
        )
    )


def accounts_balance(
    args: Dict[str, Any],
) -> Tuple[str, float]:
    total_recharge = payments_get_total_recharge(args)
    if total_recharge.status_code != 200 or total_recharge.parsed is None:
        raise ValueError("Unable to fetch total recharge")
    cusage = calls_usage(args)
    if cusage.status_code != 200 or cusage.parsed is None:
        raise ValueError("Unable to fetch calls usage")
    return (
        total_recharge.parsed.symbol,
        total_recharge.parsed.total - cast(float, cusage.parsed.results[0].cost),
    )


def _subparser(parser: argparse.ArgumentParser) -> None:
    """Manage Accounts"""
    subparsers = parser.add_subparsers(dest="action", required=True)

    me_parser = subparsers.add_parser("me", help="Fetch your account basic details")
    me_parser.set_defaults(
        func=accounts_me,
        _arg_keys=[],
    )

    balance_parser = subparsers.add_parser(
        "balance", help="Fetch current account balance"
    )
    balance_parser.add_argument(
        "--currency",
        default=DEFAULT_CURRENCY,
        type=int,
        required=False,
        help="Call usage currency. Defaults to INR value 2.",
    )
    balance_parser.set_defaults(
        func=accounts_balance,
        _arg_keys=["currency"],
    )


class JaxlAccountsSDK:

    # pylint: disable=no-self-use
    def me(self, **kwargs: Any) -> Response[AppUser]:
        return accounts_me(kwargs)

    def balance(self, **kwargs: Any) -> Tuple[str, float]:
        return accounts_balance(kwargs)
