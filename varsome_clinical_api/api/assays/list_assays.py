from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.assay_model import AssayModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/metadata/assays/".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "page": page,
        "page_size": page_size,
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


def _parse_response(*, response: httpx.Response) -> Optional[AssayModel]:
    if response.status_code == 200:
        response_200 = AssayModel.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[AssayModel]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
) -> Response[AssayModel]:
    kwargs = _get_kwargs(
        client=client,
        page=page,
        page_size=page_size,
        name=name,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
) -> Optional[AssayModel]:
    """Provides information about available *Assays* to be assigned to new analyses"""

    return sync_detailed(
        client=client,
        page=page,
        page_size=page_size,
        name=name,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
) -> Response[AssayModel]:
    kwargs = _get_kwargs(
        client=client,
        page=page,
        page_size=page_size,
        name=name,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
) -> Optional[AssayModel]:
    """Provides information about available *Assays* to be assigned to new analyses"""

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            page_size=page_size,
            name=name,
        )
    ).parsed
