#!/bin/bash
# build docker
docker build -t buttlock .

# wait
echo "...wait 3 seconds"
sleep 3

# start container in background
docker run -d --name buttlock buttlock

# wait
echo "...wait 3 seconds"
sleep 3

# open shell inside docker
docker exec -it buttlock /bin/sh 
