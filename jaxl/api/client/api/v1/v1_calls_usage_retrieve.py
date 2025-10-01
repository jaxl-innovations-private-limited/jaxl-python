"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.call_usage_response import CallUsageResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    currency: int,
    end_time: Union[Unset, None, datetime.datetime] = UNSET,
    start_time: Union[Unset, None, datetime.datetime] = UNSET,
) -> Dict[str, Any]:
    url = "{}/v1/calls/usage/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["currency"] = currency

    json_end_time: Union[Unset, None, str] = UNSET
    if not isinstance(end_time, Unset):
        json_end_time = end_time.isoformat() if end_time else None

    params["end_time"] = json_end_time

    json_start_time: Union[Unset, None, str] = UNSET
    if not isinstance(start_time, Unset):
        json_start_time = start_time.isoformat() if start_time else None

    params["start_time"] = json_start_time

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
) -> Optional[Union[Any, CallUsageResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CallUsageResponse.from_dict(response.json())

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
) -> Response[Union[Any, CallUsageResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    currency: int,
    end_time: Union[Unset, None, datetime.datetime] = UNSET,
    start_time: Union[Unset, None, datetime.datetime] = UNSET,
) -> Response[Union[Any, CallUsageResponse]]:
    """API view set for Call model.

    Args:
        currency (int):
        end_time (Union[Unset, None, datetime.datetime]):
        start_time (Union[Unset, None, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CallUsageResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        currency=currency,
        end_time=end_time,
        start_time=start_time,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    currency: int,
    end_time: Union[Unset, None, datetime.datetime] = UNSET,
    start_time: Union[Unset, None, datetime.datetime] = UNSET,
) -> Optional[Union[Any, CallUsageResponse]]:
    """API view set for Call model.

    Args:
        currency (int):
        end_time (Union[Unset, None, datetime.datetime]):
        start_time (Union[Unset, None, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CallUsageResponse]]
    """

    return sync_detailed(
        client=client,
        currency=currency,
        end_time=end_time,
        start_time=start_time,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    currency: int,
    end_time: Union[Unset, None, datetime.datetime] = UNSET,
    start_time: Union[Unset, None, datetime.datetime] = UNSET,
) -> Response[Union[Any, CallUsageResponse]]:
    """API view set for Call model.

    Args:
        currency (int):
        end_time (Union[Unset, None, datetime.datetime]):
        start_time (Union[Unset, None, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CallUsageResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        currency=currency,
        end_time=end_time,
        start_time=start_time,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    currency: int,
    end_time: Union[Unset, None, datetime.datetime] = UNSET,
    start_time: Union[Unset, None, datetime.datetime] = UNSET,
) -> Optional[Union[Any, CallUsageResponse]]:
    """API view set for Call model.

    Args:
        currency (int):
        end_time (Union[Unset, None, datetime.datetime]):
        start_time (Union[Unset, None, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CallUsageResponse]]
    """

    return (
        await asyncio_detailed(
            client=client,
            currency=currency,
            end_time=end_time,
            start_time=start_time,
        )
    ).parsed
