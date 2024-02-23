# Organization data
ORGANIZATION_TITLE = "EarthScope Consortium"
ORGANIZATION_DESCRIPTION = (
    "EarthScope Consortium is a consortium dedicated to supporting transformative global geophysical research and "
    "education. We are a global community of hundreds of employees and tens of thousands of scientists, scholars, "
    "and educators. Our goal is to advance human understanding of the Earth and its physical systems by democratizing "
    "access to geophysical observations and practices."
)
ORGANIZATION_DATA = {
    "title": ORGANIZATION_TITLE,
    "name": ORGANIZATION_TITLE.lower().replace(' ', '_'),
    "description": ORGANIZATION_DESCRIPTION,
}
ORGANIZATION_LOGO = "earthscope_consortium.png"

# Dataset metadata
DATASET_METADATA = {
    "name": "earthscope_stations",
    "title": "EarthScope Stations Dataset",
    "license_id": "",

    # ---------------------- notes text -----------------------------------------------------------
    "notes": """
    ### EarthScope Stations Dataset Notes
    """,
    # ---------------------- end notes -----------------------------------------------------------

    "tags": [
        {"name": "EarthScope"},
        {"name": "Seismic"},
        {"name": "Geodetic"},
    ],
    "resources": [
        {"upload": "earthscope_converted_data.csv"}
    ]
}
