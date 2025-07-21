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
from ...models.order_attributes import OrderAttributes
from ...models.patched_order_attributes_request import (
    PatchedOrderAttributesRequest,
)
from ...types import UNSET, Response


def _get_kwargs(
    id: int,
    *,
    client: AuthenticatedClient,
    json_body: PatchedOrderAttributesRequest,
    sku: str,
) -> Dict[str, Any]:
    url = "{}/v1/orders/{id}/attributes/".format(client.base_url, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["sku"] = sku

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "patch",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[OrderAttributes]:
    if response.status_code == HTTPStatus.OK:
        response_200 = OrderAttributes.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[OrderAttributes]:
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
    json_body: PatchedOrderAttributesRequest,
    sku: str,
) -> Response[OrderAttributes]:
    """
    Args:
        id (int):
        sku (str):
        json_body (PatchedOrderAttributesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrderAttributes]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        json_body=json_body,
        sku=sku,
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
    json_body: PatchedOrderAttributesRequest,
    sku: str,
) -> Optional[OrderAttributes]:
    """
    Args:
        id (int):
        sku (str):
        json_body (PatchedOrderAttributesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrderAttributes]
    """

    return sync_detailed(
        id=id,
        client=client,
        json_body=json_body,
        sku=sku,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    json_body: PatchedOrderAttributesRequest,
    sku: str,
) -> Response[OrderAttributes]:
    """
    Args:
        id (int):
        sku (str):
        json_body (PatchedOrderAttributesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrderAttributes]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        json_body=json_body,
        sku=sku,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    json_body: PatchedOrderAttributesRequest,
    sku: str,
) -> Optional[OrderAttributes]:
    """
    Args:
        id (int):
        sku (str):
        json_body (PatchedOrderAttributesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrderAttributes]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            json_body=json_body,
            sku=sku,
        )
    ).parsed
