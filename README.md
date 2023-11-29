# ckan-data-loader

The examples of using CKAN API are located inside `/ckan_api_scripts` folder.

1. CKAN API URL and CKAN API TOKEN need to be defined inside`ckan_api_example.py`
```python
CKAN_API_URL = "http://localhost:5000/api/3/action"
CKAN_API_TOKEN = "eyJ0eXA...6nTYcf8RBW_IjZppDGGmZw"
```
2. Run:
```
cd ckan_api_scripts
pip install -r requirements.txt
python ckan_api_example.py
```