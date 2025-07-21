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
from ...models.address_provider import AddressProvider
from ...models.kyc_address_creation_request import KycAddressCreationRequest
from ...models.kyc_improper_address_response import KycImproperAddressResponse
from ...models.kyc_invalidated_address_response import (
    KycInvalidatedAddressResponse,
)
from ...models.kyc_invalidated_address_with_suggestion_response import (
    KycInvalidatedAddressWithSuggestionResponse,
)
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: KycAddressCreationRequest,
) -> Dict[str, Any]:
    url = "{}/v1/kyc/address/".format(client.base_url)

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[
    Union[
        AddressProvider,
        Any,
        KycImproperAddressResponse,
        KycInvalidatedAddressResponse,
        KycInvalidatedAddressWithSuggestionResponse,
    ]
]:
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = cast(Any, None)
        return response_422
    if response.status_code == HTTPStatus.CREATED:
        response_201 = AddressProvider.from_dict(response.json())

        return response_201
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = KycImproperAddressResponse.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.EXPECTATION_FAILED:
        response_417 = KycInvalidatedAddressWithSuggestionResponse.from_dict(
            response.json()
        )

        return response_417
    if response.status_code == HTTPStatus.NOT_ACCEPTABLE:
        response_406 = KycInvalidatedAddressResponse.from_dict(response.json())

        return response_406
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[
    Union[
        AddressProvider,
        Any,
        KycImproperAddressResponse,
        KycInvalidatedAddressResponse,
        KycInvalidatedAddressWithSuggestionResponse,
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: KycAddressCreationRequest,
) -> Response[
    Union[
        AddressProvider,
        Any,
        KycImproperAddressResponse,
        KycInvalidatedAddressResponse,
        KycInvalidatedAddressWithSuggestionResponse,
    ]
]:
    """
    Args:
        json_body (KycAddressCreationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AddressProvider, Any, KycImproperAddressResponse, KycInvalidatedAddressResponse, KycInvalidatedAddressWithSuggestionResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    json_body: KycAddressCreationRequest,
) -> Optional[
    Union[
        AddressProvider,
        Any,
        KycImproperAddressResponse,
        KycInvalidatedAddressResponse,
        KycInvalidatedAddressWithSuggestionResponse,
    ]
]:
    """
    Args:
        json_body (KycAddressCreationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AddressProvider, Any, KycImproperAddressResponse, KycInvalidatedAddressResponse, KycInvalidatedAddressWithSuggestionResponse]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: KycAddressCreationRequest,
) -> Response[
    Union[
        AddressProvider,
        Any,
        KycImproperAddressResponse,
        KycInvalidatedAddressResponse,
        KycInvalidatedAddressWithSuggestionResponse,
    ]
]:
    """
    Args:
        json_body (KycAddressCreationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AddressProvider, Any, KycImproperAddressResponse, KycInvalidatedAddressResponse, KycInvalidatedAddressWithSuggestionResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    json_body: KycAddressCreationRequest,
) -> Optional[
    Union[
        AddressProvider,
        Any,
        KycImproperAddressResponse,
        KycInvalidatedAddressResponse,
        KycInvalidatedAddressWithSuggestionResponse,
    ]
]:
    """
    Args:
        json_body (KycAddressCreationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AddressProvider, Any, KycImproperAddressResponse, KycInvalidatedAddressResponse, KycInvalidatedAddressWithSuggestionResponse]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
