"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_customer_order_subscriptions_serializer_v2_list import (
    PaginatedCustomerOrderSubscriptionsSerializerV2List,
)
from ...models.v3_orders_subscriptions_list_currency import (
    V3OrdersSubscriptionsListCurrency,
)
from ...models.v3_orders_subscriptions_list_status_item import (
    V3OrdersSubscriptionsListStatusItem,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    currency: Union[
        Unset, None, V3OrdersSubscriptionsListCurrency
    ] = V3OrdersSubscriptionsListCurrency.VALUE_1,
    item: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    sku: Union[Unset, None, str] = UNSET,
    status: Union[Unset, None, List[V3OrdersSubscriptionsListStatusItem]] = UNSET,
) -> Dict[str, Any]:
    url = "{}/v3/orders/subscriptions/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_currency: Union[Unset, None, int] = UNSET
    if not isinstance(currency, Unset):
        json_currency = currency.value if currency else None

    params["currency"] = json_currency

    params["item"] = item

    params["limit"] = limit

    params["offset"] = offset

    params["sku"] = sku

    json_status: Union[Unset, None, List[str]] = UNSET
    if not isinstance(status, Unset):
        if status is None:
            json_status = None
        else:
            json_status = []
            for status_item_data in status:
                status_item = status_item_data.value

                json_status.append(status_item)

    params["status"] = json_status

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
) -> Optional[PaginatedCustomerOrderSubscriptionsSerializerV2List]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PaginatedCustomerOrderSubscriptionsSerializerV2List.from_dict(
            response.json()
        )

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[PaginatedCustomerOrderSubscriptionsSerializerV2List]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    currency: Union[
        Unset, None, V3OrdersSubscriptionsListCurrency
    ] = V3OrdersSubscriptionsListCurrency.VALUE_1,
    item: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    sku: Union[Unset, None, str] = UNSET,
    status: Union[Unset, None, List[V3OrdersSubscriptionsListStatusItem]] = UNSET,
) -> Response[PaginatedCustomerOrderSubscriptionsSerializerV2List]:
    """
    Args:
        currency (Union[Unset, None, V3OrdersSubscriptionsListCurrency]):  Default:
            V3OrdersSubscriptionsListCurrency.VALUE_1.
        item (Union[Unset, None, str]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        sku (Union[Unset, None, str]):
        status (Union[Unset, None, List[V3OrdersSubscriptionsListStatusItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedCustomerOrderSubscriptionsSerializerV2List]
    """

    kwargs = _get_kwargs(
        client=client,
        currency=currency,
        item=item,
        limit=limit,
        offset=offset,
        sku=sku,
        status=status,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    currency: Union[
        Unset, None, V3OrdersSubscriptionsListCurrency
    ] = V3OrdersSubscriptionsListCurrency.VALUE_1,
    item: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    sku: Union[Unset, None, str] = UNSET,
    status: Union[Unset, None, List[V3OrdersSubscriptionsListStatusItem]] = UNSET,
) -> Optional[PaginatedCustomerOrderSubscriptionsSerializerV2List]:
    """
    Args:
        currency (Union[Unset, None, V3OrdersSubscriptionsListCurrency]):  Default:
            V3OrdersSubscriptionsListCurrency.VALUE_1.
        item (Union[Unset, None, str]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        sku (Union[Unset, None, str]):
        status (Union[Unset, None, List[V3OrdersSubscriptionsListStatusItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedCustomerOrderSubscriptionsSerializerV2List]
    """

    return sync_detailed(
        client=client,
        currency=currency,
        item=item,
        limit=limit,
        offset=offset,
        sku=sku,
        status=status,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    currency: Union[
        Unset, None, V3OrdersSubscriptionsListCurrency
    ] = V3OrdersSubscriptionsListCurrency.VALUE_1,
    item: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    sku: Union[Unset, None, str] = UNSET,
    status: Union[Unset, None, List[V3OrdersSubscriptionsListStatusItem]] = UNSET,
) -> Response[PaginatedCustomerOrderSubscriptionsSerializerV2List]:
    """
    Args:
        currency (Union[Unset, None, V3OrdersSubscriptionsListCurrency]):  Default:
            V3OrdersSubscriptionsListCurrency.VALUE_1.
        item (Union[Unset, None, str]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        sku (Union[Unset, None, str]):
        status (Union[Unset, None, List[V3OrdersSubscriptionsListStatusItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedCustomerOrderSubscriptionsSerializerV2List]
    """

    kwargs = _get_kwargs(
        client=client,
        currency=currency,
        item=item,
        limit=limit,
        offset=offset,
        sku=sku,
        status=status,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    currency: Union[
        Unset, None, V3OrdersSubscriptionsListCurrency
    ] = V3OrdersSubscriptionsListCurrency.VALUE_1,
    item: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    sku: Union[Unset, None, str] = UNSET,
    status: Union[Unset, None, List[V3OrdersSubscriptionsListStatusItem]] = UNSET,
) -> Optional[PaginatedCustomerOrderSubscriptionsSerializerV2List]:
    """
    Args:
        currency (Union[Unset, None, V3OrdersSubscriptionsListCurrency]):  Default:
            V3OrdersSubscriptionsListCurrency.VALUE_1.
        item (Union[Unset, None, str]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        sku (Union[Unset, None, str]):
        status (Union[Unset, None, List[V3OrdersSubscriptionsListStatusItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedCustomerOrderSubscriptionsSerializerV2List]
    """

    return (
        await asyncio_detailed(
            client=client,
            currency=currency,
            item=item,
            limit=limit,
            offset=offset,
            sku=sku,
            status=status,
        )
    ).parsed
