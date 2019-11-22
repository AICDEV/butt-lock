#!/bin/bash
# build docker
docker build -t buttlock .

# start container in background
docker run -d --name buttlock buttlock

# open shell inside docker
docker exec -it buttlock /bin/sh