"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_payment_list import PaginatedPaymentList
from ...models.v1_payments_list_currency import V1PaymentsListCurrency
from ...models.v1_payments_list_subscription_type import (
    V1PaymentsListSubscriptionType,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    currency: Union[
        Unset, None, V1PaymentsListCurrency
    ] = V1PaymentsListCurrency.VALUE_1,
    historical: Union[Unset, None, bool] = False,
    item_type: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    order_id: Union[Unset, None, int] = UNSET,
    subscription_type: Union[Unset, None, V1PaymentsListSubscriptionType] = UNSET,
) -> Dict[str, Any]:
    url = "{}/v1/payments/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_currency: Union[Unset, None, int] = UNSET
    if not isinstance(currency, Unset):
        json_currency = currency.value if currency else None

    params["currency"] = json_currency

    params["historical"] = historical

    params["item_type"] = item_type

    params["limit"] = limit

    params["offset"] = offset

    params["order_id"] = order_id

    json_subscription_type: Union[Unset, None, str] = UNSET
    if not isinstance(subscription_type, Unset):
        json_subscription_type = subscription_type.value if subscription_type else None

    params["subscription_type"] = json_subscription_type

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
) -> Optional[Union[Any, PaginatedPaymentList]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PaginatedPaymentList.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[Any, PaginatedPaymentList]]:
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
        Unset, None, V1PaymentsListCurrency
    ] = V1PaymentsListCurrency.VALUE_1,
    historical: Union[Unset, None, bool] = False,
    item_type: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    order_id: Union[Unset, None, int] = UNSET,
    subscription_type: Union[Unset, None, V1PaymentsListSubscriptionType] = UNSET,
) -> Response[Union[Any, PaginatedPaymentList]]:
    """
    Args:
        currency (Union[Unset, None, V1PaymentsListCurrency]):  Default:
            V1PaymentsListCurrency.VALUE_1.
        historical (Union[Unset, None, bool]):
        item_type (Union[Unset, None, str]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        order_id (Union[Unset, None, int]):
        subscription_type (Union[Unset, None, V1PaymentsListSubscriptionType]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PaginatedPaymentList]]
    """

    kwargs = _get_kwargs(
        client=client,
        currency=currency,
        historical=historical,
        item_type=item_type,
        limit=limit,
        offset=offset,
        order_id=order_id,
        subscription_type=subscription_type,
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
        Unset, None, V1PaymentsListCurrency
    ] = V1PaymentsListCurrency.VALUE_1,
    historical: Union[Unset, None, bool] = False,
    item_type: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    order_id: Union[Unset, None, int] = UNSET,
    subscription_type: Union[Unset, None, V1PaymentsListSubscriptionType] = UNSET,
) -> Optional[Union[Any, PaginatedPaymentList]]:
    """
    Args:
        currency (Union[Unset, None, V1PaymentsListCurrency]):  Default:
            V1PaymentsListCurrency.VALUE_1.
        historical (Union[Unset, None, bool]):
        item_type (Union[Unset, None, str]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        order_id (Union[Unset, None, int]):
        subscription_type (Union[Unset, None, V1PaymentsListSubscriptionType]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PaginatedPaymentList]]
    """

    return sync_detailed(
        client=client,
        currency=currency,
        historical=historical,
        item_type=item_type,
        limit=limit,
        offset=offset,
        order_id=order_id,
        subscription_type=subscription_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    currency: Union[
        Unset, None, V1PaymentsListCurrency
    ] = V1PaymentsListCurrency.VALUE_1,
    historical: Union[Unset, None, bool] = False,
    item_type: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    order_id: Union[Unset, None, int] = UNSET,
    subscription_type: Union[Unset, None, V1PaymentsListSubscriptionType] = UNSET,
) -> Response[Union[Any, PaginatedPaymentList]]:
    """
    Args:
        currency (Union[Unset, None, V1PaymentsListCurrency]):  Default:
            V1PaymentsListCurrency.VALUE_1.
        historical (Union[Unset, None, bool]):
        item_type (Union[Unset, None, str]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        order_id (Union[Unset, None, int]):
        subscription_type (Union[Unset, None, V1PaymentsListSubscriptionType]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PaginatedPaymentList]]
    """

    kwargs = _get_kwargs(
        client=client,
        currency=currency,
        historical=historical,
        item_type=item_type,
        limit=limit,
        offset=offset,
        order_id=order_id,
        subscription_type=subscription_type,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    currency: Union[
        Unset, None, V1PaymentsListCurrency
    ] = V1PaymentsListCurrency.VALUE_1,
    historical: Union[Unset, None, bool] = False,
    item_type: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    order_id: Union[Unset, None, int] = UNSET,
    subscription_type: Union[Unset, None, V1PaymentsListSubscriptionType] = UNSET,
) -> Optional[Union[Any, PaginatedPaymentList]]:
    """
    Args:
        currency (Union[Unset, None, V1PaymentsListCurrency]):  Default:
            V1PaymentsListCurrency.VALUE_1.
        historical (Union[Unset, None, bool]):
        item_type (Union[Unset, None, str]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        order_id (Union[Unset, None, int]):
        subscription_type (Union[Unset, None, V1PaymentsListSubscriptionType]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PaginatedPaymentList]]
    """

    return (
        await asyncio_detailed(
            client=client,
            currency=currency,
            historical=historical,
            item_type=item_type,
            limit=limit,
            offset=offset,
            order_id=order_id,
            subscription_type=subscription_type,
        )
    ).parsed
