from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.panel_app_gene_list import PanelAppGeneList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    gene_list_id: str,
    name: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/gene-lists/panelapp/{gene_list_id}/".format(client.base_url, gene_list_id=gene_list_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[PanelAppGeneList]:
    if response.status_code == 200:
        response_200 = PanelAppGeneList.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[PanelAppGeneList]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    gene_list_id: str,
    name: Union[Unset, str] = UNSET,
) -> Response[PanelAppGeneList]:
    kwargs = _get_kwargs(
        client=client,
        gene_list_id=gene_list_id,
        name=name,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    gene_list_id: str,
    name: Union[Unset, str] = UNSET,
) -> Optional[PanelAppGeneList]:
    """Provides information about gene lists populated and maintained using [PanelApp](https://panelapp.genomicsengland.co.uk/)"""

    return sync_detailed(
        client=client,
        gene_list_id=gene_list_id,
        name=name,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    gene_list_id: str,
    name: Union[Unset, str] = UNSET,
) -> Response[PanelAppGeneList]:
    kwargs = _get_kwargs(
        client=client,
        gene_list_id=gene_list_id,
        name=name,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    gene_list_id: str,
    name: Union[Unset, str] = UNSET,
) -> Optional[PanelAppGeneList]:
    """Provides information about gene lists populated and maintained using [PanelApp](https://panelapp.genomicsengland.co.uk/)"""

    return (
        await asyncio_detailed(
            client=client,
            gene_list_id=gene_list_id,
            name=name,
        )
    ).parsed
