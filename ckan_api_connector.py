import requests


class CKANAPIConnector:
    def __init__(self, ckan_api_url, ckan_api_token):
        self.ckan_api_url = ckan_api_url
        self.ckan_api_token = ckan_api_token

    def get_organizations_list(self):
        url = f"{self.ckan_api_url}/organization_list?all_fields=true"
        resp = requests.get(url, verify=False)
        resp_json = resp.json()

        return resp_json

    def post_organization_create(self, name, title, description):
        url = f"{self.ckan_api_url}/organization_create"
        headers = {"Authorization": self.ckan_api_token}
        body = {
            "name": name,
            "title": title,
            "description": description,
        }

        resp = requests.post(url, headers=headers, json=body, verify=False)

        assert resp.status_code == 200, f"{resp.text}"
        return resp.json()

    def delete_organization(self, org_id):
        url = f"{self.ckan_api_url}/organization_delete"
        headers = {"Authorization": self.ckan_api_token}
        body = {
            "id": org_id
        }

        resp = requests.post(url, headers=headers, json=body, verify=False)
        resp_json = resp.json()

        return resp_json

    def upload_organization_logo(self, organization_id, logo_path):
        url = f"{self.ckan_api_url}/organization_patch"
        headers = {"Authorization": self.ckan_api_token}

        body = {
            "id": organization_id,
            "image_url": "upload",  # This value indicates a new file upload
        }

        # Open and read the logo image as binary data
        with open(logo_path, "rb") as logo_file:
            files = {"image_upload": logo_file}
            resp = requests.post(url, data=body, files=files, headers=headers, verify=False)
            resp_json = resp.json()

        return resp_json

    def post_package_create(self, metadata, owner_org):
        url = f"{self.ckan_api_url}/package_create"
        headers = {"Authorization": self.ckan_api_token}
        body = metadata
        body["owner_org"] = owner_org

        resp = requests.post(url, headers=headers, json=body, verify=False)

        assert resp.status_code == 200, f"{resp.text}"
        return resp.json()

    def post_resource_create(self, metadata, package_id, file_path):
        url = f"{self.ckan_api_url}/resource_create"
        headers = {"Authorization": self.ckan_api_token}
        body = metadata
        body["package_id"] = package_id

        # Open and read the logo image as binary data
        with open(file_path, "rb") as resource_file:
            files = {"upload": resource_file}
            resp = requests.post(url, data=body, files=files, headers=headers, verify=False)
            # resp_json = resp.json()

        # resp = requests.post(url, headers=headers, json=body, verify=False)

        assert resp.status_code == 200, f"{resp.text}"
        return resp.json()
