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
from ...models.paginated_organization_employee_list import (
    PaginatedOrganizationEmployeeList,
)
from ...models.v2_app_organizations_employees_list_status_item import (
    V2AppOrganizationsEmployeesListStatusItem,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    org_id: str,
    *,
    client: AuthenticatedClient,
    email_hash: Union[Unset, None, List[str]] = UNSET,
    group_id: Union[Unset, None, List[int]] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    status: Union[Unset, None, List[V2AppOrganizationsEmployeesListStatusItem]] = UNSET,
) -> Dict[str, Any]:
    url = "{}/v2/app/organizations/{org_id}/employees/".format(
        client.base_url, org_id=org_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_email_hash: Union[Unset, None, List[str]] = UNSET
    if not isinstance(email_hash, Unset):
        if email_hash is None:
            json_email_hash = None
        else:
            json_email_hash = email_hash

    params["email_hash"] = json_email_hash

    json_group_id: Union[Unset, None, List[int]] = UNSET
    if not isinstance(group_id, Unset):
        if group_id is None:
            json_group_id = None
        else:
            json_group_id = group_id

    params["group_id"] = json_group_id

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
) -> Optional[PaginatedOrganizationEmployeeList]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PaginatedOrganizationEmployeeList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[PaginatedOrganizationEmployeeList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    org_id: str,
    *,
    client: AuthenticatedClient,
    email_hash: Union[Unset, None, List[str]] = UNSET,
    group_id: Union[Unset, None, List[int]] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    status: Union[Unset, None, List[V2AppOrganizationsEmployeesListStatusItem]] = UNSET,
) -> Response[PaginatedOrganizationEmployeeList]:
    """API view set for App organization model.

    Args:
        org_id (str):
        email_hash (Union[Unset, None, List[str]]):
        group_id (Union[Unset, None, List[int]]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        status (Union[Unset, None, List[V2AppOrganizationsEmployeesListStatusItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedOrganizationEmployeeList]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
        client=client,
        email_hash=email_hash,
        group_id=group_id,
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
    org_id: str,
    *,
    client: AuthenticatedClient,
    email_hash: Union[Unset, None, List[str]] = UNSET,
    group_id: Union[Unset, None, List[int]] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    status: Union[Unset, None, List[V2AppOrganizationsEmployeesListStatusItem]] = UNSET,
) -> Optional[PaginatedOrganizationEmployeeList]:
    """API view set for App organization model.

    Args:
        org_id (str):
        email_hash (Union[Unset, None, List[str]]):
        group_id (Union[Unset, None, List[int]]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        status (Union[Unset, None, List[V2AppOrganizationsEmployeesListStatusItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedOrganizationEmployeeList]
    """

    return sync_detailed(
        org_id=org_id,
        client=client,
        email_hash=email_hash,
        group_id=group_id,
        limit=limit,
        offset=offset,
        status=status,
    ).parsed


async def asyncio_detailed(
    org_id: str,
    *,
    client: AuthenticatedClient,
    email_hash: Union[Unset, None, List[str]] = UNSET,
    group_id: Union[Unset, None, List[int]] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    status: Union[Unset, None, List[V2AppOrganizationsEmployeesListStatusItem]] = UNSET,
) -> Response[PaginatedOrganizationEmployeeList]:
    """API view set for App organization model.

    Args:
        org_id (str):
        email_hash (Union[Unset, None, List[str]]):
        group_id (Union[Unset, None, List[int]]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        status (Union[Unset, None, List[V2AppOrganizationsEmployeesListStatusItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedOrganizationEmployeeList]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
        client=client,
        email_hash=email_hash,
        group_id=group_id,
        limit=limit,
        offset=offset,
        status=status,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    org_id: str,
    *,
    client: AuthenticatedClient,
    email_hash: Union[Unset, None, List[str]] = UNSET,
    group_id: Union[Unset, None, List[int]] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    status: Union[Unset, None, List[V2AppOrganizationsEmployeesListStatusItem]] = UNSET,
) -> Optional[PaginatedOrganizationEmployeeList]:
    """API view set for App organization model.

    Args:
        org_id (str):
        email_hash (Union[Unset, None, List[str]]):
        group_id (Union[Unset, None, List[int]]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        status (Union[Unset, None, List[V2AppOrganizationsEmployeesListStatusItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedOrganizationEmployeeList]
    """

    return (
        await asyncio_detailed(
            org_id=org_id,
            client=client,
            email_hash=email_hash,
            group_id=group_id,
            limit=limit,
            offset=offset,
            status=status,
        )
    ).parsed
