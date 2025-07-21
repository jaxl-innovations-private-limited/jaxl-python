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
from ...models.paginated_plan_country_number_types_list import (
    PaginatedPlanCountryNumberTypesList,
)
from ...models.v1_plans_resources_list_type import V1PlansResourcesListType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    type: Union[Unset, None, V1PlansResourcesListType] = UNSET,
) -> Dict[str, Any]:
    url = "{}/v1/plans/resources/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["limit"] = limit

    params["offset"] = offset

    json_type: Union[Unset, None, int] = UNSET
    if not isinstance(type, Unset):
        json_type = type.value if type else None

    params["type"] = json_type

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
) -> Optional[Union[Any, PaginatedPlanCountryNumberTypesList]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PaginatedPlanCountryNumberTypesList.from_dict(response.json())

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
) -> Response[Union[Any, PaginatedPlanCountryNumberTypesList]]:
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
    offset: Union[Unset, None, int] = UNSET,
    type: Union[Unset, None, V1PlansResourcesListType] = UNSET,
) -> Response[Union[Any, PaginatedPlanCountryNumberTypesList]]:
    """This API will return a list of iso_country_code and number_types for each
    public, enabled and released phone number plan.

    Args:
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        type (Union[Unset, None, V1PlansResourcesListType]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PaginatedPlanCountryNumberTypesList]]
    """

    kwargs = _get_kwargs(
        client=client,
        limit=limit,
        offset=offset,
        type=type,
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
    offset: Union[Unset, None, int] = UNSET,
    type: Union[Unset, None, V1PlansResourcesListType] = UNSET,
) -> Optional[Union[Any, PaginatedPlanCountryNumberTypesList]]:
    """This API will return a list of iso_country_code and number_types for each
    public, enabled and released phone number plan.

    Args:
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        type (Union[Unset, None, V1PlansResourcesListType]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PaginatedPlanCountryNumberTypesList]]
    """

    return sync_detailed(
        client=client,
        limit=limit,
        offset=offset,
        type=type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    type: Union[Unset, None, V1PlansResourcesListType] = UNSET,
) -> Response[Union[Any, PaginatedPlanCountryNumberTypesList]]:
    """This API will return a list of iso_country_code and number_types for each
    public, enabled and released phone number plan.

    Args:
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        type (Union[Unset, None, V1PlansResourcesListType]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PaginatedPlanCountryNumberTypesList]]
    """

    kwargs = _get_kwargs(
        client=client,
        limit=limit,
        offset=offset,
        type=type,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    type: Union[Unset, None, V1PlansResourcesListType] = UNSET,
) -> Optional[Union[Any, PaginatedPlanCountryNumberTypesList]]:
    """This API will return a list of iso_country_code and number_types for each
    public, enabled and released phone number plan.

    Args:
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        type (Union[Unset, None, V1PlansResourcesListType]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PaginatedPlanCountryNumberTypesList]]
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            offset=offset,
            type=type,
        )
    ).parsed
