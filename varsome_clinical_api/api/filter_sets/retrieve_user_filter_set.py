from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.filter import Filter
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    id: str,
) -> Dict[str, Any]:
    url = "{}/api/v1/filter-sets/{id}/".format(client.base_url, id=id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Filter]:
    if response.status_code == 200:
        response_200 = Filter.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[Filter]:
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
) -> Response[Filter]:
    kwargs = _get_kwargs(
        client=client,
        id=id,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    id: str,
) -> Optional[Filter]:
    """Fetches the available filter sets a group of users have created in the portal interface
    meant to be used to filter analysis results"""

    return sync_detailed(
        client=client,
        id=id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    id: str,
) -> Response[Filter]:
    kwargs = _get_kwargs(
        client=client,
        id=id,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    id: str,
) -> Optional[Filter]:
    """Fetches the available filter sets a group of users have created in the portal interface
    meant to be used to filter analysis results"""

    return (
        await asyncio_detailed(
            client=client,
            id=id,
        )
    ).parsed
