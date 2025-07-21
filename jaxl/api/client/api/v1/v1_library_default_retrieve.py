"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.library_response import LibraryResponse
from ...models.v1_library_default_retrieve_scenario import (
    V1LibraryDefaultRetrieveScenario,
)
from ...types import UNSET, Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    scenario: V1LibraryDefaultRetrieveScenario,
) -> Dict[str, Any]:
    url = "{}/v1/library/default/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_scenario = scenario.value

    params["scenario"] = json_scenario

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
) -> Optional[LibraryResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = LibraryResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[LibraryResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    scenario: V1LibraryDefaultRetrieveScenario,
) -> Response[LibraryResponse]:
    """
    Args:
        scenario (V1LibraryDefaultRetrieveScenario):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LibraryResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        scenario=scenario,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    scenario: V1LibraryDefaultRetrieveScenario,
) -> Optional[LibraryResponse]:
    """
    Args:
        scenario (V1LibraryDefaultRetrieveScenario):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LibraryResponse]
    """

    return sync_detailed(
        client=client,
        scenario=scenario,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    scenario: V1LibraryDefaultRetrieveScenario,
) -> Response[LibraryResponse]:
    """
    Args:
        scenario (V1LibraryDefaultRetrieveScenario):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LibraryResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        scenario=scenario,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    scenario: V1LibraryDefaultRetrieveScenario,
) -> Optional[LibraryResponse]:
    """
    Args:
        scenario (V1LibraryDefaultRetrieveScenario):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LibraryResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            scenario=scenario,
        )
    ).parsed
