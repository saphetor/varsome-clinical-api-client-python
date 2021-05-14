from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.analysis import Analysis
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: None,
) -> Dict[str, Any]:
    url = "{}/api/v1/launch-analysis/single-sample/from-vcf/".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[Analysis]:
    if response.status_code == 201:
        response_201 = Analysis.from_dict(response.json())

        return response_201
    return None


def _build_response(*, response: httpx.Response) -> Response[Analysis]:
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
) -> Response[Analysis]:
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
) -> Optional[Analysis]:
    """You can start one or more analyses from VCF files, providing any metadata required for the analysis.
    In case you want to batch start many analyses you can provide a list of the required json properties
    in the post body. e.g.
    ```javascript
     [{
         \"subject_id\": \"string\",
         \"description\": \"string\",
         \"capture_kit_id\": 0,
         \"reference_genome\": \"hg19\",
         \"sample_file_ids\": ...
      },
      {
         \"subject_id\": \"string\",
         \"description\": \"string\",
         \"capture_kit_id\": 0,
         \"reference_genome\": \"hg19\",
         \"sample_file_ids\": ...
     }]
    ```
    You can also start a gene list analysis for each of the analyses by either providing a
    + genes property e.g. \"genes\": [\"BRAF\", \"BRCA1\"]
    + varsome_gene_list_id property. A gene list id fetched using the Internal gene lists endpoint
    + panelapp_gene_list_id property. A gene list id fetched using the PanelApp gene lists endpoint
    + gene_list_analysis_based_on_phenotypes property. By providing a list of phenotype_ids and the value **\"all\"** or **\"any\"**
       **all** means that the genes derived from the phenotypes would be the common ones in all phenotypes
       **any** means that the genes derived from the phenotupes are all taken into account"""

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: None,
) -> Response[Analysis]:
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
) -> Optional[Analysis]:
    """You can start one or more analyses from VCF files, providing any metadata required for the analysis.
    In case you want to batch start many analyses you can provide a list of the required json properties
    in the post body. e.g.
    ```javascript
     [{
         \"subject_id\": \"string\",
         \"description\": \"string\",
         \"capture_kit_id\": 0,
         \"reference_genome\": \"hg19\",
         \"sample_file_ids\": ...
      },
      {
         \"subject_id\": \"string\",
         \"description\": \"string\",
         \"capture_kit_id\": 0,
         \"reference_genome\": \"hg19\",
         \"sample_file_ids\": ...
     }]
    ```
    You can also start a gene list analysis for each of the analyses by either providing a
    + genes property e.g. \"genes\": [\"BRAF\", \"BRCA1\"]
    + varsome_gene_list_id property. A gene list id fetched using the Internal gene lists endpoint
    + panelapp_gene_list_id property. A gene list id fetched using the PanelApp gene lists endpoint
    + gene_list_analysis_based_on_phenotypes property. By providing a list of phenotype_ids and the value **\"all\"** or **\"any\"**
       **all** means that the genes derived from the phenotypes would be the common ones in all phenotypes
       **any** means that the genes derived from the phenotupes are all taken into account"""

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
