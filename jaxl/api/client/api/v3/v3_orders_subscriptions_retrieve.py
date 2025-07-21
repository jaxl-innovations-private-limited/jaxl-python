"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.customer_order_subscriptions_serializer_v2 import (
    CustomerOrderSubscriptionsSerializerV2,
)
from ...models.v3_orders_subscriptions_retrieve_currency import (
    V3OrdersSubscriptionsRetrieveCurrency,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    client: AuthenticatedClient,
    currency: Union[
        Unset, None, V3OrdersSubscriptionsRetrieveCurrency
    ] = V3OrdersSubscriptionsRetrieveCurrency.VALUE_1,
) -> Dict[str, Any]:
    url = "{}/v3/orders/subscriptions/{id}/".format(client.base_url, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_currency: Union[Unset, None, int] = UNSET
    if not isinstance(currency, Unset):
        json_currency = currency.value if currency else None

    params["currency"] = json_currency

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[CustomerOrderSubscriptionsSerializerV2]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CustomerOrderSubscriptionsSerializerV2.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[CustomerOrderSubscriptionsSerializerV2]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    currency: Union[
        Unset, None, V3OrdersSubscriptionsRetrieveCurrency
    ] = V3OrdersSubscriptionsRetrieveCurrency.VALUE_1,
) -> Response[CustomerOrderSubscriptionsSerializerV2]:
    """
    Args:
        id (int):
        currency (Union[Unset, None, V3OrdersSubscriptionsRetrieveCurrency]):  Default:
            V3OrdersSubscriptionsRetrieveCurrency.VALUE_1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CustomerOrderSubscriptionsSerializerV2]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        currency=currency,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    currency: Union[
        Unset, None, V3OrdersSubscriptionsRetrieveCurrency
    ] = V3OrdersSubscriptionsRetrieveCurrency.VALUE_1,
) -> Optional[CustomerOrderSubscriptionsSerializerV2]:
    """
    Args:
        id (int):
        currency (Union[Unset, None, V3OrdersSubscriptionsRetrieveCurrency]):  Default:
            V3OrdersSubscriptionsRetrieveCurrency.VALUE_1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CustomerOrderSubscriptionsSerializerV2]
    """

    return sync_detailed(
        id=id,
        client=client,
        currency=currency,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    currency: Union[
        Unset, None, V3OrdersSubscriptionsRetrieveCurrency
    ] = V3OrdersSubscriptionsRetrieveCurrency.VALUE_1,
) -> Response[CustomerOrderSubscriptionsSerializerV2]:
    """
    Args:
        id (int):
        currency (Union[Unset, None, V3OrdersSubscriptionsRetrieveCurrency]):  Default:
            V3OrdersSubscriptionsRetrieveCurrency.VALUE_1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CustomerOrderSubscriptionsSerializerV2]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        currency=currency,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    currency: Union[
        Unset, None, V3OrdersSubscriptionsRetrieveCurrency
    ] = V3OrdersSubscriptionsRetrieveCurrency.VALUE_1,
) -> Optional[CustomerOrderSubscriptionsSerializerV2]:
    """
    Args:
        id (int):
        currency (Union[Unset, None, V3OrdersSubscriptionsRetrieveCurrency]):  Default:
            V3OrdersSubscriptionsRetrieveCurrency.VALUE_1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CustomerOrderSubscriptionsSerializerV2]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            currency=currency,
        )
    ).parsed
