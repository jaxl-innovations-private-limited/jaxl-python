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
from ...models.call_schedule_request import CallScheduleRequest
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: CallScheduleRequest,
) -> Dict[str, Any]:
    url = "{}/v1/calls/schedule/".format(client.base_url)

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
    if response.status_code == HTTPStatus.CREATED:
        response_201 = Call.from_dict(response.json())

        return response_201
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
    *,
    client: AuthenticatedClient,
    json_body: CallScheduleRequest,
) -> Response[Call]:
    """F-167a K-1b — schedule a standalone outbound call for a future
    time. Rides the F-85 lifecycle (same row shape, same placement
    task with its balance/from-ownership gates, same cancel path) —
    no prior call or tag needed.

    Args:
        json_body (CallScheduleRequest): F-167a K-1b — `POST /v1/calls/schedule/`: schedule a
            standalone
            outbound call for a future time (no prior call / tag needed).
            E.164 numbers; `run_at` ISO-8601 with timezone; `ivr_id` decides what
            the callee lands in on answer (required — same rule as calls create).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Call]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    json_body: CallScheduleRequest,
) -> Optional[Call]:
    """F-167a K-1b — schedule a standalone outbound call for a future
    time. Rides the F-85 lifecycle (same row shape, same placement
    task with its balance/from-ownership gates, same cancel path) —
    no prior call or tag needed.

    Args:
        json_body (CallScheduleRequest): F-167a K-1b — `POST /v1/calls/schedule/`: schedule a
            standalone
            outbound call for a future time (no prior call / tag needed).
            E.164 numbers; `run_at` ISO-8601 with timezone; `ivr_id` decides what
            the callee lands in on answer (required — same rule as calls create).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Call]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: CallScheduleRequest,
) -> Response[Call]:
    """F-167a K-1b — schedule a standalone outbound call for a future
    time. Rides the F-85 lifecycle (same row shape, same placement
    task with its balance/from-ownership gates, same cancel path) —
    no prior call or tag needed.

    Args:
        json_body (CallScheduleRequest): F-167a K-1b — `POST /v1/calls/schedule/`: schedule a
            standalone
            outbound call for a future time (no prior call / tag needed).
            E.164 numbers; `run_at` ISO-8601 with timezone; `ivr_id` decides what
            the callee lands in on answer (required — same rule as calls create).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Call]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    json_body: CallScheduleRequest,
) -> Optional[Call]:
    """F-167a K-1b — schedule a standalone outbound call for a future
    time. Rides the F-85 lifecycle (same row shape, same placement
    task with its balance/from-ownership gates, same cancel path) —
    no prior call or tag needed.

    Args:
        json_body (CallScheduleRequest): F-167a K-1b — `POST /v1/calls/schedule/`: schedule a
            standalone
            outbound call for a future time (no prior call / tag needed).
            E.164 numbers; `run_at` ISO-8601 with timezone; `ivr_id` decides what
            the callee lands in on answer (required — same rule as calls create).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Call]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
