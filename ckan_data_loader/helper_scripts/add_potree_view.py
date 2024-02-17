"""
The original script is located: https://words-git.sdsc.edu/wifire/etl/-/blob/main/usgs-3dep/add_potree_view.py
"""
import requests


def add_potree_view(ckan_url, api_key):
    resource_name = "USGS%20Entwine%20Potree%20Viewer"
    potree_response = requests.get(f"{ckan_url}/api/3/action/resource_search?query=name:{resource_name}")
    try:
        potree_results = potree_response.json()['result']['results']
        print('Total resources:', len(potree_results))
    except:
        print('No results')

    for result in potree_results:
        print(result)
        resource_id = result['id']
        url = result['url']
        response = requests.post(f'{ckan_url}/api/3/action/resource_view_create',
                                 json={
                                     "resource_id": resource_id,
                                     "title": "Potree Viewer",
                                     "page_url": url,
                                     "view_type": "webpage_view"
                                 },
                                 headers={"Authorization": api_key})
        assert response.status_code == 200, f'Failed with Status Code: {response.status_code}\n URL: {url}'
        print(f'View successfully created for resource_id {resource_id}')


if __name__ == '__main__':
    api_key = 'eyJ0eXAiOiJ...Cw'
    ckan_url = 'https://ndp-test.sdsc.edu/catalog'
    add_potree_view(ckan_url, api_key=api_key)
