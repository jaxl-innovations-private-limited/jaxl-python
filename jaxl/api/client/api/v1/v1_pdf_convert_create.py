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
from ...models.incorrect_pdf_image_conversion import (
    IncorrectPdfImageConversion,
)
from ...models.pdf_image_conversion_request import PdfImageConversionRequest
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    multipart_data: PdfImageConversionRequest,
) -> Dict[str, Any]:
    url = "{}/v1/pdf/convert/".format(client.base_url)

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
) -> Optional[IncorrectPdfImageConversion]:
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = IncorrectPdfImageConversion.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.NOT_ACCEPTABLE:
        response_406 = IncorrectPdfImageConversion.from_dict(response.json())

        return response_406
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[IncorrectPdfImageConversion]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    multipart_data: PdfImageConversionRequest,
) -> Response[IncorrectPdfImageConversion]:
    """
    Args:
        multipart_data (PdfImageConversionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IncorrectPdfImageConversion]
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
    multipart_data: PdfImageConversionRequest,
) -> Optional[IncorrectPdfImageConversion]:
    """
    Args:
        multipart_data (PdfImageConversionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IncorrectPdfImageConversion]
    """

    return sync_detailed(
        client=client,
        multipart_data=multipart_data,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    multipart_data: PdfImageConversionRequest,
) -> Response[IncorrectPdfImageConversion]:
    """
    Args:
        multipart_data (PdfImageConversionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IncorrectPdfImageConversion]
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
    multipart_data: PdfImageConversionRequest,
) -> Optional[IncorrectPdfImageConversion]:
    """
    Args:
        multipart_data (PdfImageConversionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IncorrectPdfImageConversion]
    """

    return (
        await asyncio_detailed(
            client=client,
            multipart_data=multipart_data,
        )
    ).parsed
