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
from ...models.paginated_analytics_slug_response_list import (
    PaginatedAnalyticsSlugResponseList,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    eid: Union[Unset, None, List[int]] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    tid: Union[Unset, None, List[int]] = UNSET,
) -> Dict[str, Any]:
    url = "{}/v1/analytics/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_eid: Union[Unset, None, List[int]] = UNSET
    if not isinstance(eid, Unset):
        if eid is None:
            json_eid = None
        else:
            json_eid = eid

    params["eid"] = json_eid

    params["limit"] = limit

    params["offset"] = offset

    json_tid: Union[Unset, None, List[int]] = UNSET
    if not isinstance(tid, Unset):
        if tid is None:
            json_tid = None
        else:
            json_tid = tid

    params["tid"] = json_tid

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
) -> Optional[PaginatedAnalyticsSlugResponseList]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PaginatedAnalyticsSlugResponseList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[PaginatedAnalyticsSlugResponseList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    eid: Union[Unset, None, List[int]] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    tid: Union[Unset, None, List[int]] = UNSET,
) -> Response[PaginatedAnalyticsSlugResponseList]:
    """
    Args:
        eid (Union[Unset, None, List[int]]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        tid (Union[Unset, None, List[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedAnalyticsSlugResponseList]
    """

    kwargs = _get_kwargs(
        client=client,
        eid=eid,
        limit=limit,
        offset=offset,
        tid=tid,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    eid: Union[Unset, None, List[int]] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    tid: Union[Unset, None, List[int]] = UNSET,
) -> Optional[PaginatedAnalyticsSlugResponseList]:
    """
    Args:
        eid (Union[Unset, None, List[int]]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        tid (Union[Unset, None, List[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedAnalyticsSlugResponseList]
    """

    return sync_detailed(
        client=client,
        eid=eid,
        limit=limit,
        offset=offset,
        tid=tid,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    eid: Union[Unset, None, List[int]] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    tid: Union[Unset, None, List[int]] = UNSET,
) -> Response[PaginatedAnalyticsSlugResponseList]:
    """
    Args:
        eid (Union[Unset, None, List[int]]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        tid (Union[Unset, None, List[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedAnalyticsSlugResponseList]
    """

    kwargs = _get_kwargs(
        client=client,
        eid=eid,
        limit=limit,
        offset=offset,
        tid=tid,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    eid: Union[Unset, None, List[int]] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    tid: Union[Unset, None, List[int]] = UNSET,
) -> Optional[PaginatedAnalyticsSlugResponseList]:
    """
    Args:
        eid (Union[Unset, None, List[int]]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        tid (Union[Unset, None, List[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedAnalyticsSlugResponseList]
    """

    return (
        await asyncio_detailed(
            client=client,
            eid=eid,
            limit=limit,
            offset=offset,
            tid=tid,
        )
    ).parsed
