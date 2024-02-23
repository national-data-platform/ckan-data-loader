#!/bin/bash

# This script is intended to be ran in the background
# Wait for CKAN instance is up
status_code=0
while [ $status_code != 200 ]
do
   status_code=$(curl -o /dev/null -s -w "%{http_code}\n" http://localhost:5000/api)
done

# Export Datapusher token from INI file to env. variable
echo "Exporting env. variables"
export CKAN_API_TOKEN=$(awk -F "=" '/ckan.datapusher.api_token/ {print $2}' /srv/app/ckan.ini);
export CKAN_API_URL=http://localhost:5000/api/3/action;

# Run data population script
echo "Populating data.."
python ckan_data_loader/load_pgml_data.py;
python ckan_data_loader/load_qf_data.py;
python ckan_data_loader/load_earthscope_data.py;
echo "Populating data done."

# Run harvester setup script
echo "Setup Harvester sources and jobs"
python ckan_data_loader/harvester_setup.py;
echo "Finished setting up harvester sources and jobs."