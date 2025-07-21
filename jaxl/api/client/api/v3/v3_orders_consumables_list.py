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
from ...models.paginated_customer_order_consumables_serializer_v2_list import (
    PaginatedCustomerOrderConsumablesSerializerV2List,
)
from ...models.v3_orders_consumables_list_currency import (
    V3OrdersConsumablesListCurrency,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    currency: Union[
        Unset, None, V3OrdersConsumablesListCurrency
    ] = V3OrdersConsumablesListCurrency.VALUE_1,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/v3/orders/consumables/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_currency: Union[Unset, None, int] = UNSET
    if not isinstance(currency, Unset):
        json_currency = currency.value if currency else None

    params["currency"] = json_currency

    params["limit"] = limit

    params["offset"] = offset

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
) -> Optional[PaginatedCustomerOrderConsumablesSerializerV2List]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PaginatedCustomerOrderConsumablesSerializerV2List.from_dict(
            response.json()
        )

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[PaginatedCustomerOrderConsumablesSerializerV2List]:
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
        Unset, None, V3OrdersConsumablesListCurrency
    ] = V3OrdersConsumablesListCurrency.VALUE_1,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
) -> Response[PaginatedCustomerOrderConsumablesSerializerV2List]:
    """
    Args:
        currency (Union[Unset, None, V3OrdersConsumablesListCurrency]):  Default:
            V3OrdersConsumablesListCurrency.VALUE_1.
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedCustomerOrderConsumablesSerializerV2List]
    """

    kwargs = _get_kwargs(
        client=client,
        currency=currency,
        limit=limit,
        offset=offset,
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
        Unset, None, V3OrdersConsumablesListCurrency
    ] = V3OrdersConsumablesListCurrency.VALUE_1,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
) -> Optional[PaginatedCustomerOrderConsumablesSerializerV2List]:
    """
    Args:
        currency (Union[Unset, None, V3OrdersConsumablesListCurrency]):  Default:
            V3OrdersConsumablesListCurrency.VALUE_1.
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedCustomerOrderConsumablesSerializerV2List]
    """

    return sync_detailed(
        client=client,
        currency=currency,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    currency: Union[
        Unset, None, V3OrdersConsumablesListCurrency
    ] = V3OrdersConsumablesListCurrency.VALUE_1,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
) -> Response[PaginatedCustomerOrderConsumablesSerializerV2List]:
    """
    Args:
        currency (Union[Unset, None, V3OrdersConsumablesListCurrency]):  Default:
            V3OrdersConsumablesListCurrency.VALUE_1.
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedCustomerOrderConsumablesSerializerV2List]
    """

    kwargs = _get_kwargs(
        client=client,
        currency=currency,
        limit=limit,
        offset=offset,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    currency: Union[
        Unset, None, V3OrdersConsumablesListCurrency
    ] = V3OrdersConsumablesListCurrency.VALUE_1,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
) -> Optional[PaginatedCustomerOrderConsumablesSerializerV2List]:
    """
    Args:
        currency (Union[Unset, None, V3OrdersConsumablesListCurrency]):  Default:
            V3OrdersConsumablesListCurrency.VALUE_1.
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedCustomerOrderConsumablesSerializerV2List]
    """

    return (
        await asyncio_detailed(
            client=client,
            currency=currency,
            limit=limit,
            offset=offset,
        )
    ).parsed
