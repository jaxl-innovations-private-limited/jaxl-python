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
from ...models.v1_calls_report_retrieve_date_range import V1CallsReportRetrieveDateRange
from ...models.v1_calls_report_retrieve_fields_item import (
    V1CallsReportRetrieveFieldsItem,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    date_range: Union[
        Unset, None, V1CallsReportRetrieveDateRange
    ] = V1CallsReportRetrieveDateRange.TODAY,
    eid: Union[Unset, None, List[int]] = UNSET,
    fields: Union[Unset, None, List[V1CallsReportRetrieveFieldsItem]] = UNSET,
    tid: Union[Unset, None, List[int]] = UNSET,
) -> Dict[str, Any]:
    url = "{}/v1/calls/report/".format(client.base_url)

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

    json_fields: Union[Unset, None, List[str]] = UNSET
    if not isinstance(fields, Unset):
        if fields is None:
            json_fields = None
        else:
            json_fields = []
            for fields_item_data in fields:
                fields_item = fields_item_data.value

                json_fields.append(fields_item)

    params["fields"] = json_fields

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.BAD_REQUEST:
        return None
    if response.status_code == HTTPStatus.OK:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Any]:
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
        Unset, None, V1CallsReportRetrieveDateRange
    ] = V1CallsReportRetrieveDateRange.TODAY,
    eid: Union[Unset, None, List[int]] = UNSET,
    fields: Union[Unset, None, List[V1CallsReportRetrieveFieldsItem]] = UNSET,
    tid: Union[Unset, None, List[int]] = UNSET,
) -> Response[Any]:
    """API view set for Call model.

    Args:
        date_range (Union[Unset, None, V1CallsReportRetrieveDateRange]):  Default:
            V1CallsReportRetrieveDateRange.TODAY.
        eid (Union[Unset, None, List[int]]):
        fields (Union[Unset, None, List[V1CallsReportRetrieveFieldsItem]]):
        tid (Union[Unset, None, List[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        date_range=date_range,
        eid=eid,
        fields=fields,
        tid=tid,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    date_range: Union[
        Unset, None, V1CallsReportRetrieveDateRange
    ] = V1CallsReportRetrieveDateRange.TODAY,
    eid: Union[Unset, None, List[int]] = UNSET,
    fields: Union[Unset, None, List[V1CallsReportRetrieveFieldsItem]] = UNSET,
    tid: Union[Unset, None, List[int]] = UNSET,
) -> Response[Any]:
    """API view set for Call model.

    Args:
        date_range (Union[Unset, None, V1CallsReportRetrieveDateRange]):  Default:
            V1CallsReportRetrieveDateRange.TODAY.
        eid (Union[Unset, None, List[int]]):
        fields (Union[Unset, None, List[V1CallsReportRetrieveFieldsItem]]):
        tid (Union[Unset, None, List[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        date_range=date_range,
        eid=eid,
        fields=fields,
        tid=tid,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)
