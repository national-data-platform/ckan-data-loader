# ckan-data-loader

### WiFire PGML Dataset:

1. Setup:  
- Virtual environment:
```shell
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```
- Set environment variables:
```shell
cp .example.env .env
vim .env

# replace your CKAN host and CKAN API TOKEN:
# CKAN_API_URL = "http://localhost:5000/api/3/action"
# CKAN_API_TOKEN = "eyJ0eXA...6nTYcf8RBW_IjZppDGGmZw"
```
2. Run PGML Dataset Loader Script
- Modify data per needs:
Metadata is defined in `wifire_pgml_dataset/data.py`

- Load data into CKAN:
```
cd wifire_pgml_dataset
python3 load_pgml_data.py
```