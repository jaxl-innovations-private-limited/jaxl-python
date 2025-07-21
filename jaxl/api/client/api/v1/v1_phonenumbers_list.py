"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_phone_number_list import PaginatedPhoneNumberList
from ...models.v1_phonenumbers_list_additional_status_item import (
    V1PhonenumbersListAdditionalStatusItem,
)
from ...models.v1_phonenumbers_list_provider import V1PhonenumbersListProvider
from ...models.v1_phonenumbers_list_status import V1PhonenumbersListStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    additional_status: Union[
        Unset, None, List[V1PhonenumbersListAdditionalStatusItem]
    ] = UNSET,
    ivr: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    provider: Union[Unset, None, V1PhonenumbersListProvider] = UNSET,
    status: Union[Unset, None, V1PhonenumbersListStatus] = UNSET,
    uid: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/v1/phonenumbers/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_additional_status: Union[Unset, None, List[str]] = UNSET
    if not isinstance(additional_status, Unset):
        if additional_status is None:
            json_additional_status = None
        else:
            json_additional_status = []
            for additional_status_item_data in additional_status:
                additional_status_item = additional_status_item_data.value

                json_additional_status.append(additional_status_item)

    params["additional_status"] = json_additional_status

    params["ivr"] = ivr

    params["limit"] = limit

    params["offset"] = offset

    json_provider: Union[Unset, None, int] = UNSET
    if not isinstance(provider, Unset):
        json_provider = provider.value if provider else None

    params["provider"] = json_provider

    json_status: Union[Unset, None, str] = UNSET
    if not isinstance(status, Unset):
        json_status = status.value if status else None

    params["status"] = json_status

    params["uid"] = uid

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
) -> Optional[PaginatedPhoneNumberList]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PaginatedPhoneNumberList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[PaginatedPhoneNumberList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    additional_status: Union[
        Unset, None, List[V1PhonenumbersListAdditionalStatusItem]
    ] = UNSET,
    ivr: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    provider: Union[Unset, None, V1PhonenumbersListProvider] = UNSET,
    status: Union[Unset, None, V1PhonenumbersListStatus] = UNSET,
    uid: Union[Unset, None, str] = UNSET,
) -> Response[PaginatedPhoneNumberList]:
    """API view set for PhoneNumber model.

    Args:
        additional_status (Union[Unset, None, List[V1PhonenumbersListAdditionalStatusItem]]):
        ivr (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        provider (Union[Unset, None, V1PhonenumbersListProvider]):
        status (Union[Unset, None, V1PhonenumbersListStatus]):
        uid (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedPhoneNumberList]
    """

    kwargs = _get_kwargs(
        client=client,
        additional_status=additional_status,
        ivr=ivr,
        limit=limit,
        offset=offset,
        provider=provider,
        status=status,
        uid=uid,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    additional_status: Union[
        Unset, None, List[V1PhonenumbersListAdditionalStatusItem]
    ] = UNSET,
    ivr: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    provider: Union[Unset, None, V1PhonenumbersListProvider] = UNSET,
    status: Union[Unset, None, V1PhonenumbersListStatus] = UNSET,
    uid: Union[Unset, None, str] = UNSET,
) -> Optional[PaginatedPhoneNumberList]:
    """API view set for PhoneNumber model.

    Args:
        additional_status (Union[Unset, None, List[V1PhonenumbersListAdditionalStatusItem]]):
        ivr (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        provider (Union[Unset, None, V1PhonenumbersListProvider]):
        status (Union[Unset, None, V1PhonenumbersListStatus]):
        uid (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedPhoneNumberList]
    """

    return sync_detailed(
        client=client,
        additional_status=additional_status,
        ivr=ivr,
        limit=limit,
        offset=offset,
        provider=provider,
        status=status,
        uid=uid,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    additional_status: Union[
        Unset, None, List[V1PhonenumbersListAdditionalStatusItem]
    ] = UNSET,
    ivr: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    provider: Union[Unset, None, V1PhonenumbersListProvider] = UNSET,
    status: Union[Unset, None, V1PhonenumbersListStatus] = UNSET,
    uid: Union[Unset, None, str] = UNSET,
) -> Response[PaginatedPhoneNumberList]:
    """API view set for PhoneNumber model.

    Args:
        additional_status (Union[Unset, None, List[V1PhonenumbersListAdditionalStatusItem]]):
        ivr (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        provider (Union[Unset, None, V1PhonenumbersListProvider]):
        status (Union[Unset, None, V1PhonenumbersListStatus]):
        uid (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedPhoneNumberList]
    """

    kwargs = _get_kwargs(
        client=client,
        additional_status=additional_status,
        ivr=ivr,
        limit=limit,
        offset=offset,
        provider=provider,
        status=status,
        uid=uid,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    additional_status: Union[
        Unset, None, List[V1PhonenumbersListAdditionalStatusItem]
    ] = UNSET,
    ivr: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    provider: Union[Unset, None, V1PhonenumbersListProvider] = UNSET,
    status: Union[Unset, None, V1PhonenumbersListStatus] = UNSET,
    uid: Union[Unset, None, str] = UNSET,
) -> Optional[PaginatedPhoneNumberList]:
    """API view set for PhoneNumber model.

    Args:
        additional_status (Union[Unset, None, List[V1PhonenumbersListAdditionalStatusItem]]):
        ivr (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        provider (Union[Unset, None, V1PhonenumbersListProvider]):
        status (Union[Unset, None, V1PhonenumbersListStatus]):
        uid (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedPhoneNumberList]
    """

    return (
        await asyncio_detailed(
            client=client,
            additional_status=additional_status,
            ivr=ivr,
            limit=limit,
            offset=offset,
            provider=provider,
            status=status,
            uid=uid,
        )
    ).parsed
