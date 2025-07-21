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
from ...models.pricing_error import PricingError
from ...models.pricing_response import PricingResponse
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/v1/pricing/data/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[PricingError, PricingResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PricingResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = PricingError.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = PricingError.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[PricingError, PricingResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Union[PricingError, PricingResponse]]:
    r"""Return pricing CSV data as JSON.

    The following are the columns in CSV:
    \"ISO\",
    \"Country\",
    \"Phone Number Type\",
    \"SMS Enabled\",
    \"SMS Price / msg\",
    \"Voice Enabled\",
    \"Incoming Price / min\",
    \"Outgoing Price Min / min\",
    \"Outgoing Price Max / min\",
    \"Recording Enabled\",
    \"Recording Price / min\",
    \"Stripe Monthly\",
    \"Android Monthly\",
    \"iOS Monthly\",

    Currently does not include Quarterly, Half Yearly and Yearly pricing.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PricingError, PricingResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> Optional[Union[PricingError, PricingResponse]]:
    r"""Return pricing CSV data as JSON.

    The following are the columns in CSV:
    \"ISO\",
    \"Country\",
    \"Phone Number Type\",
    \"SMS Enabled\",
    \"SMS Price / msg\",
    \"Voice Enabled\",
    \"Incoming Price / min\",
    \"Outgoing Price Min / min\",
    \"Outgoing Price Max / min\",
    \"Recording Enabled\",
    \"Recording Price / min\",
    \"Stripe Monthly\",
    \"Android Monthly\",
    \"iOS Monthly\",

    Currently does not include Quarterly, Half Yearly and Yearly pricing.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PricingError, PricingResponse]]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Union[PricingError, PricingResponse]]:
    r"""Return pricing CSV data as JSON.

    The following are the columns in CSV:
    \"ISO\",
    \"Country\",
    \"Phone Number Type\",
    \"SMS Enabled\",
    \"SMS Price / msg\",
    \"Voice Enabled\",
    \"Incoming Price / min\",
    \"Outgoing Price Min / min\",
    \"Outgoing Price Max / min\",
    \"Recording Enabled\",
    \"Recording Price / min\",
    \"Stripe Monthly\",
    \"Android Monthly\",
    \"iOS Monthly\",

    Currently does not include Quarterly, Half Yearly and Yearly pricing.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PricingError, PricingResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Optional[Union[PricingError, PricingResponse]]:
    r"""Return pricing CSV data as JSON.

    The following are the columns in CSV:
    \"ISO\",
    \"Country\",
    \"Phone Number Type\",
    \"SMS Enabled\",
    \"SMS Price / msg\",
    \"Voice Enabled\",
    \"Incoming Price / min\",
    \"Outgoing Price Min / min\",
    \"Outgoing Price Max / min\",
    \"Recording Enabled\",
    \"Recording Price / min\",
    \"Stripe Monthly\",
    \"Android Monthly\",
    \"iOS Monthly\",

    Currently does not include Quarterly, Half Yearly and Yearly pricing.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PricingError, PricingResponse]]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
