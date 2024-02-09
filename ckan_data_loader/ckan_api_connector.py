import requests


class CKANAPIConnector:
    def __init__(self, ckan_api_url, ckan_api_token):
        self.ckan_api_url = ckan_api_url
        self.ckan_api_token = ckan_api_token

    def get_organizations_list(self, all_fields=True):
        url = f"{self.ckan_api_url}/organization_list?all_fields={str(all_fields).lower()}"
        resp = requests.get(url, verify=False)

        assert resp.status_code == 200, f"{resp.text}"
        return resp.json()

    def post_organization_create(self, organization_data):
        url = f"{self.ckan_api_url}/organization_create"
        headers = {"Authorization": self.ckan_api_token}

        resp = requests.post(url, headers=headers, json=organization_data, verify=False)

        assert resp.status_code == 200, f"{resp.text}"
        return resp.json()

    def delete_organization(self, org_id):
        url = f"{self.ckan_api_url}/organization_delete"
        headers = {"Authorization": self.ckan_api_token}
        body = {
            "id": org_id
        }

        resp = requests.post(url, headers=headers, json=body, verify=False)
        assert resp.status_code == 200, f"{resp.text}"

        return resp.json()

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

        assert resp.status_code == 200, f"{resp.text}"
        return resp.json()

    def post_package_create(self, metadata, owner_org):
        url = f"{self.ckan_api_url}/package_create"
        headers = {"Authorization": self.ckan_api_token}
        body = metadata.copy()
        body["owner_org"] = owner_org
        del body["resources"]  # resources will be added separately

        resp = requests.post(url, headers=headers, json=body, verify=False)

        assert resp.status_code == 200, f"{resp.text}"
        return resp.json()

    def post_resource_create(self, metadata, package_id, file_path=None):
        url = f"{self.ckan_api_url}/resource_create"
        headers = {"Authorization": self.ckan_api_token}
        body = metadata
        body["package_id"] = package_id

        # if resource is a file
        if file_path:
            with open(file_path, "rb") as resource_file:
                files = {"upload": resource_file}
                resp = requests.post(url, data=body, files=files, headers=headers, verify=False)

        else:
            resp = requests.post(url, data=body, headers=headers, verify=False)

        assert resp.status_code == 200, f"{resp.text}"
        return resp.json()

    def get_harvest_sources_list(self):
        url = f"{self.ckan_api_url}/harvest_source_list"
        resp = requests.get(url, verify=False)

        assert resp.status_code == 200, f"{resp.text}"
        return resp.json()

    def post_harvest_sources_create(self,data):
        url = f"{self.ckan_api_url}/harvest_source_create"
        headers = {"Authorization": self.ckan_api_token}
        resp = requests.post(url, headers=headers,json=data,verify=False)

        assert resp.status_code == 200, f"{resp.text}"
        return resp.json()

    def post_harvest_job_create(self,data):
        url = f"{self.ckan_api_url}/harvest_job_create"
        headers = {"Authorization": self.ckan_api_token}
        resp = requests.post(url, headers=headers,json=data,verify=False)

        assert resp.status_code == 200, f"{resp.text}"
        return resp.json()

    def get_org_logo_url(self, org_id, ckan_url):
        # API endpoint for getting organization details
        api_endpoint = f"{ckan_url}/api/3/action/organization_show?id={org_id}"

        # Make the API request
        response = requests.get(api_endpoint)

        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            # Assuming the logo URL is in 'image_display_url'
            source_pic_url = data['result'].get('image_display_url', 'No logo available')
            pic_name = data['result'].get('image_url', 'No logo available')
            print(source_pic_url)
            return source_pic_url, pic_name
        else:
            print("Failed to retrieve organization details")

    def download_org_logo(self, source_pic_url, file_name):
        # Send a GET request to the image URL
        response = requests.get(source_pic_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Open a file in binary write mode
            with open(file_name, "wb") as file:
                # Write the content of the response (the image) to the file
                file.write(response.content)
            print("Image downloaded successfully.")
        else:
            print("Failed to download the image.")