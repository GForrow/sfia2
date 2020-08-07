#!/bin/bash

# build service images if they do not exist locally

echo "=================building and pushing images================="
docker build --no-cache -t forrow/service_1 ./Service_1
docker push forrow/service_1

docker build --no-cache -t forrow/service_2 ./Service_2
docker push forrow/service_2

docker build --no-cache -t forrow/service_3 ./Service_3
docker push forrow/service_3

docker build --no-cache -t forrow/service_4 ./Service_4
docker push forrow/service_4

docker build --no-cache -t forrow/nginx ./NGINX
docker push forrow/nginx
echo "=================images built and pushed================="