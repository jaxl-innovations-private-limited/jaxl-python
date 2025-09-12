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
from ...models.aadhar_otp_invalid_response import AadharOtpInvalidResponse
from ...models.aadhar_otp_response import AadharOtpResponse
from ...models.offline_aadhar_otp_request_request import (
    OfflineAadharOtpRequestRequest,
)
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    multipart_data: OfflineAadharOtpRequestRequest,
) -> Dict[str, Any]:
    url = "{}/v1/kyc/offline/otp/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    multipart_multipart_data = multipart_data.to_multipart()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "files": multipart_multipart_data,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[AadharOtpInvalidResponse, AadharOtpResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = AadharOtpResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = AadharOtpInvalidResponse.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        response_429 = AadharOtpInvalidResponse.from_dict(response.json())

        return response_429
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[AadharOtpInvalidResponse, AadharOtpResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    multipart_data: OfflineAadharOtpRequestRequest,
) -> Response[Union[AadharOtpInvalidResponse, AadharOtpResponse]]:
    """
    Args:
        multipart_data (OfflineAadharOtpRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AadharOtpInvalidResponse, AadharOtpResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        multipart_data=multipart_data,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    multipart_data: OfflineAadharOtpRequestRequest,
) -> Optional[Union[AadharOtpInvalidResponse, AadharOtpResponse]]:
    """
    Args:
        multipart_data (OfflineAadharOtpRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AadharOtpInvalidResponse, AadharOtpResponse]]
    """

    return sync_detailed(
        client=client,
        multipart_data=multipart_data,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    multipart_data: OfflineAadharOtpRequestRequest,
) -> Response[Union[AadharOtpInvalidResponse, AadharOtpResponse]]:
    """
    Args:
        multipart_data (OfflineAadharOtpRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AadharOtpInvalidResponse, AadharOtpResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        multipart_data=multipart_data,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    multipart_data: OfflineAadharOtpRequestRequest,
) -> Optional[Union[AadharOtpInvalidResponse, AadharOtpResponse]]:
    """
    Args:
        multipart_data (OfflineAadharOtpRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AadharOtpInvalidResponse, AadharOtpResponse]]
    """

    return (
        await asyncio_detailed(
            client=client,
            multipart_data=multipart_data,
        )
    ).parsed
