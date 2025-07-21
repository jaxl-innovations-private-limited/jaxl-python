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
from ...models.paginated_address_provider_list import (
    PaginatedAddressProviderList,
)
from ...models.v1_kyc_address_list_exclude import V1KycAddressListExclude
from ...models.v1_kyc_address_list_iso_country import (
    V1KycAddressListIsoCountry,
)
from ...models.v1_kyc_address_list_resource import V1KycAddressListResource
from ...models.v1_kyc_address_list_status import V1KycAddressListStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    exclude: Union[Unset, None, V1KycAddressListExclude] = UNSET,
    historical: Union[Unset, None, bool] = UNSET,
    iso_country: Union[Unset, None, V1KycAddressListIsoCountry] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    resource: Union[Unset, None, V1KycAddressListResource] = UNSET,
    status: Union[Unset, None, V1KycAddressListStatus] = UNSET,
    useridentity_id: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/v1/kyc/address/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_exclude: Union[Unset, None, str] = UNSET
    if not isinstance(exclude, Unset):
        json_exclude = exclude.value if exclude else None

    params["exclude"] = json_exclude

    params["historical"] = historical

    json_iso_country: Union[Unset, None, str] = UNSET
    if not isinstance(iso_country, Unset):
        json_iso_country = iso_country.value if iso_country else None

    params["iso_country"] = json_iso_country

    params["limit"] = limit

    params["offset"] = offset

    json_resource: Union[Unset, None, str] = UNSET
    if not isinstance(resource, Unset):
        json_resource = resource.value if resource else None

    params["resource"] = json_resource

    json_status: Union[Unset, None, str] = UNSET
    if not isinstance(status, Unset):
        json_status = status.value if status else None

    params["status"] = json_status

    params["useridentity_id"] = useridentity_id

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
) -> Optional[PaginatedAddressProviderList]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PaginatedAddressProviderList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[PaginatedAddressProviderList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    exclude: Union[Unset, None, V1KycAddressListExclude] = UNSET,
    historical: Union[Unset, None, bool] = UNSET,
    iso_country: Union[Unset, None, V1KycAddressListIsoCountry] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    resource: Union[Unset, None, V1KycAddressListResource] = UNSET,
    status: Union[Unset, None, V1KycAddressListStatus] = UNSET,
    useridentity_id: Union[Unset, None, int] = UNSET,
) -> Response[PaginatedAddressProviderList]:
    """
    Args:
        exclude (Union[Unset, None, V1KycAddressListExclude]):
        historical (Union[Unset, None, bool]):
        iso_country (Union[Unset, None, V1KycAddressListIsoCountry]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        resource (Union[Unset, None, V1KycAddressListResource]):
        status (Union[Unset, None, V1KycAddressListStatus]):
        useridentity_id (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedAddressProviderList]
    """

    kwargs = _get_kwargs(
        client=client,
        exclude=exclude,
        historical=historical,
        iso_country=iso_country,
        limit=limit,
        offset=offset,
        resource=resource,
        status=status,
        useridentity_id=useridentity_id,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    exclude: Union[Unset, None, V1KycAddressListExclude] = UNSET,
    historical: Union[Unset, None, bool] = UNSET,
    iso_country: Union[Unset, None, V1KycAddressListIsoCountry] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    resource: Union[Unset, None, V1KycAddressListResource] = UNSET,
    status: Union[Unset, None, V1KycAddressListStatus] = UNSET,
    useridentity_id: Union[Unset, None, int] = UNSET,
) -> Optional[PaginatedAddressProviderList]:
    """
    Args:
        exclude (Union[Unset, None, V1KycAddressListExclude]):
        historical (Union[Unset, None, bool]):
        iso_country (Union[Unset, None, V1KycAddressListIsoCountry]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        resource (Union[Unset, None, V1KycAddressListResource]):
        status (Union[Unset, None, V1KycAddressListStatus]):
        useridentity_id (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedAddressProviderList]
    """

    return sync_detailed(
        client=client,
        exclude=exclude,
        historical=historical,
        iso_country=iso_country,
        limit=limit,
        offset=offset,
        resource=resource,
        status=status,
        useridentity_id=useridentity_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    exclude: Union[Unset, None, V1KycAddressListExclude] = UNSET,
    historical: Union[Unset, None, bool] = UNSET,
    iso_country: Union[Unset, None, V1KycAddressListIsoCountry] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    resource: Union[Unset, None, V1KycAddressListResource] = UNSET,
    status: Union[Unset, None, V1KycAddressListStatus] = UNSET,
    useridentity_id: Union[Unset, None, int] = UNSET,
) -> Response[PaginatedAddressProviderList]:
    """
    Args:
        exclude (Union[Unset, None, V1KycAddressListExclude]):
        historical (Union[Unset, None, bool]):
        iso_country (Union[Unset, None, V1KycAddressListIsoCountry]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        resource (Union[Unset, None, V1KycAddressListResource]):
        status (Union[Unset, None, V1KycAddressListStatus]):
        useridentity_id (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedAddressProviderList]
    """

    kwargs = _get_kwargs(
        client=client,
        exclude=exclude,
        historical=historical,
        iso_country=iso_country,
        limit=limit,
        offset=offset,
        resource=resource,
        status=status,
        useridentity_id=useridentity_id,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    exclude: Union[Unset, None, V1KycAddressListExclude] = UNSET,
    historical: Union[Unset, None, bool] = UNSET,
    iso_country: Union[Unset, None, V1KycAddressListIsoCountry] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    resource: Union[Unset, None, V1KycAddressListResource] = UNSET,
    status: Union[Unset, None, V1KycAddressListStatus] = UNSET,
    useridentity_id: Union[Unset, None, int] = UNSET,
) -> Optional[PaginatedAddressProviderList]:
    """
    Args:
        exclude (Union[Unset, None, V1KycAddressListExclude]):
        historical (Union[Unset, None, bool]):
        iso_country (Union[Unset, None, V1KycAddressListIsoCountry]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        resource (Union[Unset, None, V1KycAddressListResource]):
        status (Union[Unset, None, V1KycAddressListStatus]):
        useridentity_id (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedAddressProviderList]
    """

    return (
        await asyncio_detailed(
            client=client,
            exclude=exclude,
            historical=historical,
            iso_country=iso_country,
            limit=limit,
            offset=offset,
            resource=resource,
            status=status,
            useridentity_id=useridentity_id,
        )
    ).parsed
