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
from ...models.plan import Plan
from ...models.v1_plans_retrieve_currency import V1PlansRetrieveCurrency
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    client: AuthenticatedClient,
    currency: V1PlansRetrieveCurrency,
    gateway: Union[Unset, None, int] = UNSET,
    usage: Union[Unset, None, float] = UNSET,
) -> Dict[str, Any]:
    url = "{}/v1/plans/{id}/".format(client.base_url, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_currency = currency.value

    params["currency"] = json_currency

    params["gateway"] = gateway

    params["usage"] = usage

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
) -> Optional[Union[Any, Plan]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Plan.from_dict(response.json())

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
) -> Response[Union[Any, Plan]]:
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
    currency: V1PlansRetrieveCurrency,
    gateway: Union[Unset, None, int] = UNSET,
    usage: Union[Unset, None, float] = UNSET,
) -> Response[Union[Any, Plan]]:
    """Retrives plan from plan id for a given app

    Args:
        id (int):
        currency (V1PlansRetrieveCurrency):
        gateway (Union[Unset, None, int]):
        usage (Union[Unset, None, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Plan]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        currency=currency,
        gateway=gateway,
        usage=usage,
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
    currency: V1PlansRetrieveCurrency,
    gateway: Union[Unset, None, int] = UNSET,
    usage: Union[Unset, None, float] = UNSET,
) -> Optional[Union[Any, Plan]]:
    """Retrives plan from plan id for a given app

    Args:
        id (int):
        currency (V1PlansRetrieveCurrency):
        gateway (Union[Unset, None, int]):
        usage (Union[Unset, None, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Plan]]
    """

    return sync_detailed(
        id=id,
        client=client,
        currency=currency,
        gateway=gateway,
        usage=usage,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    currency: V1PlansRetrieveCurrency,
    gateway: Union[Unset, None, int] = UNSET,
    usage: Union[Unset, None, float] = UNSET,
) -> Response[Union[Any, Plan]]:
    """Retrives plan from plan id for a given app

    Args:
        id (int):
        currency (V1PlansRetrieveCurrency):
        gateway (Union[Unset, None, int]):
        usage (Union[Unset, None, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Plan]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        currency=currency,
        gateway=gateway,
        usage=usage,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    currency: V1PlansRetrieveCurrency,
    gateway: Union[Unset, None, int] = UNSET,
    usage: Union[Unset, None, float] = UNSET,
) -> Optional[Union[Any, Plan]]:
    """Retrives plan from plan id for a given app

    Args:
        id (int):
        currency (V1PlansRetrieveCurrency):
        gateway (Union[Unset, None, int]):
        usage (Union[Unset, None, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Plan]]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            currency=currency,
            gateway=gateway,
            usage=usage,
        )
    ).parsed
