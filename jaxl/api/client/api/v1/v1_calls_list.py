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
from ...models.paginated_call_list import PaginatedCallList
from ...models.v1_calls_list_direction import V1CallsListDirection
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    aid: Union[Unset, None, List[int]] = UNSET,
    bot: Union[Unset, None, bool] = UNSET,
    currency: int,
    direction: Union[Unset, None, V1CallsListDirection] = UNSET,
    duration: Union[Unset, None, int] = UNSET,
    from_number: Union[Unset, None, str] = UNSET,
    ivr: Union[Unset, None, bool] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    missed: Union[Unset, None, bool] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    other_numbers: Union[Unset, None, str] = UNSET,
    our_numbers: Union[Unset, None, str] = UNSET,
    recording: Union[Unset, None, bool] = UNSET,
    tag_operator: Union[Unset, None, bool] = UNSET,
    tid: Union[Unset, None, List[int]] = UNSET,
    to_number: Union[Unset, None, str] = UNSET,
    voicemail: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    url = "{}/v1/calls/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_aid: Union[Unset, None, List[int]] = UNSET
    if not isinstance(aid, Unset):
        if aid is None:
            json_aid = None
        else:
            json_aid = aid

    params["aid"] = json_aid

    params["bot"] = bot

    params["currency"] = currency

    json_direction: Union[Unset, None, int] = UNSET
    if not isinstance(direction, Unset):
        json_direction = direction.value if direction else None

    params["direction"] = json_direction

    params["duration"] = duration

    params["from_number"] = from_number

    params["ivr"] = ivr

    params["limit"] = limit

    params["missed"] = missed

    params["offset"] = offset

    params["other_numbers"] = other_numbers

    params["our_numbers"] = our_numbers

    params["recording"] = recording

    params["tag_operator"] = tag_operator

    json_tid: Union[Unset, None, List[int]] = UNSET
    if not isinstance(tid, Unset):
        if tid is None:
            json_tid = None
        else:
            json_tid = tid

    params["tid"] = json_tid

    params["to_number"] = to_number

    params["voicemail"] = voicemail

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
) -> Optional[PaginatedCallList]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PaginatedCallList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[PaginatedCallList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    aid: Union[Unset, None, List[int]] = UNSET,
    bot: Union[Unset, None, bool] = UNSET,
    currency: int,
    direction: Union[Unset, None, V1CallsListDirection] = UNSET,
    duration: Union[Unset, None, int] = UNSET,
    from_number: Union[Unset, None, str] = UNSET,
    ivr: Union[Unset, None, bool] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    missed: Union[Unset, None, bool] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    other_numbers: Union[Unset, None, str] = UNSET,
    our_numbers: Union[Unset, None, str] = UNSET,
    recording: Union[Unset, None, bool] = UNSET,
    tag_operator: Union[Unset, None, bool] = UNSET,
    tid: Union[Unset, None, List[int]] = UNSET,
    to_number: Union[Unset, None, str] = UNSET,
    voicemail: Union[Unset, None, bool] = UNSET,
) -> Response[PaginatedCallList]:
    """API view set for Call model.

    Args:
        aid (Union[Unset, None, List[int]]):
        bot (Union[Unset, None, bool]):
        currency (int):
        direction (Union[Unset, None, V1CallsListDirection]):
        duration (Union[Unset, None, int]):
        from_number (Union[Unset, None, str]):
        ivr (Union[Unset, None, bool]):
        limit (Union[Unset, None, int]):
        missed (Union[Unset, None, bool]):
        offset (Union[Unset, None, int]):
        other_numbers (Union[Unset, None, str]):
        our_numbers (Union[Unset, None, str]):
        recording (Union[Unset, None, bool]):
        tag_operator (Union[Unset, None, bool]):
        tid (Union[Unset, None, List[int]]):
        to_number (Union[Unset, None, str]):
        voicemail (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedCallList]
    """

    kwargs = _get_kwargs(
        client=client,
        aid=aid,
        bot=bot,
        currency=currency,
        direction=direction,
        duration=duration,
        from_number=from_number,
        ivr=ivr,
        limit=limit,
        missed=missed,
        offset=offset,
        other_numbers=other_numbers,
        our_numbers=our_numbers,
        recording=recording,
        tag_operator=tag_operator,
        tid=tid,
        to_number=to_number,
        voicemail=voicemail,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    aid: Union[Unset, None, List[int]] = UNSET,
    bot: Union[Unset, None, bool] = UNSET,
    currency: int,
    direction: Union[Unset, None, V1CallsListDirection] = UNSET,
    duration: Union[Unset, None, int] = UNSET,
    from_number: Union[Unset, None, str] = UNSET,
    ivr: Union[Unset, None, bool] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    missed: Union[Unset, None, bool] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    other_numbers: Union[Unset, None, str] = UNSET,
    our_numbers: Union[Unset, None, str] = UNSET,
    recording: Union[Unset, None, bool] = UNSET,
    tag_operator: Union[Unset, None, bool] = UNSET,
    tid: Union[Unset, None, List[int]] = UNSET,
    to_number: Union[Unset, None, str] = UNSET,
    voicemail: Union[Unset, None, bool] = UNSET,
) -> Optional[PaginatedCallList]:
    """API view set for Call model.

    Args:
        aid (Union[Unset, None, List[int]]):
        bot (Union[Unset, None, bool]):
        currency (int):
        direction (Union[Unset, None, V1CallsListDirection]):
        duration (Union[Unset, None, int]):
        from_number (Union[Unset, None, str]):
        ivr (Union[Unset, None, bool]):
        limit (Union[Unset, None, int]):
        missed (Union[Unset, None, bool]):
        offset (Union[Unset, None, int]):
        other_numbers (Union[Unset, None, str]):
        our_numbers (Union[Unset, None, str]):
        recording (Union[Unset, None, bool]):
        tag_operator (Union[Unset, None, bool]):
        tid (Union[Unset, None, List[int]]):
        to_number (Union[Unset, None, str]):
        voicemail (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedCallList]
    """

    return sync_detailed(
        client=client,
        aid=aid,
        bot=bot,
        currency=currency,
        direction=direction,
        duration=duration,
        from_number=from_number,
        ivr=ivr,
        limit=limit,
        missed=missed,
        offset=offset,
        other_numbers=other_numbers,
        our_numbers=our_numbers,
        recording=recording,
        tag_operator=tag_operator,
        tid=tid,
        to_number=to_number,
        voicemail=voicemail,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    aid: Union[Unset, None, List[int]] = UNSET,
    bot: Union[Unset, None, bool] = UNSET,
    currency: int,
    direction: Union[Unset, None, V1CallsListDirection] = UNSET,
    duration: Union[Unset, None, int] = UNSET,
    from_number: Union[Unset, None, str] = UNSET,
    ivr: Union[Unset, None, bool] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    missed: Union[Unset, None, bool] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    other_numbers: Union[Unset, None, str] = UNSET,
    our_numbers: Union[Unset, None, str] = UNSET,
    recording: Union[Unset, None, bool] = UNSET,
    tag_operator: Union[Unset, None, bool] = UNSET,
    tid: Union[Unset, None, List[int]] = UNSET,
    to_number: Union[Unset, None, str] = UNSET,
    voicemail: Union[Unset, None, bool] = UNSET,
) -> Response[PaginatedCallList]:
    """API view set for Call model.

    Args:
        aid (Union[Unset, None, List[int]]):
        bot (Union[Unset, None, bool]):
        currency (int):
        direction (Union[Unset, None, V1CallsListDirection]):
        duration (Union[Unset, None, int]):
        from_number (Union[Unset, None, str]):
        ivr (Union[Unset, None, bool]):
        limit (Union[Unset, None, int]):
        missed (Union[Unset, None, bool]):
        offset (Union[Unset, None, int]):
        other_numbers (Union[Unset, None, str]):
        our_numbers (Union[Unset, None, str]):
        recording (Union[Unset, None, bool]):
        tag_operator (Union[Unset, None, bool]):
        tid (Union[Unset, None, List[int]]):
        to_number (Union[Unset, None, str]):
        voicemail (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedCallList]
    """

    kwargs = _get_kwargs(
        client=client,
        aid=aid,
        bot=bot,
        currency=currency,
        direction=direction,
        duration=duration,
        from_number=from_number,
        ivr=ivr,
        limit=limit,
        missed=missed,
        offset=offset,
        other_numbers=other_numbers,
        our_numbers=our_numbers,
        recording=recording,
        tag_operator=tag_operator,
        tid=tid,
        to_number=to_number,
        voicemail=voicemail,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    aid: Union[Unset, None, List[int]] = UNSET,
    bot: Union[Unset, None, bool] = UNSET,
    currency: int,
    direction: Union[Unset, None, V1CallsListDirection] = UNSET,
    duration: Union[Unset, None, int] = UNSET,
    from_number: Union[Unset, None, str] = UNSET,
    ivr: Union[Unset, None, bool] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    missed: Union[Unset, None, bool] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    other_numbers: Union[Unset, None, str] = UNSET,
    our_numbers: Union[Unset, None, str] = UNSET,
    recording: Union[Unset, None, bool] = UNSET,
    tag_operator: Union[Unset, None, bool] = UNSET,
    tid: Union[Unset, None, List[int]] = UNSET,
    to_number: Union[Unset, None, str] = UNSET,
    voicemail: Union[Unset, None, bool] = UNSET,
) -> Optional[PaginatedCallList]:
    """API view set for Call model.

    Args:
        aid (Union[Unset, None, List[int]]):
        bot (Union[Unset, None, bool]):
        currency (int):
        direction (Union[Unset, None, V1CallsListDirection]):
        duration (Union[Unset, None, int]):
        from_number (Union[Unset, None, str]):
        ivr (Union[Unset, None, bool]):
        limit (Union[Unset, None, int]):
        missed (Union[Unset, None, bool]):
        offset (Union[Unset, None, int]):
        other_numbers (Union[Unset, None, str]):
        our_numbers (Union[Unset, None, str]):
        recording (Union[Unset, None, bool]):
        tag_operator (Union[Unset, None, bool]):
        tid (Union[Unset, None, List[int]]):
        to_number (Union[Unset, None, str]):
        voicemail (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedCallList]
    """

    return (
        await asyncio_detailed(
            client=client,
            aid=aid,
            bot=bot,
            currency=currency,
            direction=direction,
            duration=duration,
            from_number=from_number,
            ivr=ivr,
            limit=limit,
            missed=missed,
            offset=offset,
            other_numbers=other_numbers,
            our_numbers=our_numbers,
            recording=recording,
            tag_operator=tag_operator,
            tid=tid,
            to_number=to_number,
            voicemail=voicemail,
        )
    ).parsed
