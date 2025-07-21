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
from ...models.organization_employee_invitation_request import (
    OrganizationEmployeeInvitationRequest,
)
from ...models.organization_employee_invite_response import (
    OrganizationEmployeeInviteResponse,
)
from ...types import Response


def _get_kwargs(
    org_id: str,
    *,
    client: AuthenticatedClient,
    json_body: OrganizationEmployeeInvitationRequest,
) -> Dict[str, Any]:
    url = "{}/v2/app/organizations/{org_id}/employees/invite/".format(
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
) -> Optional[OrganizationEmployeeInviteResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = OrganizationEmployeeInviteResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[OrganizationEmployeeInviteResponse]:
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
    json_body: OrganizationEmployeeInvitationRequest,
) -> Response[OrganizationEmployeeInviteResponse]:
    """API view set for App organization model.

    Args:
        org_id (str):
        json_body (OrganizationEmployeeInvitationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrganizationEmployeeInviteResponse]
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
    json_body: OrganizationEmployeeInvitationRequest,
) -> Optional[OrganizationEmployeeInviteResponse]:
    """API view set for App organization model.

    Args:
        org_id (str):
        json_body (OrganizationEmployeeInvitationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrganizationEmployeeInviteResponse]
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
    json_body: OrganizationEmployeeInvitationRequest,
) -> Response[OrganizationEmployeeInviteResponse]:
    """API view set for App organization model.

    Args:
        org_id (str):
        json_body (OrganizationEmployeeInvitationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrganizationEmployeeInviteResponse]
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
    json_body: OrganizationEmployeeInvitationRequest,
) -> Optional[OrganizationEmployeeInviteResponse]:
    """API view set for App organization model.

    Args:
        org_id (str):
        json_body (OrganizationEmployeeInvitationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrganizationEmployeeInviteResponse]
    """

    return (
        await asyncio_detailed(
            org_id=org_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
