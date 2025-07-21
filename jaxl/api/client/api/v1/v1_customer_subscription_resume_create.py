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
from ...models.cannot_resume_subscription_response import (
    CannotResumeSubscriptionResponse,
)
from ...models.resume_subscription_response import ResumeSubscriptionResponse
from ...types import UNSET, Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    order_id: int,
) -> Dict[str, Any]:
    url = "{}/v1/customer/subscription/resume/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["order_id"] = order_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[CannotResumeSubscriptionResponse, ResumeSubscriptionResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ResumeSubscriptionResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = CannotResumeSubscriptionResponse.from_dict(response.json())

        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[CannotResumeSubscriptionResponse, ResumeSubscriptionResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    order_id: int,
) -> Response[Union[CannotResumeSubscriptionResponse, ResumeSubscriptionResponse]]:
    """
    Args:
        order_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CannotResumeSubscriptionResponse, ResumeSubscriptionResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        order_id=order_id,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    order_id: int,
) -> Optional[Union[CannotResumeSubscriptionResponse, ResumeSubscriptionResponse]]:
    """
    Args:
        order_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CannotResumeSubscriptionResponse, ResumeSubscriptionResponse]]
    """

    return sync_detailed(
        client=client,
        order_id=order_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    order_id: int,
) -> Response[Union[CannotResumeSubscriptionResponse, ResumeSubscriptionResponse]]:
    """
    Args:
        order_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CannotResumeSubscriptionResponse, ResumeSubscriptionResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        order_id=order_id,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    order_id: int,
) -> Optional[Union[CannotResumeSubscriptionResponse, ResumeSubscriptionResponse]]:
    """
    Args:
        order_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CannotResumeSubscriptionResponse, ResumeSubscriptionResponse]]
    """

    return (
        await asyncio_detailed(
            client=client,
            order_id=order_id,
        )
    ).parsed
