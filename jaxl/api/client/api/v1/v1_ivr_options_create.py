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
from ...models.ivr_options_invalid_response import IVROptionsInvalidResponse
from ...models.ivr_options_request import IVROptionsRequest
from ...models.ivr_options_response import IVROptionsResponse
from ...types import Response


def _get_kwargs(
    menu_id: int,
    *,
    client: AuthenticatedClient,
    json_body: IVROptionsRequest,
) -> Dict[str, Any]:
    url = "{}/v1/ivr/{menu_id}/options/".format(client.base_url, menu_id=menu_id)

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
) -> Optional[Union[Any, IVROptionsInvalidResponse, IVROptionsResponse]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = IVROptionsResponse.from_dict(response.json())

        return response_201
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.CONFLICT:
        response_409 = cast(Any, None)
        return response_409
    if response.status_code == HTTPStatus.NOT_ACCEPTABLE:
        response_406 = IVROptionsInvalidResponse.from_dict(response.json())

        return response_406
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[Any, IVROptionsInvalidResponse, IVROptionsResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    menu_id: int,
    *,
    client: AuthenticatedClient,
    json_body: IVROptionsRequest,
) -> Response[Union[Any, IVROptionsInvalidResponse, IVROptionsResponse]]:
    """API view set for IVR Options model.

    Args:
        menu_id (int):
        json_body (IVROptionsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, IVROptionsInvalidResponse, IVROptionsResponse]]
    """

    kwargs = _get_kwargs(
        menu_id=menu_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    menu_id: int,
    *,
    client: AuthenticatedClient,
    json_body: IVROptionsRequest,
) -> Optional[Union[Any, IVROptionsInvalidResponse, IVROptionsResponse]]:
    """API view set for IVR Options model.

    Args:
        menu_id (int):
        json_body (IVROptionsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, IVROptionsInvalidResponse, IVROptionsResponse]]
    """

    return sync_detailed(
        menu_id=menu_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    menu_id: int,
    *,
    client: AuthenticatedClient,
    json_body: IVROptionsRequest,
) -> Response[Union[Any, IVROptionsInvalidResponse, IVROptionsResponse]]:
    """API view set for IVR Options model.

    Args:
        menu_id (int):
        json_body (IVROptionsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, IVROptionsInvalidResponse, IVROptionsResponse]]
    """

    kwargs = _get_kwargs(
        menu_id=menu_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    menu_id: int,
    *,
    client: AuthenticatedClient,
    json_body: IVROptionsRequest,
) -> Optional[Union[Any, IVROptionsInvalidResponse, IVROptionsResponse]]:
    """API view set for IVR Options model.

    Args:
        menu_id (int):
        json_body (IVROptionsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, IVROptionsInvalidResponse, IVROptionsResponse]]
    """

    return (
        await asyncio_detailed(
            menu_id=menu_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
