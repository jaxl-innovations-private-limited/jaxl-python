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
from ...models.organization_group_request import OrganizationGroupRequest
from ...models.organization_group_response import OrganizationGroupResponse
from ...types import Response


def _get_kwargs(
    org_id: str,
    *,
    client: AuthenticatedClient,
    json_body: OrganizationGroupRequest,
) -> Dict[str, Any]:
    url = "{}/v2/app/organizations/{org_id}/groups/".format(
        client.base_url, org_id=org_id
    )

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
) -> Optional[OrganizationGroupResponse]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = OrganizationGroupResponse.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[OrganizationGroupResponse]:
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
    json_body: OrganizationGroupRequest,
) -> Response[OrganizationGroupResponse]:
    """Create a new team.

    Args:
        org_id (str):
        json_body (OrganizationGroupRequest): Adds a 'jaxlid' field which contains signed ID
            information.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrganizationGroupResponse]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
        client=client,
        json_body=json_body,
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
    json_body: OrganizationGroupRequest,
) -> Optional[OrganizationGroupResponse]:
    """Create a new team.

    Args:
        org_id (str):
        json_body (OrganizationGroupRequest): Adds a 'jaxlid' field which contains signed ID
            information.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrganizationGroupResponse]
    """

    return sync_detailed(
        org_id=org_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    org_id: str,
    *,
    client: AuthenticatedClient,
    json_body: OrganizationGroupRequest,
) -> Response[OrganizationGroupResponse]:
    """Create a new team.

    Args:
        org_id (str):
        json_body (OrganizationGroupRequest): Adds a 'jaxlid' field which contains signed ID
            information.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrganizationGroupResponse]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    org_id: str,
    *,
    client: AuthenticatedClient,
    json_body: OrganizationGroupRequest,
) -> Optional[OrganizationGroupResponse]:
    """Create a new team.

    Args:
        org_id (str):
        json_body (OrganizationGroupRequest): Adds a 'jaxlid' field which contains signed ID
            information.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrganizationGroupResponse]
    """

    return (
        await asyncio_detailed(
            org_id=org_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
