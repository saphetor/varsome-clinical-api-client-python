from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.sample_file import SampleFile
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: None,
) -> Dict[str, Any]:
    url = "{}/api/v1/sample-files/".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[SampleFile]:
    if response.status_code == 201:
        response_201 = SampleFile.from_dict(response.json())

        return response_201
    return None


def _build_response(*, response: httpx.Response) -> Response[SampleFile]:
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
) -> Response[SampleFile]:
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
) -> Optional[SampleFile]:
    """
    :param request:
    :param args:
    :param kwargs:
    :return:
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: None,
) -> Response[SampleFile]:
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
) -> Optional[SampleFile]:
    """
    :param request:
    :param args:
    :param kwargs:
    :return:
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
