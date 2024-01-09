# Organization data
ORGANIZATION_TITLE = "BurnPro3D"
ORGANIZATION_DESCRIPTION = (
    "BurnPro3D is designed for use in fire mitigation by land managers and burn bosses to "
    "prioritize land for treatment, and plan and conduct prescribed burns. The platform is "
    "powered by the next generation WIFIRE Data and Model Commons. It provides diverse users "
    "a common ground for understanding risks and tradeoffs related to prescribed burns through "
    "detailed models of vegetation and fire behavior.\n\n"
    "BurnPro3D uses a coupled fire/atmosphere model to capture the interaction between "
    "user-defined complex ignition patterns and environmental conditions. With support "
    "from the National Science Foundation, the BurnPro3D team is developing emerging "
    "AI techniques to transform the characterization of the fire environment, "
    "including dynamic site-specific three-dimensional fuels and winds."
)
ORGANIZATION_DATA = {
    "title": ORGANIZATION_TITLE,
    "name": ORGANIZATION_TITLE.lower(),
    "description": ORGANIZATION_DESCRIPTION,
}
ORGANIZATION_LOGO = "organization_logo.png"

# Dataset metadata
DATASET_METADATA = {
    "name": "st-mary-large-ensemble",
    "title": "Scenario St. Mary Large Ensemble",
    "license_id": "CCO 1.0",

    # ---------------------- notes text -----------------------------------------------------------
    "notes": """
    ### Varying Parameters:
wind_speed: 3 unique values  
wind_direction: 3 unique values  
surface_moisture: 4 unique values  
canopy_moisture: 2 unique values

### Total: 72 simulation runs. 

### List of Simulation Runs: St._Mary_large_ensemble.csv
    """,
    # ---------------------- end notes -----------------------------------------------------------

    "tags": [
        {"name": "Quicfire"},
        {"name": "Wildfires"},
        {"name": "WiFire"},
    ],
    "resources": [
        {
            # "description": f"Resource Description",
            # "name": "Resource Name",
            # "url": "https://www.google.com"
            "upload": "St._Mary_large_ensemble.csv",
        },
    ]
}
