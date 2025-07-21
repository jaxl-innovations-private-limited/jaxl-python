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
from ...models.paginated_transcription_search_response_serializer_v2_list import (
    PaginatedTranscriptionSearchResponseSerializerV2List,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, None, int] = UNSET,
    limit_per_transcription: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    text: str,
    transcription_limit: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/v2/transcription/search/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["limit"] = limit

    params["limit_per_transcription"] = limit_per_transcription

    params["offset"] = offset

    params["text"] = text

    params["transcription_limit"] = transcription_limit

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
) -> Optional[PaginatedTranscriptionSearchResponseSerializerV2List]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PaginatedTranscriptionSearchResponseSerializerV2List.from_dict(
            response.json()
        )

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[PaginatedTranscriptionSearchResponseSerializerV2List]:
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
    limit_per_transcription: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    text: str,
    transcription_limit: Union[Unset, None, int] = UNSET,
) -> Response[PaginatedTranscriptionSearchResponseSerializerV2List]:
    """
    Args:
        limit (Union[Unset, None, int]):
        limit_per_transcription (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        text (str):
        transcription_limit (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedTranscriptionSearchResponseSerializerV2List]
    """

    kwargs = _get_kwargs(
        client=client,
        limit=limit,
        limit_per_transcription=limit_per_transcription,
        offset=offset,
        text=text,
        transcription_limit=transcription_limit,
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
    limit_per_transcription: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    text: str,
    transcription_limit: Union[Unset, None, int] = UNSET,
) -> Optional[PaginatedTranscriptionSearchResponseSerializerV2List]:
    """
    Args:
        limit (Union[Unset, None, int]):
        limit_per_transcription (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        text (str):
        transcription_limit (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedTranscriptionSearchResponseSerializerV2List]
    """

    return sync_detailed(
        client=client,
        limit=limit,
        limit_per_transcription=limit_per_transcription,
        offset=offset,
        text=text,
        transcription_limit=transcription_limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, None, int] = UNSET,
    limit_per_transcription: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    text: str,
    transcription_limit: Union[Unset, None, int] = UNSET,
) -> Response[PaginatedTranscriptionSearchResponseSerializerV2List]:
    """
    Args:
        limit (Union[Unset, None, int]):
        limit_per_transcription (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        text (str):
        transcription_limit (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedTranscriptionSearchResponseSerializerV2List]
    """

    kwargs = _get_kwargs(
        client=client,
        limit=limit,
        limit_per_transcription=limit_per_transcription,
        offset=offset,
        text=text,
        transcription_limit=transcription_limit,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, None, int] = UNSET,
    limit_per_transcription: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    text: str,
    transcription_limit: Union[Unset, None, int] = UNSET,
) -> Optional[PaginatedTranscriptionSearchResponseSerializerV2List]:
    """
    Args:
        limit (Union[Unset, None, int]):
        limit_per_transcription (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        text (str):
        transcription_limit (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedTranscriptionSearchResponseSerializerV2List]
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            limit_per_transcription=limit_per_transcription,
            offset=offset,
            text=text,
            transcription_limit=transcription_limit,
        )
    ).parsed
