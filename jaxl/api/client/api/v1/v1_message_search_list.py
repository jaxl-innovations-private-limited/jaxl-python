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
from ...models.paginated_message_search_response_list import (
    PaginatedMessageSearchResponseList,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, None, int] = UNSET,
    limit_per_message: Union[Unset, None, int] = UNSET,
    message_limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    text: str,
) -> Dict[str, Any]:
    url = "{}/v1/message/search/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["limit"] = limit

    params["limit_per_message"] = limit_per_message

    params["message_limit"] = message_limit

    params["offset"] = offset

    params["text"] = text

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
) -> Optional[PaginatedMessageSearchResponseList]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PaginatedMessageSearchResponseList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[PaginatedMessageSearchResponseList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, None, int] = UNSET,
    limit_per_message: Union[Unset, None, int] = UNSET,
    message_limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    text: str,
) -> Response[PaginatedMessageSearchResponseList]:
    """
    Args:
        limit (Union[Unset, None, int]):
        limit_per_message (Union[Unset, None, int]):
        message_limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        text (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedMessageSearchResponseList]
    """

    kwargs = _get_kwargs(
        client=client,
        limit=limit,
        limit_per_message=limit_per_message,
        message_limit=message_limit,
        offset=offset,
        text=text,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, None, int] = UNSET,
    limit_per_message: Union[Unset, None, int] = UNSET,
    message_limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    text: str,
) -> Optional[PaginatedMessageSearchResponseList]:
    """
    Args:
        limit (Union[Unset, None, int]):
        limit_per_message (Union[Unset, None, int]):
        message_limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        text (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedMessageSearchResponseList]
    """

    return sync_detailed(
        client=client,
        limit=limit,
        limit_per_message=limit_per_message,
        message_limit=message_limit,
        offset=offset,
        text=text,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, None, int] = UNSET,
    limit_per_message: Union[Unset, None, int] = UNSET,
    message_limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    text: str,
) -> Response[PaginatedMessageSearchResponseList]:
    """
    Args:
        limit (Union[Unset, None, int]):
        limit_per_message (Union[Unset, None, int]):
        message_limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        text (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedMessageSearchResponseList]
    """

    kwargs = _get_kwargs(
        client=client,
        limit=limit,
        limit_per_message=limit_per_message,
        message_limit=message_limit,
        offset=offset,
        text=text,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, None, int] = UNSET,
    limit_per_message: Union[Unset, None, int] = UNSET,
    message_limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    text: str,
) -> Optional[PaginatedMessageSearchResponseList]:
    """
    Args:
        limit (Union[Unset, None, int]):
        limit_per_message (Union[Unset, None, int]):
        message_limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        text (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedMessageSearchResponseList]
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            limit_per_message=limit_per_message,
            message_limit=message_limit,
            offset=offset,
            text=text,
        )
    ).parsed
