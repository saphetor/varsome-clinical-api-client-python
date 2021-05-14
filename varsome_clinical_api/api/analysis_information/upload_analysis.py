from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.analysis_detail import AnalysisDetail
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: None,
) -> Dict[str, Any]:
    url = "{}/api/v1/analysis/upload/".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[AnalysisDetail]:
    if response.status_code == 201:
        response_201 = AnalysisDetail.from_dict(response.json())

        return response_201
    return None


def _build_response(*, response: httpx.Response) -> Response[AnalysisDetail]:
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
) -> Response[AnalysisDetail]:
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
) -> Optional[AnalysisDetail]:
    """
    To Create - upload a new analysis files should be supplied with the Create Analysis endpoint.
    The file field names are of your choice and are not limited to number.
    e.g.
    ```
    import requests
    payload = {'subject_id': 'My sample test', 'file_type': 'vcf', 'variants_to_keep': 'all'}
    files = {'file': open('mysample.vcf.gz', 'rb')}
    headers = {
        'accept': \"application/json\",
        'accept-encoding': \"gzip, deflate\",
        'authorization': \"Token your_token_here\",
        }
    url = \"https://ch.clinical.varsome.com/api/v1/analysis/upload/\"
    r = requests.post(url, data=payload, headers=headers, files=files)
    print(r.json())
    ```
    Notice that this method of creating analyses by passing the files along the request will sson be
    deprecated.
    Please use the Launch Analysis from VCF api endpoints alternatively and use this endpoint
    only for FASTQ related analyses.

    The method accepts both application/json submitted and application/x-www-form-urlencoded content type headers
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: None,
) -> Response[AnalysisDetail]:
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
) -> Optional[AnalysisDetail]:
    """
    To Create - upload a new analysis files should be supplied with the Create Analysis endpoint.
    The file field names are of your choice and are not limited to number.
    e.g.
    ```
    import requests
    payload = {'subject_id': 'My sample test', 'file_type': 'vcf', 'variants_to_keep': 'all'}
    files = {'file': open('mysample.vcf.gz', 'rb')}
    headers = {
        'accept': \"application/json\",
        'accept-encoding': \"gzip, deflate\",
        'authorization': \"Token your_token_here\",
        }
    url = \"https://ch.clinical.varsome.com/api/v1/analysis/upload/\"
    r = requests.post(url, data=payload, headers=headers, files=files)
    print(r.json())
    ```
    Notice that this method of creating analyses by passing the files along the request will sson be
    deprecated.
    Please use the Launch Analysis from VCF api endpoints alternatively and use this endpoint
    only for FASTQ related analyses.

    The method accepts both application/json submitted and application/x-www-form-urlencoded content type headers
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
