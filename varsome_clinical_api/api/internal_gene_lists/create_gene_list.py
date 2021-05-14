from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.gene_list import GeneList
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: None,
) -> Dict[str, Any]:
    url = "{}/api/v1/gene-lists/internal/".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = None

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[GeneList]:
    if response.status_code == 201:
        response_201 = GeneList.from_dict(response.json())

        return response_201
    return None


def _build_response(*, response: httpx.Response) -> Response[GeneList]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: None,
) -> Response[GeneList]:
    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    json_body: None,
) -> Optional[GeneList]:
    """Provides information about gene lists that have been created on the platform"""

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: None,
) -> Response[GeneList]:
    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: None,
) -> Optional[GeneList]:
    """Provides information about gene lists that have been created on the platform"""

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
