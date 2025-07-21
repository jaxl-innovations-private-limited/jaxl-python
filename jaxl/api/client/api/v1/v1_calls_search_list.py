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
from ...models.invalid_call_search_response import InvalidCallSearchResponse
from ...models.paginated_call_search_response_list import (
    PaginatedCallSearchResponseList,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    text: str,
) -> Dict[str, Any]:
    url = "{}/v1/calls/search/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["limit"] = limit

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
) -> Optional[Union[InvalidCallSearchResponse, PaginatedCallSearchResponseList]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PaginatedCallSearchResponseList.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = InvalidCallSearchResponse.from_dict(response.json())

        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[InvalidCallSearchResponse, PaginatedCallSearchResponseList]]:
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
    offset: Union[Unset, None, int] = UNSET,
    text: str,
) -> Response[Union[InvalidCallSearchResponse, PaginatedCallSearchResponseList]]:
    """Searches for calls matching a numeric input string and returns grouped call data.

    This endpoint performs the following:
    - Validates that the input `text` parameter is a numeric string (with optional leading `+`).
    - Filters `Call` records where the input matches either the `from_number` (for incoming calls)
    or `to_number` (for outgoing calls), excluding in-app calls.
    - Groups matching calls by phone number, annotating:
        - The total number of calls (`count`)
        - The timestamp of the most recent call (`last_activity`)
        - The most recent `Call` object (`latest_call`) for detailed info
    - Returns a paginated response where each entry contains:
        - `number`: The phone number associated with the call group
        - `count`: Total calls for that number
        - `last_activity`: Timestamp of the most recent call
        - `latest_call`: Serialized data from the most recent matching `Call`

    Returns:
        400 Bad Request if the input text is not a valid number.
        200 OK with a paginated list of grouped call search results.

    Args:
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        text (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[InvalidCallSearchResponse, PaginatedCallSearchResponseList]]
    """

    kwargs = _get_kwargs(
        client=client,
        limit=limit,
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
    offset: Union[Unset, None, int] = UNSET,
    text: str,
) -> Optional[Union[InvalidCallSearchResponse, PaginatedCallSearchResponseList]]:
    """Searches for calls matching a numeric input string and returns grouped call data.

    This endpoint performs the following:
    - Validates that the input `text` parameter is a numeric string (with optional leading `+`).
    - Filters `Call` records where the input matches either the `from_number` (for incoming calls)
    or `to_number` (for outgoing calls), excluding in-app calls.
    - Groups matching calls by phone number, annotating:
        - The total number of calls (`count`)
        - The timestamp of the most recent call (`last_activity`)
        - The most recent `Call` object (`latest_call`) for detailed info
    - Returns a paginated response where each entry contains:
        - `number`: The phone number associated with the call group
        - `count`: Total calls for that number
        - `last_activity`: Timestamp of the most recent call
        - `latest_call`: Serialized data from the most recent matching `Call`

    Returns:
        400 Bad Request if the input text is not a valid number.
        200 OK with a paginated list of grouped call search results.

    Args:
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        text (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[InvalidCallSearchResponse, PaginatedCallSearchResponseList]]
    """

    return sync_detailed(
        client=client,
        limit=limit,
        offset=offset,
        text=text,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    text: str,
) -> Response[Union[InvalidCallSearchResponse, PaginatedCallSearchResponseList]]:
    """Searches for calls matching a numeric input string and returns grouped call data.

    This endpoint performs the following:
    - Validates that the input `text` parameter is a numeric string (with optional leading `+`).
    - Filters `Call` records where the input matches either the `from_number` (for incoming calls)
    or `to_number` (for outgoing calls), excluding in-app calls.
    - Groups matching calls by phone number, annotating:
        - The total number of calls (`count`)
        - The timestamp of the most recent call (`last_activity`)
        - The most recent `Call` object (`latest_call`) for detailed info
    - Returns a paginated response where each entry contains:
        - `number`: The phone number associated with the call group
        - `count`: Total calls for that number
        - `last_activity`: Timestamp of the most recent call
        - `latest_call`: Serialized data from the most recent matching `Call`

    Returns:
        400 Bad Request if the input text is not a valid number.
        200 OK with a paginated list of grouped call search results.

    Args:
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        text (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[InvalidCallSearchResponse, PaginatedCallSearchResponseList]]
    """

    kwargs = _get_kwargs(
        client=client,
        limit=limit,
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
    offset: Union[Unset, None, int] = UNSET,
    text: str,
) -> Optional[Union[InvalidCallSearchResponse, PaginatedCallSearchResponseList]]:
    """Searches for calls matching a numeric input string and returns grouped call data.

    This endpoint performs the following:
    - Validates that the input `text` parameter is a numeric string (with optional leading `+`).
    - Filters `Call` records where the input matches either the `from_number` (for incoming calls)
    or `to_number` (for outgoing calls), excluding in-app calls.
    - Groups matching calls by phone number, annotating:
        - The total number of calls (`count`)
        - The timestamp of the most recent call (`last_activity`)
        - The most recent `Call` object (`latest_call`) for detailed info
    - Returns a paginated response where each entry contains:
        - `number`: The phone number associated with the call group
        - `count`: Total calls for that number
        - `last_activity`: Timestamp of the most recent call
        - `latest_call`: Serialized data from the most recent matching `Call`

    Returns:
        400 Bad Request if the input text is not a valid number.
        200 OK with a paginated list of grouped call search results.

    Args:
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        text (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[InvalidCallSearchResponse, PaginatedCallSearchResponseList]]
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            offset=offset,
            text=text,
        )
    ).parsed
