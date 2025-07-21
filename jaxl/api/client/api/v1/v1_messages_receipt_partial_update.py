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
from ...models.dh_public_key_read_receipt_response import (
    DHPublicKeyReadReceiptResponse,
)
from ...models.patched_dh_public_key_read_receipt_request import (
    PatchedDHPublicKeyReadReceiptRequest,
)
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: PatchedDHPublicKeyReadReceiptRequest,
) -> Dict[str, Any]:
    url = "{}/v1/messages/receipt/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "patch",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[Any, DHPublicKeyReadReceiptResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = DHPublicKeyReadReceiptResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.PRECONDITION_FAILED:
        response_412 = cast(Any, None)
        return response_412
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[Any, DHPublicKeyReadReceiptResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: PatchedDHPublicKeyReadReceiptRequest,
) -> Response[Union[Any, DHPublicKeyReadReceiptResponse]]:
    """Only other party can send read receipts.

    Args:
        json_body (PatchedDHPublicKeyReadReceiptRequest): Read receipts are sent for the last PK
            that user device has seen/read.

            NOTE: "to_key" is acknowledging read receipt for all messages until primary key "till"
            received "from_key" user.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DHPublicKeyReadReceiptResponse]]
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
    json_body: PatchedDHPublicKeyReadReceiptRequest,
) -> Optional[Union[Any, DHPublicKeyReadReceiptResponse]]:
    """Only other party can send read receipts.

    Args:
        json_body (PatchedDHPublicKeyReadReceiptRequest): Read receipts are sent for the last PK
            that user device has seen/read.

            NOTE: "to_key" is acknowledging read receipt for all messages until primary key "till"
            received "from_key" user.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DHPublicKeyReadReceiptResponse]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: PatchedDHPublicKeyReadReceiptRequest,
) -> Response[Union[Any, DHPublicKeyReadReceiptResponse]]:
    """Only other party can send read receipts.

    Args:
        json_body (PatchedDHPublicKeyReadReceiptRequest): Read receipts are sent for the last PK
            that user device has seen/read.

            NOTE: "to_key" is acknowledging read receipt for all messages until primary key "till"
            received "from_key" user.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DHPublicKeyReadReceiptResponse]]
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
    json_body: PatchedDHPublicKeyReadReceiptRequest,
) -> Optional[Union[Any, DHPublicKeyReadReceiptResponse]]:
    """Only other party can send read receipts.

    Args:
        json_body (PatchedDHPublicKeyReadReceiptRequest): Read receipts are sent for the last PK
            that user device has seen/read.

            NOTE: "to_key" is acknowledging read receipt for all messages until primary key "till"
            received "from_key" user.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DHPublicKeyReadReceiptResponse]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
