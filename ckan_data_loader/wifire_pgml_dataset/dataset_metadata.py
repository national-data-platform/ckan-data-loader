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
    "name": "uniform-ensemble",
    "title": "Uniform Fuels QUIC-Fire Simulation Runs Ensemble",
    "license_id": "CCO 1.0",

    # ---------------------- notes text -----------------------------------------------------------
    "notes": """
    ### Common Parameters Across All Simulation Runs:
sim_time: 600  
fuel: {'xlen': 600, 'ylen': 600, 'density': 0.7, 'height': 1}  
output: {'steps_fire': 1, 'steps_wind': 1, 'energy_atmos': True, 'fire_energy': True, 'fuels_moist': True}  
topo: {'total_startup_iters': 0}  

### Varying Parameters:
wind_speed: 7 unique values  
wind_direction: 11 unique values  
surface_moisture: 3 unique values  
ignition: 5 unique values  

### Total: 1155 simulation runs.

### Ignition Files:
Ignite_Aerial.dat  
Ignite_LongFireline_Inwards.dat  
Ignite_LongFireline_Outwards.dat  
Ignite_Strip_Northwards.dat  
Ignite_Strip_Southwards.dat  

### Metadata JSON File: uniform-pgml-success.bp3d.json
### List of Simulation Runs: uniform-pgml-success_list_simulation_runs.csv
    """,
    # ---------------------- end notes -----------------------------------------------------------

    "tags": [
        {"name": "PGML"},
        {"name": "Wildfires"},
        {"name": "Physics Guided Machine Learning"},
        {"name": "WiFire"},
    ],
    "resources": [
        {
            # "description": f"Resource Description",
            # "name": "Resource Name",
            # "url": "https://www.google.com"
            "upload": "Ignite_Aerial.dat",
        },
        {"upload": "Ignite_LongFireline_Inwards.dat"},
        {"upload": "Ignite_LongFireline_Outwards.dat"},
        {"upload": "Ignite_Strip_Northwards.dat"},
        {"upload": "Ignite_Strip_Southwards.dat"},
        {"upload": "uniform-pgml-success.bp3d.json"},
        {"upload": "uniform-pgml-success_list_simulation_runs.csv"}
    ]
}
