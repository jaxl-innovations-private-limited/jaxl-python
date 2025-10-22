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
from ...models.invalid_provider_request import InvalidProviderRequest
from ...models.paginated_organization_provider_list import (
    PaginatedOrganizationProviderList,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    org_id: str,
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/v1/app/organizations/{org_id}/providers/".format(
        client.base_url, org_id=org_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
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
) -> Optional[Union[Any, InvalidProviderRequest, PaginatedOrganizationProviderList]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PaginatedOrganizationProviderList.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = InvalidProviderRequest.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(Any, None)
        return response_403
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[Any, InvalidProviderRequest, PaginatedOrganizationProviderList]]:
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
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
) -> Response[Union[Any, InvalidProviderRequest, PaginatedOrganizationProviderList]]:
    """Authentication and Configuration Mapping for Shopify and Exotel Integrations
    Shopify Required Fields:
    ------------------------
    - public_key     == shop_url
        The full Shopify store URL. Example: 'https://your-store.myshopify.com'
    - private_key    == access token
        The private access token for the Shopify private or custom app.

    Exotel Required Fields:
    -----------------------
    - public_key     == api key
    - private_key    == api token
    - webhook_secret == tenant ID
    - certificate    == flow ID

    Args:
        org_id (str):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, InvalidProviderRequest, PaginatedOrganizationProviderList]]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
        client=client,
        limit=limit,
        offset=offset,
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
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
) -> Optional[Union[Any, InvalidProviderRequest, PaginatedOrganizationProviderList]]:
    """Authentication and Configuration Mapping for Shopify and Exotel Integrations
    Shopify Required Fields:
    ------------------------
    - public_key     == shop_url
        The full Shopify store URL. Example: 'https://your-store.myshopify.com'
    - private_key    == access token
        The private access token for the Shopify private or custom app.

    Exotel Required Fields:
    -----------------------
    - public_key     == api key
    - private_key    == api token
    - webhook_secret == tenant ID
    - certificate    == flow ID

    Args:
        org_id (str):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, InvalidProviderRequest, PaginatedOrganizationProviderList]]
    """

    return sync_detailed(
        org_id=org_id,
        client=client,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    org_id: str,
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
) -> Response[Union[Any, InvalidProviderRequest, PaginatedOrganizationProviderList]]:
    """Authentication and Configuration Mapping for Shopify and Exotel Integrations
    Shopify Required Fields:
    ------------------------
    - public_key     == shop_url
        The full Shopify store URL. Example: 'https://your-store.myshopify.com'
    - private_key    == access token
        The private access token for the Shopify private or custom app.

    Exotel Required Fields:
    -----------------------
    - public_key     == api key
    - private_key    == api token
    - webhook_secret == tenant ID
    - certificate    == flow ID

    Args:
        org_id (str):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, InvalidProviderRequest, PaginatedOrganizationProviderList]]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
        client=client,
        limit=limit,
        offset=offset,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    org_id: str,
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
) -> Optional[Union[Any, InvalidProviderRequest, PaginatedOrganizationProviderList]]:
    """Authentication and Configuration Mapping for Shopify and Exotel Integrations
    Shopify Required Fields:
    ------------------------
    - public_key     == shop_url
        The full Shopify store URL. Example: 'https://your-store.myshopify.com'
    - private_key    == access token
        The private access token for the Shopify private or custom app.

    Exotel Required Fields:
    -----------------------
    - public_key     == api key
    - private_key    == api token
    - webhook_secret == tenant ID
    - certificate    == flow ID

    Args:
        org_id (str):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, InvalidProviderRequest, PaginatedOrganizationProviderList]]
    """

    return (
        await asyncio_detailed(
            org_id=org_id,
            client=client,
            limit=limit,
            offset=offset,
        )
    ).parsed
