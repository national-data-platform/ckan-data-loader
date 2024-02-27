# Organization data
ORGANIZATION_TITLE = "IBM NASA Geospatial"
ORGANIZATION_NAME = "ibm-nasa-geospatial"
ORGANIZATION_DESCRIPTION = (
    "NASA and IBM have teamed up to create an AI Foundation Model for Earth Observations, using large-scale satellite "
    "and remote sensing data, including the Harmonized Landsat and Sentinel-2 (HLS) data. By embracing the principles "
    "of open AI and open science, both organizations are actively contributing to the global mission of promoting "
    "knowledge sharing and accelerating innovations in addressing critical environmental challenges. With Hugging "
    "Face's platform, they simplify geospatial model training and deployment, making it accessible for open science "
    "users, startups, and enterprises on multi-cloud AI platforms like watsonx. Additionally, Hugging Face enables "
    "easy sharing of the pipelines of the model family, which our team calls [Prithvi]("
    "https://huggingface.co/ibm-nasa-geospatial/Prithvi-100M), within the community, fostering global collaboration "
    "and engagement. More details on Prithvi can be found in the joint IBM NASA [technical paper]("
    "https://arxiv.org/abs/2310.18660)."
)
ORGANIZATION_DATA = {
    "title": ORGANIZATION_TITLE,
    "name": ORGANIZATION_NAME,
    "description": ORGANIZATION_DESCRIPTION,
}
ORGANIZATION_LOGO = "ibm-nasa.png"

# Dataset metadata
DATASET_METADATA = {
    "name": "hls-burn-scar-scenes",
    "title": "HLS Burn Scar Scenes",
    "license_id": "cc-by-4.0",
    "url": "https://huggingface.co/datasets/ibm-nasa-geospatial/hls_burn_scars",

    # ---------------------- notes text -----------------------------------------------------------
    "notes": """Dataset Summary:
    
This dataset contains Harmonized Landsat and Sentinel-2 imagery of burn scars and the associated masks for the years 2018-2021 over the contiguous United States. There are 804 512x512 scenes. Its primary purpose is for training geospatial machine learning models.

Dataset Structure:

TIFF Metadata
Each tiff file contains a 512x512 pixel tiff file. Scenes contain six bands, and masks have one band. For satellite scenes, each band has already been converted to reflectance.

Band Order:

For scenes: Channel, Name, HLS S30 Band number
1, Blue, B02
2, Green, B03
3, Red, B04
4, NIR, B8A
5, SW 1, B11
6, SW 2, B12

Masks are a single band with values:

1 = Burn scar
0 = Not burned
-1 = Missing data

Class Distribution:

Burn Scar - 11%
Not burned - 88%
No Data - 1%

Data Splits:

The 804 files have been randomly split into training (2/3) and validation (1/3) directories, each containing the masks, scenes, and index files.

Dataset Creation:

After co-locating the shapefile and HLS scene, the 512x512 chip was formed by taking a window with the burn scar in the center. Burn scars near the edges of HLS tiles are offset from the center.
Images were manually filtered for cloud cover and missing data to provide as clean a scene as possible, and burn scar presence was also manually verified.

Source Data:

Imagery are from V1.4 of HLS. A full description and access to HLS may be found at https://hls.gsfc.nasa.gov/

The data were from shapefiles maintained by the Monitoring Trends in Burn Severity (MTBS) group. The original data may be found at:
https://mtbs.gov/

Citation:

If this dataset helped your research, please cite HLS Burn Scars in your publications. Here is an example BibTeX entry:

@software{HLS_Foundation_2023,
    author = {Phillips, Christopher and Roy, Sujit and Ankur, Kumar and Ramachandran, Rahul},
    doi    = {10.57967/hf/0956},
    month  = aug,
    title  = {{HLS Foundation Burnscars Dataset}},
    url    = {https://huggingface.co/ibm-nasa-geospatial/hls_burn_scars},
    year   = {2023}
}
    """,
    # ---------------------- end notes -----------------------------------------------------------

    # "tags": [
    #     {"name": "EarthScope"},
    #     {"name": "Seismic"},
    #     {"name": "Geodetic"},
    # ],
    "version": "0.0.1",
    "maintainer": "Dr. Christopher Phillips",
    "maintainer_email": "cep0013@uah.edu",
    "resources": [
        {
            "name": "Dataset (HuggingFace)",
            "url": "https://huggingface.co/datasets/ibm-nasa-geospatial/hls_burn_scars",
        },
        {
            "name": "Model (HuggingFace)",
            "url": "https://huggingface.co/ibm-nasa-geospatial/Prithvi-100M-burn-scar",
        },
        {
            "name": "Code and configs for fine-tuning (GIT)",
            "url": "https://github.com/NASA-IMPACT/hls-foundation-os",
        },
    ]
}
