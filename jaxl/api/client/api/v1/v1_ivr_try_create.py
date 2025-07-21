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
from ...models.ivr import IVR
from ...models.ivr_simulation_state_request import IVRSimulationStateRequest
from ...models.ivr_try_request import IVRTryRequest
from ...models.v1_ivr_try_create_lang import V1IvrTryCreateLang
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    client: AuthenticatedClient,
    json_body: IVRTryRequest,
    lang: Union[Unset, None, V1IvrTryCreateLang] = V1IvrTryCreateLang.EN,
    state: Union[Unset, None, "IVRSimulationStateRequest"] = UNSET,
) -> Dict[str, Any]:
    url = "{}/v1/ivr/{id}/try/".format(client.base_url, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_lang: Union[Unset, None, str] = UNSET
    if not isinstance(lang, Unset):
        json_lang = lang.value if lang else None

    params["lang"] = json_lang

    json_state: Union[Unset, None, Dict[str, Any]] = UNSET
    if not isinstance(state, Unset):
        json_state = state.to_dict() if state else None

    if not isinstance(json_state, Unset) and json_state is not None:
        params.update(json_state)

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[Any, IVR]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = IVR.from_dict(response.json())

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
) -> Response[Union[Any, IVR]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    json_body: IVRTryRequest,
    lang: Union[Unset, None, V1IvrTryCreateLang] = V1IvrTryCreateLang.EN,
    state: Union[Unset, None, "IVRSimulationStateRequest"] = UNSET,
) -> Response[Union[Any, IVR]]:
    """API view set for IVR Menu model.

    Args:
        id (int):
        lang (Union[Unset, None, V1IvrTryCreateLang]):  Default: V1IvrTryCreateLang.EN.
        state (Union[Unset, None, IVRSimulationStateRequest]):
        json_body (IVRTryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, IVR]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        json_body=json_body,
        lang=lang,
        state=state,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    json_body: IVRTryRequest,
    lang: Union[Unset, None, V1IvrTryCreateLang] = V1IvrTryCreateLang.EN,
    state: Union[Unset, None, "IVRSimulationStateRequest"] = UNSET,
) -> Optional[Union[Any, IVR]]:
    """API view set for IVR Menu model.

    Args:
        id (int):
        lang (Union[Unset, None, V1IvrTryCreateLang]):  Default: V1IvrTryCreateLang.EN.
        state (Union[Unset, None, IVRSimulationStateRequest]):
        json_body (IVRTryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, IVR]]
    """

    return sync_detailed(
        id=id,
        client=client,
        json_body=json_body,
        lang=lang,
        state=state,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    json_body: IVRTryRequest,
    lang: Union[Unset, None, V1IvrTryCreateLang] = V1IvrTryCreateLang.EN,
    state: Union[Unset, None, "IVRSimulationStateRequest"] = UNSET,
) -> Response[Union[Any, IVR]]:
    """API view set for IVR Menu model.

    Args:
        id (int):
        lang (Union[Unset, None, V1IvrTryCreateLang]):  Default: V1IvrTryCreateLang.EN.
        state (Union[Unset, None, IVRSimulationStateRequest]):
        json_body (IVRTryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, IVR]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        json_body=json_body,
        lang=lang,
        state=state,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    json_body: IVRTryRequest,
    lang: Union[Unset, None, V1IvrTryCreateLang] = V1IvrTryCreateLang.EN,
    state: Union[Unset, None, "IVRSimulationStateRequest"] = UNSET,
) -> Optional[Union[Any, IVR]]:
    """API view set for IVR Menu model.

    Args:
        id (int):
        lang (Union[Unset, None, V1IvrTryCreateLang]):  Default: V1IvrTryCreateLang.EN.
        state (Union[Unset, None, IVRSimulationStateRequest]):
        json_body (IVRTryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, IVR]]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            json_body=json_body,
            lang=lang,
            state=state,
        )
    ).parsed
