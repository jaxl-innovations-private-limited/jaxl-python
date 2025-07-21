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
from ...models.customer_cannot_checkout_due_to_ongoing_checkout import (
    CustomerCannotCheckoutDueToOngoingCheckout,
)
from ...models.customer_cannot_purchase_item import CustomerCannotPurchaseItem
from ...models.order_checkout_response import OrderCheckoutResponse
from ...models.plan_price_gateway_request import PlanPriceGatewayRequest
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: PlanPriceGatewayRequest,
) -> Dict[str, Any]:
    url = "{}/v1/orders/checkout/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[
    Union[
        CustomerCannotCheckoutDueToOngoingCheckout,
        CustomerCannotPurchaseItem,
        OrderCheckoutResponse,
    ]
]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = OrderCheckoutResponse.from_dict(response.json())

        return response_201
    if response.status_code == HTTPStatus.EXPECTATION_FAILED:
        response_417 = CustomerCannotPurchaseItem.from_dict(response.json())

        return response_417
    if response.status_code == HTTPStatus.GONE:
        response_410 = CustomerCannotPurchaseItem.from_dict(response.json())

        return response_410
    if response.status_code == HTTPStatus.CONFLICT:
        response_409 = CustomerCannotPurchaseItem.from_dict(response.json())

        return response_409
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = CustomerCannotPurchaseItem.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.NOT_ACCEPTABLE:
        response_406 = CustomerCannotCheckoutDueToOngoingCheckout.from_dict(
            response.json()
        )

        return response_406
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = CustomerCannotPurchaseItem.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[
    Union[
        CustomerCannotCheckoutDueToOngoingCheckout,
        CustomerCannotPurchaseItem,
        OrderCheckoutResponse,
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: PlanPriceGatewayRequest,
) -> Response[
    Union[
        CustomerCannotCheckoutDueToOngoingCheckout,
        CustomerCannotPurchaseItem,
        OrderCheckoutResponse,
    ]
]:
    """
    Args:
        json_body (PlanPriceGatewayRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CustomerCannotCheckoutDueToOngoingCheckout, CustomerCannotPurchaseItem, OrderCheckoutResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    json_body: PlanPriceGatewayRequest,
) -> Optional[
    Union[
        CustomerCannotCheckoutDueToOngoingCheckout,
        CustomerCannotPurchaseItem,
        OrderCheckoutResponse,
    ]
]:
    """
    Args:
        json_body (PlanPriceGatewayRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CustomerCannotCheckoutDueToOngoingCheckout, CustomerCannotPurchaseItem, OrderCheckoutResponse]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: PlanPriceGatewayRequest,
) -> Response[
    Union[
        CustomerCannotCheckoutDueToOngoingCheckout,
        CustomerCannotPurchaseItem,
        OrderCheckoutResponse,
    ]
]:
    """
    Args:
        json_body (PlanPriceGatewayRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CustomerCannotCheckoutDueToOngoingCheckout, CustomerCannotPurchaseItem, OrderCheckoutResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    json_body: PlanPriceGatewayRequest,
) -> Optional[
    Union[
        CustomerCannotCheckoutDueToOngoingCheckout,
        CustomerCannotPurchaseItem,
        OrderCheckoutResponse,
    ]
]:
    """
    Args:
        json_body (PlanPriceGatewayRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CustomerCannotCheckoutDueToOngoingCheckout, CustomerCannotPurchaseItem, OrderCheckoutResponse]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
