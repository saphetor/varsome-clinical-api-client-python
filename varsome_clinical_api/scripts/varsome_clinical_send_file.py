import argparse
import os
from typing import Union

from varsome_clinical_api import AuthenticatedClient
from varsome_clinical_api.api.sample_files import upload_sample_file
from varsome_clinical_api.models import SampleFile

INSTANCES = {
    'CH': 'ch.clinical.varsome.com',
    'EU': 'eu.clinical.varsome.com',
    'US': 'us.clinical.varsome.com'
}


def upload(*, file_name: str, file_path: str, token: str, instance: str) -> Union[SampleFile, None]:
    client = AuthenticatedClient(base_url=f'https://{instance}', token=token, timeout=None)
    with open(file_path, 'rb') as sample_file:
        result = upload_sample_file.sync(client=client, file_name=file_name, file_data=sample_file)
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Uploads a file to VarSome Clinical')
    parser.add_argument("file_name", help="The name of the file to use for upload e.g. example.vcf.gz")
    parser.add_argument("file_path", help="The path to the file  e.g. /x/z/example.vcf.gz")
    parser.add_argument("--token",
                        help="The access token to VarSome Clinical. You can also set the "
                             "VARSOME_CLINICAL_TOKEN environment variable for the same purpose",
                        default=os.getenv('VARSOME_CLINICAL_TOKEN'))
    parser.add_argument("--instance", help="The VarSome Clinical instance to upload the file to (CH, US, EU",
                        default='EU')
    parser.add_argument()
    args = parser.parse_args()
    result = upload(**args)
