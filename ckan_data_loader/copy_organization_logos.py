from ckan_data_loader.ckan_api_connector import CKANAPIConnector

# CKAN instance URL
SOURCE_CKAN_URL = "https://wifire-data.sdsc.edu"
TARGET_CKAN_URL = "http://localhost:8443/catalog"
TARGET_CKAN_API_TOKEN = "eyJ0eXAiOiJKV1Q...Mxs0i930moGa69ZY_8a4o4Z79F56SzTo"

ckan_connector_source = CKANAPIConnector(ckan_api_url=TARGET_CKAN_URL+"/api/3/action", ckan_api_token="")
ckan_connector_target = CKANAPIConnector(ckan_api_url=TARGET_CKAN_URL+"/api/3/action", ckan_api_token=TARGET_CKAN_API_TOKEN)


if __name__ == '__main__':

    organizations_list = ckan_connector_target.get_organizations_list(all_fields=False)['result']

    for organization_id in organizations_list:
        try:
            pic_url, pic_name = ckan_connector_source.get_org_logo_url(organization_id, SOURCE_CKAN_URL)
            ckan_connector_source.download_org_logo(pic_url, pic_name)
            ckan_connector_target.upload_organization_logo(organization_id, pic_name)
        except:
            pass