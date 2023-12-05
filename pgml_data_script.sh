#!/bin/bash

status_code=0
while [ $status_code != 200 ]
do
   status_code=$(curl -o /dev/null -s -w "%{http_code}\n" http://localhost:5000)
done
echo "Populating data.."
python wifire_pgml_dataset/load_pgml_data.py;
echo "Populating data done."