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
from ...models.call import Call
from ...models.call_reschedule_request import CallRescheduleRequest
from ...types import Response


def _get_kwargs(
    id: int,
    *,
    client: AuthenticatedClient,
    json_body: CallRescheduleRequest,
) -> Dict[str, Any]:
    url = "{}/v1/calls/{id}/schedule/".format(client.base_url, id=id)

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Call]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Call.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Call]:
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
    json_body: CallRescheduleRequest,
) -> Response[Call]:
    """F-167a K-1b — POST = move a still-pending scheduled call to a
    new run_at (evict + re-schedule); DELETE = cancel it. Both 409 on
    a call that already placed/cancelled — the caller learns the truth
    instead of a silent no-op.

    Args:
        id (int):
        json_body (CallRescheduleRequest): F-167a K-1b — `POST /v1/calls/<id>/schedule/`: move a
            still-pending
            scheduled call to a new `run_at`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Call]
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


def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    json_body: CallRescheduleRequest,
) -> Optional[Call]:
    """F-167a K-1b — POST = move a still-pending scheduled call to a
    new run_at (evict + re-schedule); DELETE = cancel it. Both 409 on
    a call that already placed/cancelled — the caller learns the truth
    instead of a silent no-op.

    Args:
        id (int):
        json_body (CallRescheduleRequest): F-167a K-1b — `POST /v1/calls/<id>/schedule/`: move a
            still-pending
            scheduled call to a new `run_at`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Call]
    """

    return sync_detailed(
        id=id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    json_body: CallRescheduleRequest,
) -> Response[Call]:
    """F-167a K-1b — POST = move a still-pending scheduled call to a
    new run_at (evict + re-schedule); DELETE = cancel it. Both 409 on
    a call that already placed/cancelled — the caller learns the truth
    instead of a silent no-op.

    Args:
        id (int):
        json_body (CallRescheduleRequest): F-167a K-1b — `POST /v1/calls/<id>/schedule/`: move a
            still-pending
            scheduled call to a new `run_at`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Call]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    json_body: CallRescheduleRequest,
) -> Optional[Call]:
    """F-167a K-1b — POST = move a still-pending scheduled call to a
    new run_at (evict + re-schedule); DELETE = cancel it. Both 409 on
    a call that already placed/cancelled — the caller learns the truth
    instead of a silent no-op.

    Args:
        id (int):
        json_body (CallRescheduleRequest): F-167a K-1b — `POST /v1/calls/<id>/schedule/`: move a
            still-pending
            scheduled call to a new `run_at`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Call]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            json_body=json_body,
        )
    ).parsed
