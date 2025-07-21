"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.key_info import KeyInfo
from ...models.line_chart_response import LineChartResponse
from ...models.pie_chart_response import PieChartResponse
from ...models.table_chart_response import TableChartResponse
from ...models.v1_analytics_data_retrieve_date_range import (
    V1AnalyticsDataRetrieveDateRange,
)
from ...models.v1_analytics_data_retrieve_resolution import (
    V1AnalyticsDataRetrieveResolution,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    date_range: Union[
        Unset, None, V1AnalyticsDataRetrieveDateRange
    ] = V1AnalyticsDataRetrieveDateRange.TODAY,
    eid: Union[Unset, None, List[int]] = UNSET,
    resolution: Union[Unset, None, V1AnalyticsDataRetrieveResolution] = UNSET,
    slug: str,
    tid: Union[Unset, None, List[int]] = UNSET,
) -> Dict[str, Any]:
    url = "{}/v1/analytics/data/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_date_range: Union[Unset, None, str] = UNSET
    if not isinstance(date_range, Unset):
        json_date_range = date_range.value if date_range else None

    params["date_range"] = json_date_range

    json_eid: Union[Unset, None, List[int]] = UNSET
    if not isinstance(eid, Unset):
        if eid is None:
            json_eid = None
        else:
            json_eid = eid

    params["eid"] = json_eid

    json_resolution: Union[Unset, None, str] = UNSET
    if not isinstance(resolution, Unset):
        json_resolution = resolution.value if resolution else None

    params["resolution"] = json_resolution

    params["slug"] = slug

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[
    Union[
        Any,
        Union["KeyInfo", "LineChartResponse", "PieChartResponse", "TableChartResponse"],
    ]
]:
    if response.status_code == HTTPStatus.OK:

        def _parse_response_200(
            data: object,
        ) -> Union[
            "KeyInfo", "LineChartResponse", "PieChartResponse", "TableChartResponse"
        ]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_chart_response_type_0 = LineChartResponse.from_dict(
                    data
                )

                return componentsschemas_chart_response_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_chart_response_type_1 = PieChartResponse.from_dict(
                    data
                )

                return componentsschemas_chart_response_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_chart_response_type_2 = TableChartResponse.from_dict(
                    data
                )

                return componentsschemas_chart_response_type_2
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_chart_response_type_3 = KeyInfo.from_dict(data)

            return componentsschemas_chart_response_type_3

        response_200 = _parse_response_200(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[
    Union[
        Any,
        Union["KeyInfo", "LineChartResponse", "PieChartResponse", "TableChartResponse"],
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    date_range: Union[
        Unset, None, V1AnalyticsDataRetrieveDateRange
    ] = V1AnalyticsDataRetrieveDateRange.TODAY,
    eid: Union[Unset, None, List[int]] = UNSET,
    resolution: Union[Unset, None, V1AnalyticsDataRetrieveResolution] = UNSET,
    slug: str,
    tid: Union[Unset, None, List[int]] = UNSET,
) -> Response[
    Union[
        Any,
        Union["KeyInfo", "LineChartResponse", "PieChartResponse", "TableChartResponse"],
    ]
]:
    """
    Args:
        date_range (Union[Unset, None, V1AnalyticsDataRetrieveDateRange]):  Default:
            V1AnalyticsDataRetrieveDateRange.TODAY.
        eid (Union[Unset, None, List[int]]):
        resolution (Union[Unset, None, V1AnalyticsDataRetrieveResolution]):
        slug (str):
        tid (Union[Unset, None, List[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Union['KeyInfo', 'LineChartResponse', 'PieChartResponse', 'TableChartResponse']]]
    """

    kwargs = _get_kwargs(
        client=client,
        date_range=date_range,
        eid=eid,
        resolution=resolution,
        slug=slug,
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
    date_range: Union[
        Unset, None, V1AnalyticsDataRetrieveDateRange
    ] = V1AnalyticsDataRetrieveDateRange.TODAY,
    eid: Union[Unset, None, List[int]] = UNSET,
    resolution: Union[Unset, None, V1AnalyticsDataRetrieveResolution] = UNSET,
    slug: str,
    tid: Union[Unset, None, List[int]] = UNSET,
) -> Optional[
    Union[
        Any,
        Union["KeyInfo", "LineChartResponse", "PieChartResponse", "TableChartResponse"],
    ]
]:
    """
    Args:
        date_range (Union[Unset, None, V1AnalyticsDataRetrieveDateRange]):  Default:
            V1AnalyticsDataRetrieveDateRange.TODAY.
        eid (Union[Unset, None, List[int]]):
        resolution (Union[Unset, None, V1AnalyticsDataRetrieveResolution]):
        slug (str):
        tid (Union[Unset, None, List[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Union['KeyInfo', 'LineChartResponse', 'PieChartResponse', 'TableChartResponse']]]
    """

    return sync_detailed(
        client=client,
        date_range=date_range,
        eid=eid,
        resolution=resolution,
        slug=slug,
        tid=tid,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    date_range: Union[
        Unset, None, V1AnalyticsDataRetrieveDateRange
    ] = V1AnalyticsDataRetrieveDateRange.TODAY,
    eid: Union[Unset, None, List[int]] = UNSET,
    resolution: Union[Unset, None, V1AnalyticsDataRetrieveResolution] = UNSET,
    slug: str,
    tid: Union[Unset, None, List[int]] = UNSET,
) -> Response[
    Union[
        Any,
        Union["KeyInfo", "LineChartResponse", "PieChartResponse", "TableChartResponse"],
    ]
]:
    """
    Args:
        date_range (Union[Unset, None, V1AnalyticsDataRetrieveDateRange]):  Default:
            V1AnalyticsDataRetrieveDateRange.TODAY.
        eid (Union[Unset, None, List[int]]):
        resolution (Union[Unset, None, V1AnalyticsDataRetrieveResolution]):
        slug (str):
        tid (Union[Unset, None, List[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Union['KeyInfo', 'LineChartResponse', 'PieChartResponse', 'TableChartResponse']]]
    """

    kwargs = _get_kwargs(
        client=client,
        date_range=date_range,
        eid=eid,
        resolution=resolution,
        slug=slug,
        tid=tid,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    date_range: Union[
        Unset, None, V1AnalyticsDataRetrieveDateRange
    ] = V1AnalyticsDataRetrieveDateRange.TODAY,
    eid: Union[Unset, None, List[int]] = UNSET,
    resolution: Union[Unset, None, V1AnalyticsDataRetrieveResolution] = UNSET,
    slug: str,
    tid: Union[Unset, None, List[int]] = UNSET,
) -> Optional[
    Union[
        Any,
        Union["KeyInfo", "LineChartResponse", "PieChartResponse", "TableChartResponse"],
    ]
]:
    """
    Args:
        date_range (Union[Unset, None, V1AnalyticsDataRetrieveDateRange]):  Default:
            V1AnalyticsDataRetrieveDateRange.TODAY.
        eid (Union[Unset, None, List[int]]):
        resolution (Union[Unset, None, V1AnalyticsDataRetrieveResolution]):
        slug (str):
        tid (Union[Unset, None, List[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Union['KeyInfo', 'LineChartResponse', 'PieChartResponse', 'TableChartResponse']]]
    """

    return (
        await asyncio_detailed(
            client=client,
            date_range=date_range,
            eid=eid,
            resolution=resolution,
            slug=slug,
            tid=tid,
        )
    ).parsed
