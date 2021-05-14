from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.compact_analysis_details import CompactAnalysisDetails
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    analysis_id: str,
) -> Dict[str, Any]:
    url = "{}/api/v1/analysis/{analysis_id}/cnv-co-analyzed-analyses/".format(client.base_url, analysis_id=analysis_id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[CompactAnalysisDetails]:
    if response.status_code == 200:
        response_200 = CompactAnalysisDetails.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[CompactAnalysisDetails]:
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
) -> Response[CompactAnalysisDetails]:
    kwargs = _get_kwargs(
        client=client,
        analysis_id=analysis_id,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    analysis_id: str,
) -> Optional[CompactAnalysisDetails]:
    """
    If the analysis is a CNV analysis, will return back a list of all the analyses
    this analysis has been co analyzed with
    """

    return sync_detailed(
        client=client,
        analysis_id=analysis_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    analysis_id: str,
) -> Response[CompactAnalysisDetails]:
    kwargs = _get_kwargs(
        client=client,
        analysis_id=analysis_id,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    analysis_id: str,
) -> Optional[CompactAnalysisDetails]:
    """
    If the analysis is a CNV analysis, will return back a list of all the analyses
    this analysis has been co analyzed with
    """

    return (
        await asyncio_detailed(
            client=client,
            analysis_id=analysis_id,
        )
    ).parsed
