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
from ...models.transcription_download_response import (
    TranscriptionDownloadResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    call_id: int,
    transcription_id: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/v1/transcription/url/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["call_id"] = call_id

    params["transcription_id"] = transcription_id

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
) -> Optional[TranscriptionDownloadResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = TranscriptionDownloadResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[TranscriptionDownloadResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    call_id: int,
    transcription_id: Union[Unset, None, int] = UNSET,
) -> Response[TranscriptionDownloadResponse]:
    """Fetch the latest transcription for this call.

    Args:
        call_id (int):
        transcription_id (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TranscriptionDownloadResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        call_id=call_id,
        transcription_id=transcription_id,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    call_id: int,
    transcription_id: Union[Unset, None, int] = UNSET,
) -> Optional[TranscriptionDownloadResponse]:
    """Fetch the latest transcription for this call.

    Args:
        call_id (int):
        transcription_id (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TranscriptionDownloadResponse]
    """

    return sync_detailed(
        client=client,
        call_id=call_id,
        transcription_id=transcription_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    call_id: int,
    transcription_id: Union[Unset, None, int] = UNSET,
) -> Response[TranscriptionDownloadResponse]:
    """Fetch the latest transcription for this call.

    Args:
        call_id (int):
        transcription_id (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TranscriptionDownloadResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        call_id=call_id,
        transcription_id=transcription_id,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    call_id: int,
    transcription_id: Union[Unset, None, int] = UNSET,
) -> Optional[TranscriptionDownloadResponse]:
    """Fetch the latest transcription for this call.

    Args:
        call_id (int):
        transcription_id (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TranscriptionDownloadResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            call_id=call_id,
            transcription_id=transcription_id,
        )
    ).parsed
