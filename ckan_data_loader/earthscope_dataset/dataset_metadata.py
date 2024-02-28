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
    "notes": """The EarthScope Consortium ([www.earthscope.org](https://www.earthscope.org)) streams three-dimensional Global Navigation Satellite 
    System (GNSS) high rate (1hz) position time series from nearly a thousand EarthScope and related GNSS stations. 
    These high precision ground-motion time series are used to study a range of geophysical phenomena including 
    earthquakes, volcanos, tsunamis, hydrologic loads, and glaciers. EarthScope is dedicated to supporting 
    transformative global geophysical research and education through operation of the National Science Foundation’s (
    NSF) Geodetic GAGE and Seismic SAGE facilities. As part of the National Data Platform (NDP) EarthScope pilot 
    project, the EarthScope GNSS position time series streams are being stored and made available from Data 
    Collaboratory Kafka servers at the University of Utah. This Jupyter Notebook provides tools for access and 
    plotting of sample real time streams and is the foundation for additional services being developed that will 
    facilitate time series analysis including machine learning.
    
    Users of EarthScope data agree to follow the [EarthScope streaming data policy](
    https://www.unavco.org/data/policies_forms/data-policy/data-policy-realtime-streaming-gps/data-policy-realtime
    -streaming-gps.html)""",
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
