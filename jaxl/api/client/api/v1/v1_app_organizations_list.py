"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_organization_list import PaginatedOrganizationList
from ...models.v1_app_organizations_list_status_item import (
    V1AppOrganizationsListStatusItem,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    status: Union[Unset, None, List[V1AppOrganizationsListStatusItem]] = UNSET,
) -> Dict[str, Any]:
    url = "{}/v1/app/organizations/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["limit"] = limit

    params["offset"] = offset

    json_status: Union[Unset, None, List[str]] = UNSET
    if not isinstance(status, Unset):
        if status is None:
            json_status = None
        else:
            json_status = []
            for status_item_data in status:
                status_item = status_item_data.value

                json_status.append(status_item)

    params["status"] = json_status

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
) -> Optional[PaginatedOrganizationList]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PaginatedOrganizationList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[PaginatedOrganizationList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    status: Union[Unset, None, List[V1AppOrganizationsListStatusItem]] = UNSET,
) -> Response[PaginatedOrganizationList]:
    """API view set for App organization model.

    Args:
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        status (Union[Unset, None, List[V1AppOrganizationsListStatusItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedOrganizationList]
    """

    kwargs = _get_kwargs(
        client=client,
        limit=limit,
        offset=offset,
        status=status,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    status: Union[Unset, None, List[V1AppOrganizationsListStatusItem]] = UNSET,
) -> Optional[PaginatedOrganizationList]:
    """API view set for App organization model.

    Args:
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        status (Union[Unset, None, List[V1AppOrganizationsListStatusItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedOrganizationList]
    """

    return sync_detailed(
        client=client,
        limit=limit,
        offset=offset,
        status=status,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    status: Union[Unset, None, List[V1AppOrganizationsListStatusItem]] = UNSET,
) -> Response[PaginatedOrganizationList]:
    """API view set for App organization model.

    Args:
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        status (Union[Unset, None, List[V1AppOrganizationsListStatusItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedOrganizationList]
    """

    kwargs = _get_kwargs(
        client=client,
        limit=limit,
        offset=offset,
        status=status,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    status: Union[Unset, None, List[V1AppOrganizationsListStatusItem]] = UNSET,
) -> Optional[PaginatedOrganizationList]:
    """API view set for App organization model.

    Args:
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        status (Union[Unset, None, List[V1AppOrganizationsListStatusItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedOrganizationList]
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            offset=offset,
            status=status,
        )
    ).parsed
