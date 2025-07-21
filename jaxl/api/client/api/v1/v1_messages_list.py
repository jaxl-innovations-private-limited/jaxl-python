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
from ...models.paginated_dh_message_list import PaginatedDHMessageList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, None, int] = UNSET,
    mid: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    okey: Union[Unset, None, List[str]] = UNSET,
) -> Dict[str, Any]:
    url = "{}/v1/messages/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["limit"] = limit

    params["mid"] = mid

    params["offset"] = offset

    json_okey: Union[Unset, None, List[str]] = UNSET
    if not isinstance(okey, Unset):
        if okey is None:
            json_okey = None
        else:
            json_okey = okey

    params["okey"] = json_okey

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
) -> Optional[PaginatedDHMessageList]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PaginatedDHMessageList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[PaginatedDHMessageList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, None, int] = UNSET,
    mid: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    okey: Union[Unset, None, List[str]] = UNSET,
) -> Response[PaginatedDHMessageList]:
    """API view set for Network message related model.

    Args:
        limit (Union[Unset, None, int]):
        mid (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        okey (Union[Unset, None, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedDHMessageList]
    """

    kwargs = _get_kwargs(
        client=client,
        limit=limit,
        mid=mid,
        offset=offset,
        okey=okey,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, None, int] = UNSET,
    mid: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    okey: Union[Unset, None, List[str]] = UNSET,
) -> Optional[PaginatedDHMessageList]:
    """API view set for Network message related model.

    Args:
        limit (Union[Unset, None, int]):
        mid (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        okey (Union[Unset, None, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedDHMessageList]
    """

    return sync_detailed(
        client=client,
        limit=limit,
        mid=mid,
        offset=offset,
        okey=okey,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, None, int] = UNSET,
    mid: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    okey: Union[Unset, None, List[str]] = UNSET,
) -> Response[PaginatedDHMessageList]:
    """API view set for Network message related model.

    Args:
        limit (Union[Unset, None, int]):
        mid (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        okey (Union[Unset, None, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedDHMessageList]
    """

    kwargs = _get_kwargs(
        client=client,
        limit=limit,
        mid=mid,
        offset=offset,
        okey=okey,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, None, int] = UNSET,
    mid: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    okey: Union[Unset, None, List[str]] = UNSET,
) -> Optional[PaginatedDHMessageList]:
    """API view set for Network message related model.

    Args:
        limit (Union[Unset, None, int]):
        mid (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        okey (Union[Unset, None, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedDHMessageList]
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            mid=mid,
            offset=offset,
            okey=okey,
        )
    ).parsed
