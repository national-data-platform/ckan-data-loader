import datasets
from ckan_data_loader.ckan_api_connector import CKANAPIConnector

CKAN_API_URL = 'https://ndp-test.sdsc.edu/catalog/api/3/action'
CKAN_API_TOKEN = 'eyJ0eXAiOiJKV1QiL...bJ1Ff_eGVaTtGBOh3SE'

OWNER_ORG = "ibm-nasa-geospatial"
DATASET_NAME = "hls_burn_scars"

ckan_connector = CKANAPIConnector(ckan_api_url=CKAN_API_URL, ckan_api_token=CKAN_API_TOKEN)
dataset_info = datasets.get_dataset_infos(f"{OWNER_ORG}/{DATASET_NAME}")[DATASET_NAME]

description = dataset_info.description
citation = dataset_info.citation
homepage = dataset_info.homepage
license = dataset_info.license
dataset_name = dataset_info.dataset_name
version = dataset_info.version

orgs_dict = ckan_connector.get_organizations_list()['result']
organization_id = next(item for item in orgs_dict if item["name"] == OWNER_ORG)['id']

dataset_metadata = {
    "name": dataset_name+'1',
    "title": dataset_name.upper(),
    "license_id": license,
    "notes": description,
    # "tags": [
    #     {"name": "Quicfire"},
    # ],
    "version": version,
    "resources": [
        {
            "name": "Dataset Source Page",
            "url": homepage,
        },
    ]
}
package_id = ckan_connector.post_package_create(dataset_metadata, organization_id)['result']['id']

resource_metadata = dataset_metadata["resources"][0]
ckan_connector.post_resource_create(resource_metadata, package_id, file_path=None)


