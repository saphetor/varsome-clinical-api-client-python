from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.capture_kit import CaptureKit
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    id: str,
    name: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/metadata/assays/{id}/".format(client.base_url, id=id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "name": name,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[CaptureKit]:
    if response.status_code == 200:
        response_200 = CaptureKit.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[CaptureKit]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    id: str,
    name: Union[Unset, str] = UNSET,
) -> Response[CaptureKit]:
    kwargs = _get_kwargs(
        client=client,
        id=id,
        name=name,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    id: str,
    name: Union[Unset, str] = UNSET,
) -> Optional[CaptureKit]:
    """Provides information about available *Assays* to be assigned to new analyses"""

    return sync_detailed(
        client=client,
        id=id,
        name=name,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    id: str,
    name: Union[Unset, str] = UNSET,
) -> Response[CaptureKit]:
    kwargs = _get_kwargs(
        client=client,
        id=id,
        name=name,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    id: str,
    name: Union[Unset, str] = UNSET,
) -> Optional[CaptureKit]:
    """Provides information about available *Assays* to be assigned to new analyses"""

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            name=name,
        )
    ).parsed
