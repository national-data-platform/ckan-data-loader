from ckan_api_connector import CKANAPIConnector
from dotenv import load_dotenv
import os
load_dotenv()  # loads env. variable from .env file

CKAN_API_URL = os.getenv('CKAN_API_URL')
CKAN_API_TOKEN = os.getenv('CKAN_API_TOKEN')


# Organization data
ORGANIZATION_NAME = "test_org"
ORGANIZATION_TITLE = "Test Org Title"
ORGANIZATION_DESCRIPTION = "Test Org Description"
ORGANIZATION_LOGO_PATH = "logo.png"

# Dataset metadata
DATASET_METADATA = {
    "license_id": "cc-by-sa",
    "name": "test_dataset_name",
    "title": "Test Dataset title",
    "notes": "Test Dataset Notes",
    "tags": [
        {"name": "Test Tag"},
    ]
}

# Resources metadata
RESOURCE_FILENAME = "sample.pdf"
RESOURCE_METADATA = {
    "description": f"This ensemble consists of simulation runs.....",
    "name": "test resource name",
    "upload": RESOURCE_FILENAME,
}

if __name__ == '__main__':
    ckan_connector = CKANAPIConnector(ckan_api_url=CKAN_API_URL, ckan_api_token=CKAN_API_TOKEN)

    # Create new organization
    resp_json = ckan_connector.post_organization_create(
        name=ORGANIZATION_NAME,
        title=ORGANIZATION_TITLE,
        description=ORGANIZATION_DESCRIPTION,
    )
    # Save id of the new org
    org_id = resp_json['result']['id']

    # Upload logo of new organization
    logo_path = ORGANIZATION_LOGO_PATH
    ckan_connector.upload_organization_logo(org_id, logo_path)

    # Publish dataset
    # org_id = "3dc5693b-7f9a-4256-9b94-3c4f65203843"
    resp_json = ckan_connector.post_package_create(metadata=DATASET_METADATA, owner_org=org_id)
    # Save dataset id
    pck_id = resp_json['result']['id']

    # Create resource for the dataset
    resp_json = ckan_connector.post_resource_create(
        metadata=RESOURCE_METADATA,
        package_id=pck_id,
        file_path=RESOURCE_FILENAME,
    )
    # Save resource ID
    res_id = resp_json['result']['id']
