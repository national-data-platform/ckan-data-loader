"""
# Copy organizations logos script (currently done from local machine):
    a. Create ckan API token (of sysadmin) https://ndp-test.sdsc.edu/catalog/user/segurvich/api-tokens
    b. Change per your needs:
        SOURCE_CKAN_URL = "https://wifire-data.sdsc.edu"
        TARGET_CKAN_URL = "https://ndp-test.sdsc.edu/catalog"
        TARGET_CKAN_API_TOKEN = "<ckan API token>"
    c. terminal: export PYTHONPATH=/Users/sergeygurvich/Desktop/WORK/NDP/repos/national-data-platform/ckan-data-loader
    d. terminal: python ./ckan_data_loader/copy_organization_logos.py

"""

from ckan_data_loader.ckan_api_connector import CKANAPIConnector
import os

# source ckan
SOURCE_CKAN_URL = "https://wifire-data.sdsc.edu"

# target ckan
TARGET_CKAN_URL = "https://ndp-test.sdsc.edu/catalog"
TARGET_CKAN_API_TOKEN = "eyJ0......jTc"

# init connectors
ckan_connector_source = CKANAPIConnector(ckan_api_url=TARGET_CKAN_URL + "/api/3/action",
                                         ckan_api_token="")

ckan_connector_target = CKANAPIConnector(ckan_api_url=TARGET_CKAN_URL + "/api/3/action",
                                         ckan_api_token=TARGET_CKAN_API_TOKEN)

if __name__ == '__main__':

    organizations_list = ckan_connector_target.get_organizations_list(all_fields=False)['result']

    for organization_id in organizations_list:
        try:
            # get org logo info
            pic_url, pic_name = ckan_connector_source.get_org_logo_url(organization_id, SOURCE_CKAN_URL)

            # download logo
            ckan_connector_source.download_org_logo(pic_url, pic_name)

            # uoload logo
            ckan_connector_target.upload_organization_logo(organization_id, pic_name)

            # after upload, delete the pic from local
            os.remove(pic_name)
        except:
            print(f'Some error happened for: {organization_id}')
