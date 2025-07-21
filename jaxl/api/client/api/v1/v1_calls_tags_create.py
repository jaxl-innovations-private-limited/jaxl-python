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
from ...models.call_tag_request import CallTagRequest
from ...models.call_tag_response import CallTagResponse
from ...types import Response


def _get_kwargs(
    call_id: str,
    *,
    client: AuthenticatedClient,
    json_body: CallTagRequest,
) -> Dict[str, Any]:
    url = "{}/v1/calls/{call_id}/tags/".format(client.base_url, call_id=call_id)

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


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[Any, CallTagResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CallTagResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.PRECONDITION_FAILED:
        response_412 = cast(Any, None)
        return response_412
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[Any, CallTagResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    call_id: str,
    *,
    client: AuthenticatedClient,
    json_body: CallTagRequest,
) -> Response[Union[Any, CallTagResponse]]:
    """Create call tag

    Args:
        call_id (str):
        json_body (CallTagRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CallTagResponse]]
    """

    kwargs = _get_kwargs(
        call_id=call_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    call_id: str,
    *,
    client: AuthenticatedClient,
    json_body: CallTagRequest,
) -> Optional[Union[Any, CallTagResponse]]:
    """Create call tag

    Args:
        call_id (str):
        json_body (CallTagRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CallTagResponse]]
    """

    return sync_detailed(
        call_id=call_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    call_id: str,
    *,
    client: AuthenticatedClient,
    json_body: CallTagRequest,
) -> Response[Union[Any, CallTagResponse]]:
    """Create call tag

    Args:
        call_id (str):
        json_body (CallTagRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CallTagResponse]]
    """

    kwargs = _get_kwargs(
        call_id=call_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    call_id: str,
    *,
    client: AuthenticatedClient,
    json_body: CallTagRequest,
) -> Optional[Union[Any, CallTagResponse]]:
    """Create call tag

    Args:
        call_id (str):
        json_body (CallTagRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CallTagResponse]]
    """

    return (
        await asyncio_detailed(
            call_id=call_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
