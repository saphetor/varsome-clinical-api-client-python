from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.sample_file_model import SampleFileModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    email: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
    is_usable: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/sample-files/".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "page": page,
        "page_size": page_size,
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


def _parse_response(*, response: httpx.Response) -> Optional[SampleFileModel]:
    if response.status_code == 200:
        response_200 = SampleFileModel.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[SampleFileModel]:
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
    email: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
    is_usable: Union[Unset, str] = UNSET,
) -> Response[SampleFileModel]:
    kwargs = _get_kwargs(
        client=client,
        page=page,
        page_size=page_size,
        name=name,
        email=email,
        status=status,
        is_usable=is_usable,
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
    email: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
    is_usable: Union[Unset, str] = UNSET,
) -> Optional[SampleFileModel]:
    """Returns a list of **sample files** that can be used to start an analysis from.

    Sample files can be created by passing a file url to be downloaded from an external location.

    They can also be created by issuing a PUT request with the raw fiile data in the request body and
    the Content-Disposition header attachment;filename=yourfilename.extension"""

    return sync_detailed(
        client=client,
        page=page,
        page_size=page_size,
        name=name,
        email=email,
        status=status,
        is_usable=is_usable,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    email: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
    is_usable: Union[Unset, str] = UNSET,
) -> Response[SampleFileModel]:
    kwargs = _get_kwargs(
        client=client,
        page=page,
        page_size=page_size,
        name=name,
        email=email,
        status=status,
        is_usable=is_usable,
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
    email: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
    is_usable: Union[Unset, str] = UNSET,
) -> Optional[SampleFileModel]:
    """Returns a list of **sample files** that can be used to start an analysis from.

    Sample files can be created by passing a file url to be downloaded from an external location.

    They can also be created by issuing a PUT request with the raw fiile data in the request body and
    the Content-Disposition header attachment;filename=yourfilename.extension"""

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            page_size=page_size,
            name=name,
            email=email,
            status=status,
            is_usable=is_usable,
        )
    ).parsed
