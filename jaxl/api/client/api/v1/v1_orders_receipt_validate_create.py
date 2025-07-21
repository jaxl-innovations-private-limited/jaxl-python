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
from ...models.receipt_validate_request import ReceiptValidateRequest
from ...models.receipt_validate_response import ReceiptValidateResponse
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: ReceiptValidateRequest,
) -> Dict[str, Any]:
    url = "{}/v1/orders/receipt/validate/".format(client.base_url)

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


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[Any, ReceiptValidateResponse]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = ReceiptValidateResponse.from_dict(response.json())

        return response_201
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[Any, ReceiptValidateResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: ReceiptValidateRequest,
) -> Response[Union[Any, ReceiptValidateResponse]]:
    """We have to validate the receipt from Apple/Google Pay.
    For Apple:
    - We validate and store the validated receipt in a json file in /tmp.
    For Apple and Google Pay:
    - We update the order status to PAID for both Consumable and Subscription.
    - We update the provider subscription status to ACTIVE only for Subscription orders.
    - This function will return the payment.pk created

    Args:
        json_body (ReceiptValidateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ReceiptValidateResponse]]
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
    json_body: ReceiptValidateRequest,
) -> Optional[Union[Any, ReceiptValidateResponse]]:
    """We have to validate the receipt from Apple/Google Pay.
    For Apple:
    - We validate and store the validated receipt in a json file in /tmp.
    For Apple and Google Pay:
    - We update the order status to PAID for both Consumable and Subscription.
    - We update the provider subscription status to ACTIVE only for Subscription orders.
    - This function will return the payment.pk created

    Args:
        json_body (ReceiptValidateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ReceiptValidateResponse]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: ReceiptValidateRequest,
) -> Response[Union[Any, ReceiptValidateResponse]]:
    """We have to validate the receipt from Apple/Google Pay.
    For Apple:
    - We validate and store the validated receipt in a json file in /tmp.
    For Apple and Google Pay:
    - We update the order status to PAID for both Consumable and Subscription.
    - We update the provider subscription status to ACTIVE only for Subscription orders.
    - This function will return the payment.pk created

    Args:
        json_body (ReceiptValidateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ReceiptValidateResponse]]
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
    json_body: ReceiptValidateRequest,
) -> Optional[Union[Any, ReceiptValidateResponse]]:
    """We have to validate the receipt from Apple/Google Pay.
    For Apple:
    - We validate and store the validated receipt in a json file in /tmp.
    For Apple and Google Pay:
    - We update the order status to PAID for both Consumable and Subscription.
    - We update the provider subscription status to ACTIVE only for Subscription orders.
    - This function will return the payment.pk created

    Args:
        json_body (ReceiptValidateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ReceiptValidateResponse]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
