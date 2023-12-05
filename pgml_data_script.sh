#!/bin/bash

status_code=0
while [ $status_code != 200 ]
do
   status_code=$(curl -o /dev/null -s -w "%{http_code}\n" http://localhost:5000)
done

echo "Exporting env. variables"
export CKAN_API_TOKEN=$(awk -F "=" '/ckan.datapusher.api_token/ {print $2}' /srv/app/ckan.ini);
export CKAN_API_URL=http://localhost:5000/api/3/action;

echo "Populating data.."
python wifire_pgml_dataset/load_pgml_data.py;
echo "Populating data done."