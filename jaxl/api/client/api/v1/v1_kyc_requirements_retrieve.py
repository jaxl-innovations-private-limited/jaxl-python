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
from ...models.kyc_invalid_response import KycInvalidResponse
from ...models.kyc_requirements_response import KycRequirementsResponse
from ...models.v1_kyc_requirements_retrieve_iso_country import (
    V1KycRequirementsRetrieveIsoCountry,
)
from ...models.v1_kyc_requirements_retrieve_resource import (
    V1KycRequirementsRetrieveResource,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    iso_country: V1KycRequirementsRetrieveIsoCountry,
    resource: Union[Unset, None, V1KycRequirementsRetrieveResource] = UNSET,
    sku: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/v1/kyc/requirements/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_iso_country = iso_country.value

    params["iso_country"] = json_iso_country

    json_resource: Union[Unset, None, str] = UNSET
    if not isinstance(resource, Unset):
        json_resource = resource.value if resource else None

    params["resource"] = json_resource

    params["sku"] = sku

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
) -> Optional[Union[KycInvalidResponse, KycRequirementsResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = KycRequirementsResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.NOT_ACCEPTABLE:
        response_406 = KycInvalidResponse.from_dict(response.json())

        return response_406
    if response.status_code == HTTPStatus.UNAVAILABLE_FOR_LEGAL_REASONS:
        response_451 = KycInvalidResponse.from_dict(response.json())

        return response_451
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[KycInvalidResponse, KycRequirementsResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    iso_country: V1KycRequirementsRetrieveIsoCountry,
    resource: Union[Unset, None, V1KycRequirementsRetrieveResource] = UNSET,
    sku: Union[Unset, None, str] = UNSET,
) -> Response[Union[KycInvalidResponse, KycRequirementsResponse]]:
    """
    Args:
        iso_country (V1KycRequirementsRetrieveIsoCountry):
        resource (Union[Unset, None, V1KycRequirementsRetrieveResource]):
        sku (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[KycInvalidResponse, KycRequirementsResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        iso_country=iso_country,
        resource=resource,
        sku=sku,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    iso_country: V1KycRequirementsRetrieveIsoCountry,
    resource: Union[Unset, None, V1KycRequirementsRetrieveResource] = UNSET,
    sku: Union[Unset, None, str] = UNSET,
) -> Optional[Union[KycInvalidResponse, KycRequirementsResponse]]:
    """
    Args:
        iso_country (V1KycRequirementsRetrieveIsoCountry):
        resource (Union[Unset, None, V1KycRequirementsRetrieveResource]):
        sku (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[KycInvalidResponse, KycRequirementsResponse]]
    """

    return sync_detailed(
        client=client,
        iso_country=iso_country,
        resource=resource,
        sku=sku,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    iso_country: V1KycRequirementsRetrieveIsoCountry,
    resource: Union[Unset, None, V1KycRequirementsRetrieveResource] = UNSET,
    sku: Union[Unset, None, str] = UNSET,
) -> Response[Union[KycInvalidResponse, KycRequirementsResponse]]:
    """
    Args:
        iso_country (V1KycRequirementsRetrieveIsoCountry):
        resource (Union[Unset, None, V1KycRequirementsRetrieveResource]):
        sku (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[KycInvalidResponse, KycRequirementsResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        iso_country=iso_country,
        resource=resource,
        sku=sku,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    iso_country: V1KycRequirementsRetrieveIsoCountry,
    resource: Union[Unset, None, V1KycRequirementsRetrieveResource] = UNSET,
    sku: Union[Unset, None, str] = UNSET,
) -> Optional[Union[KycInvalidResponse, KycRequirementsResponse]]:
    """
    Args:
        iso_country (V1KycRequirementsRetrieveIsoCountry):
        resource (Union[Unset, None, V1KycRequirementsRetrieveResource]):
        sku (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[KycInvalidResponse, KycRequirementsResponse]]
    """

    return (
        await asyncio_detailed(
            client=client,
            iso_country=iso_country,
            resource=resource,
            sku=sku,
        )
    ).parsed
