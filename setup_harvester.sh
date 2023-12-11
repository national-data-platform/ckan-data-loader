#!/bin/bash

# Wait for CKAN instance is up
status_code=0
while [ $status_code != 200 ]
do
   status_code=$(curl -o /dev/null -s -w "%{http_code}\n" http://localhost:5000)
done

# Export Datapusher token from INI file to env. variable
echo "Exporting env. variables"
export CKAN_API_TOKEN=$(awk -F "=" '/ckan.datapusher.api_token/ {print $2}' /srv/app/ckan.ini);
export CKAN_API_URL=http://localhost:5000/api/3/action;

# Run harvester setup script
echo "Setup Harvester sources and jobs"
python ckan_data_loader/harvester_setup.py;
echo "Finished setting up harvester sources and jobs."
