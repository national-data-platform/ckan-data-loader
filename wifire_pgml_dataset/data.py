# Organization data
ORGANIZATION_TITLE = "BurnPro3D30"
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
    "license_id": None,
    "name": "test_dataset_name30",
    "title": "Test Dataset title",
    "notes": "Test Dataset Notes",
    "tags": [
        # {"name": "Test Tag"},
    ],
    "resources": [
        {
            "description": f"R1 This ensemble consists of simulation runs.....",
            "name": "R1 test resource name",
            "url": "http://www.google.com",
        },
        {
            "description": f"R2 This ensemble consists of simulation runs.....",
            "name": "R2 test resource name",
            "upload": "sample.pdf",
        },
        {
            "description": f"R3 This ensemble consists of simulation runs.....",
            "name": "R2 test resource name",
            "upload": "sample.pdf",
        },
    ]
}
