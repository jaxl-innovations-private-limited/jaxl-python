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
from ...models.aadhar_otp_request_request import AadharOtpRequestRequest
from ...models.aadhar_otp_response import AadharOtpResponse
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: AadharOtpRequestRequest,
) -> Dict[str, Any]:
    url = "{}/v1/kyc/otp/".format(client.base_url)

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
    json_body: AadharOtpRequestRequest,
) -> Response[Union[AadharOtpInvalidResponse, AadharOtpResponse]]:
    """
    Args:
        json_body (AadharOtpRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AadharOtpInvalidResponse, AadharOtpResponse]]
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
    json_body: AadharOtpRequestRequest,
) -> Optional[Union[AadharOtpInvalidResponse, AadharOtpResponse]]:
    """
    Args:
        json_body (AadharOtpRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AadharOtpInvalidResponse, AadharOtpResponse]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: AadharOtpRequestRequest,
) -> Response[Union[AadharOtpInvalidResponse, AadharOtpResponse]]:
    """
    Args:
        json_body (AadharOtpRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AadharOtpInvalidResponse, AadharOtpResponse]]
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
    json_body: AadharOtpRequestRequest,
) -> Optional[Union[AadharOtpInvalidResponse, AadharOtpResponse]]:
    """
    Args:
        json_body (AadharOtpRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AadharOtpInvalidResponse, AadharOtpResponse]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
