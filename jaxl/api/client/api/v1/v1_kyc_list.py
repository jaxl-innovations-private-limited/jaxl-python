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
from ...models.paginated_kyc_list import PaginatedKycList
from ...models.v1_kyc_list_iso_country import V1KycListIsoCountry
from ...models.v1_kyc_list_provider_status_item import V1KycListProviderStatusItem
from ...models.v1_kyc_list_resource import V1KycListResource
from ...models.v1_kyc_list_status import V1KycListStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    iso_country: Union[Unset, None, V1KycListIsoCountry] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    provider_status: Union[Unset, None, List[V1KycListProviderStatusItem]] = UNSET,
    resource: Union[Unset, None, V1KycListResource] = UNSET,
    status: Union[Unset, None, V1KycListStatus] = UNSET,
) -> Dict[str, Any]:
    url = "{}/v1/kyc/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_iso_country: Union[Unset, None, str] = UNSET
    if not isinstance(iso_country, Unset):
        json_iso_country = iso_country.value if iso_country else None

    params["iso_country"] = json_iso_country

    params["limit"] = limit

    params["offset"] = offset

    json_provider_status: Union[Unset, None, List[str]] = UNSET
    if not isinstance(provider_status, Unset):
        if provider_status is None:
            json_provider_status = None
        else:
            json_provider_status = []
            for provider_status_item_data in provider_status:
                provider_status_item = provider_status_item_data.value

                json_provider_status.append(provider_status_item)

    params["provider_status"] = json_provider_status

    json_resource: Union[Unset, None, str] = UNSET
    if not isinstance(resource, Unset):
        json_resource = resource.value if resource else None

    params["resource"] = json_resource

    json_status: Union[Unset, None, str] = UNSET
    if not isinstance(status, Unset):
        json_status = status.value if status else None

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
) -> Optional[PaginatedKycList]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PaginatedKycList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[PaginatedKycList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    iso_country: Union[Unset, None, V1KycListIsoCountry] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    provider_status: Union[Unset, None, List[V1KycListProviderStatusItem]] = UNSET,
    resource: Union[Unset, None, V1KycListResource] = UNSET,
    status: Union[Unset, None, V1KycListStatus] = UNSET,
) -> Response[PaginatedKycList]:
    """
    Args:
        iso_country (Union[Unset, None, V1KycListIsoCountry]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        provider_status (Union[Unset, None, List[V1KycListProviderStatusItem]]):
        resource (Union[Unset, None, V1KycListResource]):
        status (Union[Unset, None, V1KycListStatus]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedKycList]
    """

    kwargs = _get_kwargs(
        client=client,
        iso_country=iso_country,
        limit=limit,
        offset=offset,
        provider_status=provider_status,
        resource=resource,
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
    iso_country: Union[Unset, None, V1KycListIsoCountry] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    provider_status: Union[Unset, None, List[V1KycListProviderStatusItem]] = UNSET,
    resource: Union[Unset, None, V1KycListResource] = UNSET,
    status: Union[Unset, None, V1KycListStatus] = UNSET,
) -> Optional[PaginatedKycList]:
    """
    Args:
        iso_country (Union[Unset, None, V1KycListIsoCountry]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        provider_status (Union[Unset, None, List[V1KycListProviderStatusItem]]):
        resource (Union[Unset, None, V1KycListResource]):
        status (Union[Unset, None, V1KycListStatus]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedKycList]
    """

    return sync_detailed(
        client=client,
        iso_country=iso_country,
        limit=limit,
        offset=offset,
        provider_status=provider_status,
        resource=resource,
        status=status,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    iso_country: Union[Unset, None, V1KycListIsoCountry] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    provider_status: Union[Unset, None, List[V1KycListProviderStatusItem]] = UNSET,
    resource: Union[Unset, None, V1KycListResource] = UNSET,
    status: Union[Unset, None, V1KycListStatus] = UNSET,
) -> Response[PaginatedKycList]:
    """
    Args:
        iso_country (Union[Unset, None, V1KycListIsoCountry]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        provider_status (Union[Unset, None, List[V1KycListProviderStatusItem]]):
        resource (Union[Unset, None, V1KycListResource]):
        status (Union[Unset, None, V1KycListStatus]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedKycList]
    """

    kwargs = _get_kwargs(
        client=client,
        iso_country=iso_country,
        limit=limit,
        offset=offset,
        provider_status=provider_status,
        resource=resource,
        status=status,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    iso_country: Union[Unset, None, V1KycListIsoCountry] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    provider_status: Union[Unset, None, List[V1KycListProviderStatusItem]] = UNSET,
    resource: Union[Unset, None, V1KycListResource] = UNSET,
    status: Union[Unset, None, V1KycListStatus] = UNSET,
) -> Optional[PaginatedKycList]:
    """
    Args:
        iso_country (Union[Unset, None, V1KycListIsoCountry]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        provider_status (Union[Unset, None, List[V1KycListProviderStatusItem]]):
        resource (Union[Unset, None, V1KycListResource]):
        status (Union[Unset, None, V1KycListStatus]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedKycList]
    """

    return (
        await asyncio_detailed(
            client=client,
            iso_country=iso_country,
            limit=limit,
            offset=offset,
            provider_status=provider_status,
            resource=resource,
            status=status,
        )
    ).parsed
