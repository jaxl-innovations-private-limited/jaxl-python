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
from ...models.paginated_user_identity_list import PaginatedUserIdentityList
from ...models.v1_kyc_identity_list_iso_country import (
    V1KycIdentityListIsoCountry,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    iso_country: Union[Unset, None, V1KycIdentityListIsoCountry] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/v1/kyc/identity/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_iso_country: Union[Unset, None, str] = UNSET
    if not isinstance(iso_country, Unset):
        json_iso_country = iso_country.value if iso_country else None

    params["iso_country"] = json_iso_country

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
) -> Optional[PaginatedUserIdentityList]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PaginatedUserIdentityList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[PaginatedUserIdentityList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    iso_country: Union[Unset, None, V1KycIdentityListIsoCountry] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
) -> Response[PaginatedUserIdentityList]:
    """
    Args:
        iso_country (Union[Unset, None, V1KycIdentityListIsoCountry]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedUserIdentityList]
    """

    kwargs = _get_kwargs(
        client=client,
        iso_country=iso_country,
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
    iso_country: Union[Unset, None, V1KycIdentityListIsoCountry] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
) -> Optional[PaginatedUserIdentityList]:
    """
    Args:
        iso_country (Union[Unset, None, V1KycIdentityListIsoCountry]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedUserIdentityList]
    """

    return sync_detailed(
        client=client,
        iso_country=iso_country,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    iso_country: Union[Unset, None, V1KycIdentityListIsoCountry] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
) -> Response[PaginatedUserIdentityList]:
    """
    Args:
        iso_country (Union[Unset, None, V1KycIdentityListIsoCountry]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedUserIdentityList]
    """

    kwargs = _get_kwargs(
        client=client,
        iso_country=iso_country,
        limit=limit,
        offset=offset,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    iso_country: Union[Unset, None, V1KycIdentityListIsoCountry] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
) -> Optional[PaginatedUserIdentityList]:
    """
    Args:
        iso_country (Union[Unset, None, V1KycIdentityListIsoCountry]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedUserIdentityList]
    """

    return (
        await asyncio_detailed(
            client=client,
            iso_country=iso_country,
            limit=limit,
            offset=offset,
        )
    ).parsed
