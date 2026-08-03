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
from ...models.v1_calls_metadata_create_json_body import V1CallsMetadataCreateJsonBody
from ...models.v1_calls_metadata_create_response_200 import (
    V1CallsMetadataCreateResponse200,
)
from ...types import Response


def _get_kwargs(
    call_id: str,
    *,
    client: AuthenticatedClient,
    json_body: V1CallsMetadataCreateJsonBody,
) -> Dict[str, Any]:
    url = "{}/v1/calls/{call_id}/metadata/".format(client.base_url, call_id=call_id)

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
) -> Optional[Union[Any, V1CallsMetadataCreateResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = V1CallsMetadataCreateResponse200.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[Any, V1CallsMetadataCreateResponse200]]:
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
    json_body: V1CallsMetadataCreateJsonBody,
) -> Response[Union[Any, V1CallsMetadataCreateResponse200]]:
    """MERGE the request body into the call's metadata.

    POST-as-merge (not PATCH) keeps the router mount identical to
    the sibling `calls/<id>/tags/` collection. Idempotent: re-posting
    the same payload is a no-op-equivalent overwrite.

    Args:
        call_id (str):
        json_body (V1CallsMetadataCreateJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, V1CallsMetadataCreateResponse200]]
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
    json_body: V1CallsMetadataCreateJsonBody,
) -> Optional[Union[Any, V1CallsMetadataCreateResponse200]]:
    """MERGE the request body into the call's metadata.

    POST-as-merge (not PATCH) keeps the router mount identical to
    the sibling `calls/<id>/tags/` collection. Idempotent: re-posting
    the same payload is a no-op-equivalent overwrite.

    Args:
        call_id (str):
        json_body (V1CallsMetadataCreateJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, V1CallsMetadataCreateResponse200]]
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
    json_body: V1CallsMetadataCreateJsonBody,
) -> Response[Union[Any, V1CallsMetadataCreateResponse200]]:
    """MERGE the request body into the call's metadata.

    POST-as-merge (not PATCH) keeps the router mount identical to
    the sibling `calls/<id>/tags/` collection. Idempotent: re-posting
    the same payload is a no-op-equivalent overwrite.

    Args:
        call_id (str):
        json_body (V1CallsMetadataCreateJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, V1CallsMetadataCreateResponse200]]
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
    json_body: V1CallsMetadataCreateJsonBody,
) -> Optional[Union[Any, V1CallsMetadataCreateResponse200]]:
    """MERGE the request body into the call's metadata.

    POST-as-merge (not PATCH) keeps the router mount identical to
    the sibling `calls/<id>/tags/` collection. Idempotent: re-posting
    the same payload is a no-op-equivalent overwrite.

    Args:
        call_id (str):
        json_body (V1CallsMetadataCreateJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, V1CallsMetadataCreateResponse200]]
    """

    return (
        await asyncio_detailed(
            call_id=call_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
