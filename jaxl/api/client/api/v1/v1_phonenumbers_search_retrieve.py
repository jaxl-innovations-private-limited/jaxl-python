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
from ...models.phone_number_search_response import PhoneNumberSearchResponse
from ...models.v1_phonenumbers_search_retrieve_intent import (
    V1PhonenumbersSearchRetrieveIntent,
)
from ...models.v1_phonenumbers_search_retrieve_iso_country_code import (
    V1PhonenumbersSearchRetrieveIsoCountryCode,
)
from ...models.v1_phonenumbers_search_retrieve_resource import (
    V1PhonenumbersSearchRetrieveResource,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    contains: Union[Unset, None, int] = UNSET,
    fax_enabled: Union[Unset, None, bool] = UNSET,
    intent: Union[
        Unset, None, V1PhonenumbersSearchRetrieveIntent
    ] = V1PhonenumbersSearchRetrieveIntent.PROMOTIONAL,
    iso_country_code: V1PhonenumbersSearchRetrieveIsoCountryCode = V1PhonenumbersSearchRetrieveIsoCountryCode.US,
    locality: Union[Unset, None, str] = UNSET,
    mms_enabled: Union[Unset, None, bool] = UNSET,
    region: Union[Unset, None, str] = UNSET,
    resource: Union[Unset, None, V1PhonenumbersSearchRetrieveResource] = UNSET,
    sms_enabled: Union[Unset, None, bool] = UNSET,
    voice_enabled: Union[Unset, None, bool] = True,
) -> Dict[str, Any]:
    url = "{}/v1/phonenumbers/search/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["contains"] = contains

    params["fax_enabled"] = fax_enabled

    json_intent: Union[Unset, None, str] = UNSET
    if not isinstance(intent, Unset):
        json_intent = intent.value if intent else None

    params["intent"] = json_intent

    json_iso_country_code = iso_country_code.value

    params["iso_country_code"] = json_iso_country_code

    params["locality"] = locality

    params["mms_enabled"] = mms_enabled

    params["region"] = region

    json_resource: Union[Unset, None, str] = UNSET
    if not isinstance(resource, Unset):
        json_resource = resource.value if resource else None

    params["resource"] = json_resource

    params["sms_enabled"] = sms_enabled

    params["voice_enabled"] = voice_enabled

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
) -> Optional[Union[Any, PhoneNumberSearchResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PhoneNumberSearchResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.PRECONDITION_FAILED:
        response_412 = cast(Any, None)
        return response_412
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[Any, PhoneNumberSearchResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    contains: Union[Unset, None, int] = UNSET,
    fax_enabled: Union[Unset, None, bool] = UNSET,
    intent: Union[
        Unset, None, V1PhonenumbersSearchRetrieveIntent
    ] = V1PhonenumbersSearchRetrieveIntent.PROMOTIONAL,
    iso_country_code: V1PhonenumbersSearchRetrieveIsoCountryCode = V1PhonenumbersSearchRetrieveIsoCountryCode.US,
    locality: Union[Unset, None, str] = UNSET,
    mms_enabled: Union[Unset, None, bool] = UNSET,
    region: Union[Unset, None, str] = UNSET,
    resource: Union[Unset, None, V1PhonenumbersSearchRetrieveResource] = UNSET,
    sms_enabled: Union[Unset, None, bool] = UNSET,
    voice_enabled: Union[Unset, None, bool] = True,
) -> Response[Union[Any, PhoneNumberSearchResponse]]:
    """API view set for PhoneNumber model.

    Args:
        contains (Union[Unset, None, int]):
        fax_enabled (Union[Unset, None, bool]):
        intent (Union[Unset, None, V1PhonenumbersSearchRetrieveIntent]):  Default:
            V1PhonenumbersSearchRetrieveIntent.PROMOTIONAL.
        iso_country_code (V1PhonenumbersSearchRetrieveIsoCountryCode):  Default:
            V1PhonenumbersSearchRetrieveIsoCountryCode.US.
        locality (Union[Unset, None, str]):
        mms_enabled (Union[Unset, None, bool]):
        region (Union[Unset, None, str]):
        resource (Union[Unset, None, V1PhonenumbersSearchRetrieveResource]):
        sms_enabled (Union[Unset, None, bool]):
        voice_enabled (Union[Unset, None, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PhoneNumberSearchResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        contains=contains,
        fax_enabled=fax_enabled,
        intent=intent,
        iso_country_code=iso_country_code,
        locality=locality,
        mms_enabled=mms_enabled,
        region=region,
        resource=resource,
        sms_enabled=sms_enabled,
        voice_enabled=voice_enabled,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    contains: Union[Unset, None, int] = UNSET,
    fax_enabled: Union[Unset, None, bool] = UNSET,
    intent: Union[
        Unset, None, V1PhonenumbersSearchRetrieveIntent
    ] = V1PhonenumbersSearchRetrieveIntent.PROMOTIONAL,
    iso_country_code: V1PhonenumbersSearchRetrieveIsoCountryCode = V1PhonenumbersSearchRetrieveIsoCountryCode.US,
    locality: Union[Unset, None, str] = UNSET,
    mms_enabled: Union[Unset, None, bool] = UNSET,
    region: Union[Unset, None, str] = UNSET,
    resource: Union[Unset, None, V1PhonenumbersSearchRetrieveResource] = UNSET,
    sms_enabled: Union[Unset, None, bool] = UNSET,
    voice_enabled: Union[Unset, None, bool] = True,
) -> Optional[Union[Any, PhoneNumberSearchResponse]]:
    """API view set for PhoneNumber model.

    Args:
        contains (Union[Unset, None, int]):
        fax_enabled (Union[Unset, None, bool]):
        intent (Union[Unset, None, V1PhonenumbersSearchRetrieveIntent]):  Default:
            V1PhonenumbersSearchRetrieveIntent.PROMOTIONAL.
        iso_country_code (V1PhonenumbersSearchRetrieveIsoCountryCode):  Default:
            V1PhonenumbersSearchRetrieveIsoCountryCode.US.
        locality (Union[Unset, None, str]):
        mms_enabled (Union[Unset, None, bool]):
        region (Union[Unset, None, str]):
        resource (Union[Unset, None, V1PhonenumbersSearchRetrieveResource]):
        sms_enabled (Union[Unset, None, bool]):
        voice_enabled (Union[Unset, None, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PhoneNumberSearchResponse]]
    """

    return sync_detailed(
        client=client,
        contains=contains,
        fax_enabled=fax_enabled,
        intent=intent,
        iso_country_code=iso_country_code,
        locality=locality,
        mms_enabled=mms_enabled,
        region=region,
        resource=resource,
        sms_enabled=sms_enabled,
        voice_enabled=voice_enabled,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    contains: Union[Unset, None, int] = UNSET,
    fax_enabled: Union[Unset, None, bool] = UNSET,
    intent: Union[
        Unset, None, V1PhonenumbersSearchRetrieveIntent
    ] = V1PhonenumbersSearchRetrieveIntent.PROMOTIONAL,
    iso_country_code: V1PhonenumbersSearchRetrieveIsoCountryCode = V1PhonenumbersSearchRetrieveIsoCountryCode.US,
    locality: Union[Unset, None, str] = UNSET,
    mms_enabled: Union[Unset, None, bool] = UNSET,
    region: Union[Unset, None, str] = UNSET,
    resource: Union[Unset, None, V1PhonenumbersSearchRetrieveResource] = UNSET,
    sms_enabled: Union[Unset, None, bool] = UNSET,
    voice_enabled: Union[Unset, None, bool] = True,
) -> Response[Union[Any, PhoneNumberSearchResponse]]:
    """API view set for PhoneNumber model.

    Args:
        contains (Union[Unset, None, int]):
        fax_enabled (Union[Unset, None, bool]):
        intent (Union[Unset, None, V1PhonenumbersSearchRetrieveIntent]):  Default:
            V1PhonenumbersSearchRetrieveIntent.PROMOTIONAL.
        iso_country_code (V1PhonenumbersSearchRetrieveIsoCountryCode):  Default:
            V1PhonenumbersSearchRetrieveIsoCountryCode.US.
        locality (Union[Unset, None, str]):
        mms_enabled (Union[Unset, None, bool]):
        region (Union[Unset, None, str]):
        resource (Union[Unset, None, V1PhonenumbersSearchRetrieveResource]):
        sms_enabled (Union[Unset, None, bool]):
        voice_enabled (Union[Unset, None, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PhoneNumberSearchResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        contains=contains,
        fax_enabled=fax_enabled,
        intent=intent,
        iso_country_code=iso_country_code,
        locality=locality,
        mms_enabled=mms_enabled,
        region=region,
        resource=resource,
        sms_enabled=sms_enabled,
        voice_enabled=voice_enabled,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    contains: Union[Unset, None, int] = UNSET,
    fax_enabled: Union[Unset, None, bool] = UNSET,
    intent: Union[
        Unset, None, V1PhonenumbersSearchRetrieveIntent
    ] = V1PhonenumbersSearchRetrieveIntent.PROMOTIONAL,
    iso_country_code: V1PhonenumbersSearchRetrieveIsoCountryCode = V1PhonenumbersSearchRetrieveIsoCountryCode.US,
    locality: Union[Unset, None, str] = UNSET,
    mms_enabled: Union[Unset, None, bool] = UNSET,
    region: Union[Unset, None, str] = UNSET,
    resource: Union[Unset, None, V1PhonenumbersSearchRetrieveResource] = UNSET,
    sms_enabled: Union[Unset, None, bool] = UNSET,
    voice_enabled: Union[Unset, None, bool] = True,
) -> Optional[Union[Any, PhoneNumberSearchResponse]]:
    """API view set for PhoneNumber model.

    Args:
        contains (Union[Unset, None, int]):
        fax_enabled (Union[Unset, None, bool]):
        intent (Union[Unset, None, V1PhonenumbersSearchRetrieveIntent]):  Default:
            V1PhonenumbersSearchRetrieveIntent.PROMOTIONAL.
        iso_country_code (V1PhonenumbersSearchRetrieveIsoCountryCode):  Default:
            V1PhonenumbersSearchRetrieveIsoCountryCode.US.
        locality (Union[Unset, None, str]):
        mms_enabled (Union[Unset, None, bool]):
        region (Union[Unset, None, str]):
        resource (Union[Unset, None, V1PhonenumbersSearchRetrieveResource]):
        sms_enabled (Union[Unset, None, bool]):
        voice_enabled (Union[Unset, None, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PhoneNumberSearchResponse]]
    """

    return (
        await asyncio_detailed(
            client=client,
            contains=contains,
            fax_enabled=fax_enabled,
            intent=intent,
            iso_country_code=iso_country_code,
            locality=locality,
            mms_enabled=mms_enabled,
            region=region,
            resource=resource,
            sms_enabled=sms_enabled,
            voice_enabled=voice_enabled,
        )
    ).parsed
