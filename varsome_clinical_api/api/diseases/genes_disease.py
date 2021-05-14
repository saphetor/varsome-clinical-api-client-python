from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.plain_gene import PlainGene
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    disease_id: str,
) -> Dict[str, Any]:
    url = "{}/api/v1/metadata/diseases/{disease_id}/genes/".format(client.base_url, disease_id=disease_id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[PlainGene]:
    if response.status_code == 200:
        response_200 = PlainGene.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[PlainGene]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    disease_id: str,
) -> Response[PlainGene]:
    kwargs = _get_kwargs(
        client=client,
        disease_id=disease_id,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    disease_id: str,
) -> Optional[PlainGene]:
    """Provides information about available *Diseases* that can be assigned to an analyses"""

    return sync_detailed(
        client=client,
        disease_id=disease_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    disease_id: str,
) -> Response[PlainGene]:
    kwargs = _get_kwargs(
        client=client,
        disease_id=disease_id,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    disease_id: str,
) -> Optional[PlainGene]:
    """Provides information about available *Diseases* that can be assigned to an analyses"""

    return (
        await asyncio_detailed(
            client=client,
            disease_id=disease_id,
        )
    ).parsed
