"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.call_dtmf_request_request import CallDtmfRequestRequest
from ...types import Response


def _get_kwargs(
    id: int,
    *,
    client: AuthenticatedClient,
    json_body: CallDtmfRequestRequest,
) -> Dict[str, Any]:
    url = "{}/v1/calls/{id}/dtmf/".format(client.base_url, id=id)

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.OK:
        return None
    if response.status_code == HTTPStatus.BAD_REQUEST:
        return None
    if response.status_code == HTTPStatus.NOT_FOUND:
        return None
    if response.status_code == HTTPStatus.BAD_GATEWAY:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Any]:
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
    json_body: CallDtmfRequestRequest,
) -> Response[Any]:
    """Send DTMF digits into an active call (F-193 B1, KaptureCX ask).

    F-194: an API call to SIP keyed by the leg's channel id — NOT a
    message to the call's stream.py consumer (that signaling is closed
    after an AI handoff, exactly when Kapture drives the call).

    Args:
        id (int):
        json_body (CallDtmfRequestRequest): F-193 B1: DTMF digits to send INTO an active call (ARI
            alphabet).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    json_body: CallDtmfRequestRequest,
) -> Response[Any]:
    """Send DTMF digits into an active call (F-193 B1, KaptureCX ask).

    F-194: an API call to SIP keyed by the leg's channel id — NOT a
    message to the call's stream.py consumer (that signaling is closed
    after an AI handoff, exactly when Kapture drives the call).

    Args:
        id (int):
        json_body (CallDtmfRequestRequest): F-193 B1: DTMF digits to send INTO an active call (ARI
            alphabet).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)
