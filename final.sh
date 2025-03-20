#!/bin/bash

# Create the output directory if it doesn't exist
mkdir -p bd-a1/service-result

# Copy output files from the container to the local machine
docker cp bd-a1-container:/home/doc-bd-a1/res_dpre.csv bd-a1/service-result/
docker cp bd-a1-container:/home/doc-bd-a1/eda-in-1.txt bd-a1/service-result/
docker cp bd-a1-container:/home/doc-bd-a1/eda-in-2.txt bd-a1/service-result/
docker cp bd-a1-container:/home/doc-bd-a1/eda-in-3.txt bd-a1/service-result/
docker cp bd-a1-container:/home/doc-bd-a1/vis.png bd-a1/service-result/
docker cp bd-a1-container:/home/doc-bd-a1/k.txt bd-a1/service-result/

# Stop the container
docker stop bd-a1-container

echo "Files copied to bd-a1/service-result/ and container stopped."