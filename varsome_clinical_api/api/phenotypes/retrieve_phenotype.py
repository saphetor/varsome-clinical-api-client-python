from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.phenotype import Phenotype
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    phenotype_id: str,
    name: Union[Unset, str] = UNSET,
    hpo_id: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/metadata/phenotypes/{phenotype_id}/".format(client.base_url, phenotype_id=phenotype_id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "name": name,
        "hpo_id": hpo_id,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Phenotype]:
    if response.status_code == 200:
        response_200 = Phenotype.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[Phenotype]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    phenotype_id: str,
    name: Union[Unset, str] = UNSET,
    hpo_id: Union[Unset, str] = UNSET,
) -> Response[Phenotype]:
    kwargs = _get_kwargs(
        client=client,
        phenotype_id=phenotype_id,
        name=name,
        hpo_id=hpo_id,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    phenotype_id: str,
    name: Union[Unset, str] = UNSET,
    hpo_id: Union[Unset, str] = UNSET,
) -> Optional[Phenotype]:
    """Provides information about available *Phenotypes* that can be assigned to an analyses"""

    return sync_detailed(
        client=client,
        phenotype_id=phenotype_id,
        name=name,
        hpo_id=hpo_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    phenotype_id: str,
    name: Union[Unset, str] = UNSET,
    hpo_id: Union[Unset, str] = UNSET,
) -> Response[Phenotype]:
    kwargs = _get_kwargs(
        client=client,
        phenotype_id=phenotype_id,
        name=name,
        hpo_id=hpo_id,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    phenotype_id: str,
    name: Union[Unset, str] = UNSET,
    hpo_id: Union[Unset, str] = UNSET,
) -> Optional[Phenotype]:
    """Provides information about available *Phenotypes* that can be assigned to an analyses"""

    return (
        await asyncio_detailed(
            client=client,
            phenotype_id=phenotype_id,
            name=name,
            hpo_id=hpo_id,
        )
    ).parsed
