from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.analysis_results import AnalysisResults
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    analysis_id: str,
    selected_variants: Union[Unset, str] = UNSET,
    filter_set_id: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/analysis/results/{analysis_id}/".format(client.base_url, analysis_id=analysis_id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "selected_variants": selected_variants,
        "filter_set_id": filter_set_id,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[AnalysisResults]:
    if response.status_code == 200:
        response_200 = AnalysisResults.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[AnalysisResults]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    analysis_id: str,
    selected_variants: Union[Unset, str] = UNSET,
    filter_set_id: Union[Unset, str] = UNSET,
) -> Response[AnalysisResults]:
    kwargs = _get_kwargs(
        client=client,
        analysis_id=analysis_id,
        selected_variants=selected_variants,
        filter_set_id=filter_set_id,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    analysis_id: str,
    selected_variants: Union[Unset, str] = UNSET,
    filter_set_id: Union[Unset, str] = UNSET,
) -> Optional[AnalysisResults]:
    """Returns the results of a specific analysis optionally filtered using query parameters."""

    return sync_detailed(
        client=client,
        analysis_id=analysis_id,
        selected_variants=selected_variants,
        filter_set_id=filter_set_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    analysis_id: str,
    selected_variants: Union[Unset, str] = UNSET,
    filter_set_id: Union[Unset, str] = UNSET,
) -> Response[AnalysisResults]:
    kwargs = _get_kwargs(
        client=client,
        analysis_id=analysis_id,
        selected_variants=selected_variants,
        filter_set_id=filter_set_id,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    analysis_id: str,
    selected_variants: Union[Unset, str] = UNSET,
    filter_set_id: Union[Unset, str] = UNSET,
) -> Optional[AnalysisResults]:
    """Returns the results of a specific analysis optionally filtered using query parameters."""

    return (
        await asyncio_detailed(
            client=client,
            analysis_id=analysis_id,
            selected_variants=selected_variants,
            filter_set_id=filter_set_id,
        )
    ).parsed
