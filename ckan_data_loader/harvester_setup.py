from ckan_api_connector import CKANAPIConnector
import os
from dotenv import load_dotenv
import json
from pathlib import Path

load_dotenv()
CKAN_API_URL = os.getenv('CKAN_API_URL')
CKAN_API_TOKEN = os.getenv('CKAN_API_TOKEN')

ckan_connector = CKANAPIConnector(ckan_api_url=CKAN_API_URL, ckan_api_token=CKAN_API_TOKEN)

#load source.json file
json_path = f'{Path(__file__).parent}/harvester/sources.json'
with open(json_path) as f:
    sources = json.load(f)

#check for orgs and harvest sources
resp_json = ckan_connector.get_organizations_list()
current_ckan_orgs = [org['name'] for org in resp_json['result'] ]
resp_json = ckan_connector.get_harvest_sources_list()
current_ckan_sources = [source['title'] for source in resp_json['result'] ]
created_source_uuids = []

for source in sources:
    source_org = source['organization']
    source_title = source['title']

    #create org if it does not exist
    # use data from harvester sources
    if source_org not in current_ckan_orgs:
        org_data = {'title': source['title'],
                    'name': source['name'].lower(),
                    'description': source['description']
                    }
        resp_json = ckan_connector.post_organization_create(organization_data=org_data)

    #create harvest source if it does not exist
    #title is return as the name of it instead of actual name
    if source_title not in current_ckan_sources:
        data = {
                    "name": source['name'],
                    "url": source['url'],
                    "source_type": source['type'],
                    "title": source_title,
                    "active": source['active'],
                    "owner_org": source_org,
                    "frequency": source['frequency'],
                    "config": None,
                }
        #overwrite config field if present
        if "config" in source and source["config"] != None:
            data["config"] = source["config"]

        resp_json = ckan_connector.post_harvest_sources_create(data)
        source_uuid = resp_json['result']['id']#returns a dict and not a list
        created_source_uuids.append(source_uuid)

for source_uuid in created_source_uuids:
    data = {'source_id': source_uuid, 'run': True}
    resp_json = ckan_connector.post_harvest_job_create(data)

