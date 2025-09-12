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
from ...models.aadhar_xml_upload_request import AadharXmlUploadRequest
from ...models.kyc_document_response import KycDocumentResponse
from ...models.kyc_invalid_response import KycInvalidResponse
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    multipart_data: AadharXmlUploadRequest,
) -> Dict[str, Any]:
    url = "{}/v1/kyc/offline/".format(client.base_url)

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
) -> Optional[Union[KycDocumentResponse, KycInvalidResponse]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = KycDocumentResponse.from_dict(response.json())

        return response_201
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = KycInvalidResponse.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.CONFLICT:
        response_409 = KycInvalidResponse.from_dict(response.json())

        return response_409
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[KycDocumentResponse, KycInvalidResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    multipart_data: AadharXmlUploadRequest,
) -> Response[Union[KycDocumentResponse, KycInvalidResponse]]:
    """
    Args:
        multipart_data (AadharXmlUploadRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[KycDocumentResponse, KycInvalidResponse]]
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
    multipart_data: AadharXmlUploadRequest,
) -> Optional[Union[KycDocumentResponse, KycInvalidResponse]]:
    """
    Args:
        multipart_data (AadharXmlUploadRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[KycDocumentResponse, KycInvalidResponse]]
    """

    return sync_detailed(
        client=client,
        multipart_data=multipart_data,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    multipart_data: AadharXmlUploadRequest,
) -> Response[Union[KycDocumentResponse, KycInvalidResponse]]:
    """
    Args:
        multipart_data (AadharXmlUploadRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[KycDocumentResponse, KycInvalidResponse]]
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
    multipart_data: AadharXmlUploadRequest,
) -> Optional[Union[KycDocumentResponse, KycInvalidResponse]]:
    """
    Args:
        multipart_data (AadharXmlUploadRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[KycDocumentResponse, KycInvalidResponse]]
    """

    return (
        await asyncio_detailed(
            client=client,
            multipart_data=multipart_data,
        )
    ).parsed
