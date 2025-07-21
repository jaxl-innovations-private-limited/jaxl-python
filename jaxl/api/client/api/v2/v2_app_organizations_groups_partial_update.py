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
from ...models.organization_group_response import OrganizationGroupResponse
from ...models.patched_organization_group_update_request import (
    PatchedOrganizationGroupUpdateRequest,
)
from ...types import Response


def _get_kwargs(
    org_id: str,
    id: int,
    *,
    client: AuthenticatedClient,
    json_body: PatchedOrganizationGroupUpdateRequest,
) -> Dict[str, Any]:
    url = "{}/v2/app/organizations/{org_id}/groups/{id}/".format(
        client.base_url, org_id=org_id, id=id
    )

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
) -> Optional[OrganizationGroupResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = OrganizationGroupResponse.from_dict(response.json())

        return response_200
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
    id: int,
    *,
    client: AuthenticatedClient,
    json_body: PatchedOrganizationGroupUpdateRequest,
) -> Response[OrganizationGroupResponse]:
    """Use to rename the org team and add/remove member from team.

    Args:
        org_id (str):
        id (int):
        json_body (PatchedOrganizationGroupUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrganizationGroupResponse]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
        id=id,
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
    id: int,
    *,
    client: AuthenticatedClient,
    json_body: PatchedOrganizationGroupUpdateRequest,
) -> Optional[OrganizationGroupResponse]:
    """Use to rename the org team and add/remove member from team.

    Args:
        org_id (str):
        id (int):
        json_body (PatchedOrganizationGroupUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrganizationGroupResponse]
    """

    return sync_detailed(
        org_id=org_id,
        id=id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    org_id: str,
    id: int,
    *,
    client: AuthenticatedClient,
    json_body: PatchedOrganizationGroupUpdateRequest,
) -> Response[OrganizationGroupResponse]:
    """Use to rename the org team and add/remove member from team.

    Args:
        org_id (str):
        id (int):
        json_body (PatchedOrganizationGroupUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrganizationGroupResponse]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
        id=id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    org_id: str,
    id: int,
    *,
    client: AuthenticatedClient,
    json_body: PatchedOrganizationGroupUpdateRequest,
) -> Optional[OrganizationGroupResponse]:
    """Use to rename the org team and add/remove member from team.

    Args:
        org_id (str):
        id (int):
        json_body (PatchedOrganizationGroupUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrganizationGroupResponse]
    """

    return (
        await asyncio_detailed(
            org_id=org_id,
            id=id,
            client=client,
            json_body=json_body,
        )
    ).parsed
