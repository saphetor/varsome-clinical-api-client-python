from typing import Any, Dict, Union

import httpx

from ...client import Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    id: str,
    name: Union[Unset, str] = UNSET,
    email: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
    is_usable: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/sample-files/{id}/".format(client.base_url, id=id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "name": name,
        "email": email,
        "status": status,
        "is_usable": is_usable,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _build_response(*, response: httpx.Response) -> Response[None]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    *,
    client: Client,
    id: str,
    name: Union[Unset, str] = UNSET,
    email: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
    is_usable: Union[Unset, str] = UNSET,
) -> Response[None]:
    kwargs = _get_kwargs(
        client=client,
        id=id,
        name=name,
        email=email,
        status=status,
        is_usable=is_usable,
    )

    response = httpx.delete(
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    *,
    client: Client,
    id: str,
    name: Union[Unset, str] = UNSET,
    email: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
    is_usable: Union[Unset, str] = UNSET,
) -> Response[None]:
    kwargs = _get_kwargs(
        client=client,
        id=id,
        name=name,
        email=email,
        status=status,
        is_usable=is_usable,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.delete(**kwargs)

    return _build_response(response=response)
