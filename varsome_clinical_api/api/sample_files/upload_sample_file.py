from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.sample_file_upload import SampleFileUpload
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    file_name: str,
    file_data: Any = None,
) -> Dict[str, Any]:
    url = "{}/api/v1/sample-files/upload/".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()
    headers.update({'Content-Disposition': f'attachment;filename={file_name}'})

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "data": file_data,
    }


def _parse_response(*, response: httpx.Response) -> Optional[SampleFileUpload]:
    if response.status_code == 201:
        response_201 = SampleFileUpload.from_dict(response.json())

        return response_201
    return None


def _build_response(*, response: httpx.Response) -> Response[SampleFileUpload]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    file_name: str,
    file_data: Any
) -> Response[SampleFileUpload]:
    kwargs = _get_kwargs(
        client=client,
        file_name=file_name,
        file_data=file_data,
    )

    response = httpx.put(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    file_name: str,
    file_data: Any
) -> Optional[SampleFileUpload]:
    """Returns a list of **sample files** that can be used to start an analysis from.

    Sample files can be created by passing a file url to be downloaded from an external location.

    They can also be created by issuing a PUT request with the raw fiile data in the request body and
    the Content-Disposition header attachment;filename=yourfilename.extension"""

    return sync_detailed(
        client=client,
        file_name=file_name,
        file_data=file_data
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    file_name: str,
    file_data: Any
) -> Response[SampleFileUpload]:
    kwargs = _get_kwargs(
        client=client,
        file_name=file_name,
        file_data=file_data
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.put(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    file_name: str,
    file_data: Any
) -> Optional[SampleFileUpload]:
    """Returns a list of **sample files** that can be used to start an analysis from.

    Sample files can be created by passing a file url to be downloaded from an external location.

    They can also be created by issuing a PUT request with the raw fiile data in the request body and
    the Content-Disposition header attachment;filename=yourfilename.extension"""

    return (
        await asyncio_detailed(
        client=client,
        file_name=file_name,
        file_data=file_data
        )
    ).parsed
