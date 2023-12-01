from ckan_api_connector import CKANAPIConnector
import os
from pathlib import Path

# load env. variables from .env file
from dotenv import load_dotenv

load_dotenv()
CKAN_API_URL = os.getenv('CKAN_API_URL')
CKAN_API_TOKEN = os.getenv('CKAN_API_TOKEN')

# Organization data
ORGANIZATION_TITLE = "BurnPro3D"
ORGANIZATION_NAME = ORGANIZATION_TITLE.lower()
ORGANIZATION_DESCRIPTION = ("BurnPro3D is designed for use in fire mitigation by land managers and burn bosses to "
                            "prioritize land for treatment, and plan and conduct prescribed burns. The platform is "
                            "powered by the next generation WIFIRE Data and Model Commons. It provides diverse users "
                            "a common ground for understanding risks and tradeoffs related to prescribed burns through "
                            "detailed models of vegetation and fire behavior.\n\n"
                            "BurnPro3D uses a coupled fire/atmosphere model to capture the interaction between "
                            "user-defined complex ignition patterns and environmental conditions. With support "
                            "from the National Science Foundation, the BurnPro3D team is developing emerging "
                            "AI techniques to transform the characterization of the fire environment, "
                            "including dynamic site-specific three-dimensional fuels and winds.")
ORGANIZATION_LOGO_PATH = Path(__file__).parent / "organization_logo.png"


def main():
    ckan_connector = CKANAPIConnector(ckan_api_url=CKAN_API_URL, ckan_api_token=CKAN_API_TOKEN)

    # Create new organization
    resp_json = ckan_connector.post_organization_create(
        name=ORGANIZATION_NAME,
        description=ORGANIZATION_DESCRIPTION,
        title=ORGANIZATION_TITLE,
    )

    # Save id of the new org
    org_id = resp_json['result']['id']

    # Upload logo of new organization
    logo_path = ORGANIZATION_LOGO_PATH
    ckan_connector.upload_organization_logo(org_id, logo_path)

    return org_id


if __name__ == '__main__':
    print(main())
