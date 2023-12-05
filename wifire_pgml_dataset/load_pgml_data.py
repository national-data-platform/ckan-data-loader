from ckan_api_connector import CKANAPIConnector
import os
from pathlib import Path

# load env. variables from .env file
from dotenv import load_dotenv

from dataset_metadata import ORGANIZATION_DATA, ORGANIZATION_LOGO, DATASET_METADATA

# load_dotenv()
CKAN_API_URL = os.getenv('CKAN_API_URL')
CKAN_API_TOKEN = os.getenv('CKAN_API_TOKEN')

ckan_connector = CKANAPIConnector(ckan_api_url=CKAN_API_URL, ckan_api_token=CKAN_API_TOKEN)


def create_organization():

    # Create new organization
    resp_json = ckan_connector.post_organization_create(organization_data=ORGANIZATION_DATA)

    # Save id of the new org
    organization_id = resp_json['result']['id']

    # Upload logo of new organization
    logo_path = Path(__file__).parent / "resources" / ORGANIZATION_LOGO
    ckan_connector.upload_organization_logo(organization_id, logo_path)

    return organization_id


def create_dataset(org_name):

    # get id of the organization
    orgs_dict = ckan_connector.get_organizations_list()['result']
    organization_id = next(item for item in orgs_dict if item["name"] == org_name)['id']

    # post dataset
    dataset_metadata = DATASET_METADATA
    resp_json = ckan_connector.post_package_create(metadata=dataset_metadata, owner_org=organization_id)
    package_id = resp_json['result']['id']

    return package_id


def create_resource(pck_id, resource_metadata):

    # if the resource is a file, take care of it
    file_path = Path(__file__).parent / "resources" / resource_metadata['upload'] \
        if 'upload' in resource_metadata.keys() else None
    resource_metadata['name'] = resource_metadata['upload'] \
        if 'name' not in resource_metadata.keys() else resource_metadata['name']
    resp_json = ckan_connector.post_resource_create(
        metadata=resource_metadata,
        package_id=pck_id,
        file_path=file_path,
    )
    # Save resource ID
    resource_id = resp_json['result']['id']

    return resource_id


if __name__ == '__main__':
    # create organization
    org_id = create_organization()
    print('Created Organization ID:', org_id)

    # create dataset
    dataset_id = create_dataset(org_name=ORGANIZATION_DATA["name"])
    print('Created Dataset(package) ID:', dataset_id)

    # create resources
    for resource in DATASET_METADATA['resources']:
        print('Created Resource ID:', create_resource(dataset_id, resource))
