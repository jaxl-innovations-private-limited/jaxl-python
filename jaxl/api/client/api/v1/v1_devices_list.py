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
from ...models.paginated_device_list import PaginatedDeviceList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    employee_id: Union[Unset, None, int] = UNSET,
    is_sdds: Union[Unset, None, bool] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/v1/devices/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["employee_id"] = employee_id

    params["is_sdds"] = is_sdds

    params["limit"] = limit

    params["offset"] = offset

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
) -> Optional[PaginatedDeviceList]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PaginatedDeviceList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[PaginatedDeviceList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    employee_id: Union[Unset, None, int] = UNSET,
    is_sdds: Union[Unset, None, bool] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
) -> Response[PaginatedDeviceList]:
    """API view set for Device models.

    Args:
        employee_id (Union[Unset, None, int]):
        is_sdds (Union[Unset, None, bool]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedDeviceList]
    """

    kwargs = _get_kwargs(
        client=client,
        employee_id=employee_id,
        is_sdds=is_sdds,
        limit=limit,
        offset=offset,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    employee_id: Union[Unset, None, int] = UNSET,
    is_sdds: Union[Unset, None, bool] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
) -> Optional[PaginatedDeviceList]:
    """API view set for Device models.

    Args:
        employee_id (Union[Unset, None, int]):
        is_sdds (Union[Unset, None, bool]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedDeviceList]
    """

    return sync_detailed(
        client=client,
        employee_id=employee_id,
        is_sdds=is_sdds,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    employee_id: Union[Unset, None, int] = UNSET,
    is_sdds: Union[Unset, None, bool] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
) -> Response[PaginatedDeviceList]:
    """API view set for Device models.

    Args:
        employee_id (Union[Unset, None, int]):
        is_sdds (Union[Unset, None, bool]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedDeviceList]
    """

    kwargs = _get_kwargs(
        client=client,
        employee_id=employee_id,
        is_sdds=is_sdds,
        limit=limit,
        offset=offset,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    employee_id: Union[Unset, None, int] = UNSET,
    is_sdds: Union[Unset, None, bool] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
) -> Optional[PaginatedDeviceList]:
    """API view set for Device models.

    Args:
        employee_id (Union[Unset, None, int]):
        is_sdds (Union[Unset, None, bool]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedDeviceList]
    """

    return (
        await asyncio_detailed(
            client=client,
            employee_id=employee_id,
            is_sdds=is_sdds,
            limit=limit,
            offset=offset,
        )
    ).parsed
