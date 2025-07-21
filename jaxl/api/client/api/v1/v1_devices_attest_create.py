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
from ...models.device_attestation_error import DeviceAttestationError
from ...models.device_attestation_response import DeviceAttestationResponse
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/v1/devices/attest/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[DeviceAttestationError, DeviceAttestationResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = DeviceAttestationResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = DeviceAttestationError.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.CONFLICT:
        response_409 = DeviceAttestationError.from_dict(response.json())

        return response_409
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[DeviceAttestationError, DeviceAttestationResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Union[DeviceAttestationError, DeviceAttestationResponse]]:
    r"""Following payload is sent by MOBILE & WEB clients:

    Mobile: {
        # Device token to use for actual attestation with device provider
        \"dt\": deviceToken,
        # Device UUID generated locally by the client (only once) per new device.
        # This value is stored as \"uid\" in the device table
        \"pd\": deviceId,
        # User cookie
        \"cookie\": userCookie,
        # (MOBILE ONLY) Device fingerprint
        \"fp\": fingerprint,
    }

    WEB: {
        \"pd\": device_id,
        \"dt\": \"\",
        \"cookie\": signed_user_cookie,
    }

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DeviceAttestationError, DeviceAttestationResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> Optional[Union[DeviceAttestationError, DeviceAttestationResponse]]:
    r"""Following payload is sent by MOBILE & WEB clients:

    Mobile: {
        # Device token to use for actual attestation with device provider
        \"dt\": deviceToken,
        # Device UUID generated locally by the client (only once) per new device.
        # This value is stored as \"uid\" in the device table
        \"pd\": deviceId,
        # User cookie
        \"cookie\": userCookie,
        # (MOBILE ONLY) Device fingerprint
        \"fp\": fingerprint,
    }

    WEB: {
        \"pd\": device_id,
        \"dt\": \"\",
        \"cookie\": signed_user_cookie,
    }

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DeviceAttestationError, DeviceAttestationResponse]]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Union[DeviceAttestationError, DeviceAttestationResponse]]:
    r"""Following payload is sent by MOBILE & WEB clients:

    Mobile: {
        # Device token to use for actual attestation with device provider
        \"dt\": deviceToken,
        # Device UUID generated locally by the client (only once) per new device.
        # This value is stored as \"uid\" in the device table
        \"pd\": deviceId,
        # User cookie
        \"cookie\": userCookie,
        # (MOBILE ONLY) Device fingerprint
        \"fp\": fingerprint,
    }

    WEB: {
        \"pd\": device_id,
        \"dt\": \"\",
        \"cookie\": signed_user_cookie,
    }

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DeviceAttestationError, DeviceAttestationResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Optional[Union[DeviceAttestationError, DeviceAttestationResponse]]:
    r"""Following payload is sent by MOBILE & WEB clients:

    Mobile: {
        # Device token to use for actual attestation with device provider
        \"dt\": deviceToken,
        # Device UUID generated locally by the client (only once) per new device.
        # This value is stored as \"uid\" in the device table
        \"pd\": deviceId,
        # User cookie
        \"cookie\": userCookie,
        # (MOBILE ONLY) Device fingerprint
        \"fp\": fingerprint,
    }

    WEB: {
        \"pd\": device_id,
        \"dt\": \"\",
        \"cookie\": signed_user_cookie,
    }

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DeviceAttestationError, DeviceAttestationResponse]]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
