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
from ...models.ivr_menu_response import IVRMenuResponse
from ...models.v1_ivr_retrieve_duration import V1IvrRetrieveDuration
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    client: AuthenticatedClient,
    duration: Union[
        Unset, None, V1IvrRetrieveDuration
    ] = V1IvrRetrieveDuration.ONE_WEEK,
) -> Dict[str, Any]:
    url = "{}/v1/ivr/{id}/".format(client.base_url, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_duration: Union[Unset, None, str] = UNSET
    if not isinstance(duration, Unset):
        json_duration = duration.value if duration else None

    params["duration"] = json_duration

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
) -> Optional[IVRMenuResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = IVRMenuResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[IVRMenuResponse]:
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
    duration: Union[
        Unset, None, V1IvrRetrieveDuration
    ] = V1IvrRetrieveDuration.ONE_WEEK,
) -> Response[IVRMenuResponse]:
    """API view set for IVR Menu model.

    Args:
        id (int):
        duration (Union[Unset, None, V1IvrRetrieveDuration]):  Default:
            V1IvrRetrieveDuration.ONE_WEEK.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IVRMenuResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        duration=duration,
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
    duration: Union[
        Unset, None, V1IvrRetrieveDuration
    ] = V1IvrRetrieveDuration.ONE_WEEK,
) -> Optional[IVRMenuResponse]:
    """API view set for IVR Menu model.

    Args:
        id (int):
        duration (Union[Unset, None, V1IvrRetrieveDuration]):  Default:
            V1IvrRetrieveDuration.ONE_WEEK.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IVRMenuResponse]
    """

    return sync_detailed(
        id=id,
        client=client,
        duration=duration,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    duration: Union[
        Unset, None, V1IvrRetrieveDuration
    ] = V1IvrRetrieveDuration.ONE_WEEK,
) -> Response[IVRMenuResponse]:
    """API view set for IVR Menu model.

    Args:
        id (int):
        duration (Union[Unset, None, V1IvrRetrieveDuration]):  Default:
            V1IvrRetrieveDuration.ONE_WEEK.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IVRMenuResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        duration=duration,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    duration: Union[
        Unset, None, V1IvrRetrieveDuration
    ] = V1IvrRetrieveDuration.ONE_WEEK,
) -> Optional[IVRMenuResponse]:
    """API view set for IVR Menu model.

    Args:
        id (int):
        duration (Union[Unset, None, V1IvrRetrieveDuration]):  Default:
            V1IvrRetrieveDuration.ONE_WEEK.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IVRMenuResponse]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            duration=duration,
        )
    ).parsed
