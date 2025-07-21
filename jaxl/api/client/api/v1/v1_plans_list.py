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
from ...models.paginated_plan_list import PaginatedPlanList
from ...models.v1_plans_list_currency import V1PlansListCurrency
from ...models.v1_plans_list_type import V1PlansListType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    currency: V1PlansListCurrency,
    disabled: Union[Unset, None, bool] = False,
    gateway: Union[Unset, None, int] = UNSET,
    item: Union[Unset, None, str] = UNSET,
    item_attributes: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    type: Union[Unset, None, V1PlansListType] = UNSET,
    usage: Union[Unset, None, float] = UNSET,
) -> Dict[str, Any]:
    url = "{}/v1/plans/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_currency = currency.value

    params["currency"] = json_currency

    params["disabled"] = disabled

    params["gateway"] = gateway

    params["item"] = item

    params["item_attributes"] = item_attributes

    params["limit"] = limit

    params["offset"] = offset

    json_type: Union[Unset, None, int] = UNSET
    if not isinstance(type, Unset):
        json_type = type.value if type else None

    params["type"] = json_type

    params["usage"] = usage

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
) -> Optional[Union[Any, PaginatedPlanList]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PaginatedPlanList.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[Any, PaginatedPlanList]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    currency: V1PlansListCurrency,
    disabled: Union[Unset, None, bool] = False,
    gateway: Union[Unset, None, int] = UNSET,
    item: Union[Unset, None, str] = UNSET,
    item_attributes: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    type: Union[Unset, None, V1PlansListType] = UNSET,
    usage: Union[Unset, None, float] = UNSET,
) -> Response[Union[Any, PaginatedPlanList]]:
    """
    Args:
        currency (V1PlansListCurrency):
        disabled (Union[Unset, None, bool]):
        gateway (Union[Unset, None, int]):
        item (Union[Unset, None, str]):
        item_attributes (Union[Unset, None, str]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        type (Union[Unset, None, V1PlansListType]):
        usage (Union[Unset, None, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PaginatedPlanList]]
    """

    kwargs = _get_kwargs(
        client=client,
        currency=currency,
        disabled=disabled,
        gateway=gateway,
        item=item,
        item_attributes=item_attributes,
        limit=limit,
        offset=offset,
        type=type,
        usage=usage,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    currency: V1PlansListCurrency,
    disabled: Union[Unset, None, bool] = False,
    gateway: Union[Unset, None, int] = UNSET,
    item: Union[Unset, None, str] = UNSET,
    item_attributes: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    type: Union[Unset, None, V1PlansListType] = UNSET,
    usage: Union[Unset, None, float] = UNSET,
) -> Optional[Union[Any, PaginatedPlanList]]:
    """
    Args:
        currency (V1PlansListCurrency):
        disabled (Union[Unset, None, bool]):
        gateway (Union[Unset, None, int]):
        item (Union[Unset, None, str]):
        item_attributes (Union[Unset, None, str]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        type (Union[Unset, None, V1PlansListType]):
        usage (Union[Unset, None, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PaginatedPlanList]]
    """

    return sync_detailed(
        client=client,
        currency=currency,
        disabled=disabled,
        gateway=gateway,
        item=item,
        item_attributes=item_attributes,
        limit=limit,
        offset=offset,
        type=type,
        usage=usage,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    currency: V1PlansListCurrency,
    disabled: Union[Unset, None, bool] = False,
    gateway: Union[Unset, None, int] = UNSET,
    item: Union[Unset, None, str] = UNSET,
    item_attributes: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    type: Union[Unset, None, V1PlansListType] = UNSET,
    usage: Union[Unset, None, float] = UNSET,
) -> Response[Union[Any, PaginatedPlanList]]:
    """
    Args:
        currency (V1PlansListCurrency):
        disabled (Union[Unset, None, bool]):
        gateway (Union[Unset, None, int]):
        item (Union[Unset, None, str]):
        item_attributes (Union[Unset, None, str]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        type (Union[Unset, None, V1PlansListType]):
        usage (Union[Unset, None, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PaginatedPlanList]]
    """

    kwargs = _get_kwargs(
        client=client,
        currency=currency,
        disabled=disabled,
        gateway=gateway,
        item=item,
        item_attributes=item_attributes,
        limit=limit,
        offset=offset,
        type=type,
        usage=usage,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    currency: V1PlansListCurrency,
    disabled: Union[Unset, None, bool] = False,
    gateway: Union[Unset, None, int] = UNSET,
    item: Union[Unset, None, str] = UNSET,
    item_attributes: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    type: Union[Unset, None, V1PlansListType] = UNSET,
    usage: Union[Unset, None, float] = UNSET,
) -> Optional[Union[Any, PaginatedPlanList]]:
    """
    Args:
        currency (V1PlansListCurrency):
        disabled (Union[Unset, None, bool]):
        gateway (Union[Unset, None, int]):
        item (Union[Unset, None, str]):
        item_attributes (Union[Unset, None, str]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        type (Union[Unset, None, V1PlansListType]):
        usage (Union[Unset, None, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PaginatedPlanList]]
    """

    return (
        await asyncio_detailed(
            client=client,
            currency=currency,
            disabled=disabled,
            gateway=gateway,
            item=item,
            item_attributes=item_attributes,
            limit=limit,
            offset=offset,
            type=type,
            usage=usage,
        )
    ).parsed
