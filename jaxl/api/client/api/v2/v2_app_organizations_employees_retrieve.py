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
from ...models.organization_employee import OrganizationEmployee
from ...types import Response


def _get_kwargs(
    org_id: str,
    id: int,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/v2/app/organizations/{org_id}/employees/{id}/".format(
        client.base_url, org_id=org_id, id=id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[Any, OrganizationEmployee]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = OrganizationEmployee.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[Any, OrganizationEmployee]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    org_id: str,
    id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, OrganizationEmployee]]:
    """API view set for App organization model.

    Args:
        org_id (str):
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, OrganizationEmployee]]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
        id=id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    org_id: str,
    id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, OrganizationEmployee]]:
    """API view set for App organization model.

    Args:
        org_id (str):
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, OrganizationEmployee]]
    """

    return sync_detailed(
        org_id=org_id,
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    org_id: str,
    id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, OrganizationEmployee]]:
    """API view set for App organization model.

    Args:
        org_id (str):
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, OrganizationEmployee]]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
        id=id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    org_id: str,
    id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, OrganizationEmployee]]:
    """API view set for App organization model.

    Args:
        org_id (str):
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, OrganizationEmployee]]
    """

    return (
        await asyncio_detailed(
            org_id=org_id,
            id=id,
            client=client,
        )
    ).parsed
