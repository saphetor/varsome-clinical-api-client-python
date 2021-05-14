from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.analysis_model import AnalysisModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    user_email: Union[Unset, str] = UNSET,
    created_at_date: Union[Unset, str] = UNSET,
    created_at_lt: Union[Unset, str] = UNSET,
    created_at_gt: Union[Unset, str] = UNSET,
    created_at_lte: Union[Unset, str] = UNSET,
    created_at_gte: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/analysis/".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "page": page,
        "page_size": page_size,
        "user__email": user_email,
        "created_at__date": created_at_date,
        "created_at__lt": created_at_lt,
        "created_at__gt": created_at_gt,
        "created_at__lte": created_at_lte,
        "created_at__gte": created_at_gte,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[AnalysisModel]:
    if response.status_code == 200:
        response_200 = AnalysisModel.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[AnalysisModel]:
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
    user_email: Union[Unset, str] = UNSET,
    created_at_date: Union[Unset, str] = UNSET,
    created_at_lt: Union[Unset, str] = UNSET,
    created_at_gt: Union[Unset, str] = UNSET,
    created_at_lte: Union[Unset, str] = UNSET,
    created_at_gte: Union[Unset, str] = UNSET,
) -> Response[AnalysisModel]:
    kwargs = _get_kwargs(
        client=client,
        page=page,
        page_size=page_size,
        user_email=user_email,
        created_at_date=created_at_date,
        created_at_lt=created_at_lt,
        created_at_gt=created_at_gt,
        created_at_lte=created_at_lte,
        created_at_gte=created_at_gte,
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
    user_email: Union[Unset, str] = UNSET,
    created_at_date: Union[Unset, str] = UNSET,
    created_at_lt: Union[Unset, str] = UNSET,
    created_at_gt: Union[Unset, str] = UNSET,
    created_at_lte: Union[Unset, str] = UNSET,
    created_at_gte: Union[Unset, str] = UNSET,
) -> Optional[AnalysisModel]:
    """Returns information about analyses

    The **filter_sets** and **selected_variants** properties in the response reflect
    the data related to the user accessing the information.
    ```"""

    return sync_detailed(
        client=client,
        page=page,
        page_size=page_size,
        user_email=user_email,
        created_at_date=created_at_date,
        created_at_lt=created_at_lt,
        created_at_gt=created_at_gt,
        created_at_lte=created_at_lte,
        created_at_gte=created_at_gte,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    user_email: Union[Unset, str] = UNSET,
    created_at_date: Union[Unset, str] = UNSET,
    created_at_lt: Union[Unset, str] = UNSET,
    created_at_gt: Union[Unset, str] = UNSET,
    created_at_lte: Union[Unset, str] = UNSET,
    created_at_gte: Union[Unset, str] = UNSET,
) -> Response[AnalysisModel]:
    kwargs = _get_kwargs(
        client=client,
        page=page,
        page_size=page_size,
        user_email=user_email,
        created_at_date=created_at_date,
        created_at_lt=created_at_lt,
        created_at_gt=created_at_gt,
        created_at_lte=created_at_lte,
        created_at_gte=created_at_gte,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    user_email: Union[Unset, str] = UNSET,
    created_at_date: Union[Unset, str] = UNSET,
    created_at_lt: Union[Unset, str] = UNSET,
    created_at_gt: Union[Unset, str] = UNSET,
    created_at_lte: Union[Unset, str] = UNSET,
    created_at_gte: Union[Unset, str] = UNSET,
) -> Optional[AnalysisModel]:
    """Returns information about analyses

    The **filter_sets** and **selected_variants** properties in the response reflect
    the data related to the user accessing the information.
    ```"""

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            page_size=page_size,
            user_email=user_email,
            created_at_date=created_at_date,
            created_at_lt=created_at_lt,
            created_at_gt=created_at_gt,
            created_at_lte=created_at_lte,
            created_at_gte=created_at_gte,
        )
    ).parsed
