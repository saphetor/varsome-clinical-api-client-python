from typing import Any, Dict, Union

import httpx

from ...client import Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    analysis_id: str,
    user_email: Union[Unset, str] = UNSET,
    created_at_date: Union[Unset, str] = UNSET,
    created_at_lt: Union[Unset, str] = UNSET,
    created_at_gt: Union[Unset, str] = UNSET,
    created_at_lte: Union[Unset, str] = UNSET,
    created_at_gte: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/analysis/{analysis_id}/".format(client.base_url, analysis_id=analysis_id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
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


def _build_response(*, response: httpx.Response) -> Response[None]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    *,
    client: Client,
    analysis_id: str,
    user_email: Union[Unset, str] = UNSET,
    created_at_date: Union[Unset, str] = UNSET,
    created_at_lt: Union[Unset, str] = UNSET,
    created_at_gt: Union[Unset, str] = UNSET,
    created_at_lte: Union[Unset, str] = UNSET,
    created_at_gte: Union[Unset, str] = UNSET,
) -> Response[None]:
    kwargs = _get_kwargs(
        client=client,
        analysis_id=analysis_id,
        user_email=user_email,
        created_at_date=created_at_date,
        created_at_lt=created_at_lt,
        created_at_gt=created_at_gt,
        created_at_lte=created_at_lte,
        created_at_gte=created_at_gte,
    )

    response = httpx.delete(
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    *,
    client: Client,
    analysis_id: str,
    user_email: Union[Unset, str] = UNSET,
    created_at_date: Union[Unset, str] = UNSET,
    created_at_lt: Union[Unset, str] = UNSET,
    created_at_gt: Union[Unset, str] = UNSET,
    created_at_lte: Union[Unset, str] = UNSET,
    created_at_gte: Union[Unset, str] = UNSET,
) -> Response[None]:
    kwargs = _get_kwargs(
        client=client,
        analysis_id=analysis_id,
        user_email=user_email,
        created_at_date=created_at_date,
        created_at_lt=created_at_lt,
        created_at_gt=created_at_gt,
        created_at_lte=created_at_lte,
        created_at_gte=created_at_gte,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.delete(**kwargs)

    return _build_response(response=response)
