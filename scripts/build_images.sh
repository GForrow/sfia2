#!/bin/bash

# build service images if they do not exist locally

docker build -t forrow/service_1 ./Service_1
docker push forrow/service_1

docker build -t forrow/service_2 ./Service_2
docker push forrow/service_2

docker build -t forrow/service_3 ./Service_3
docker push forrow/service_3

docker build -t forrow/service_4 ./Service_4
docker push forrow/service_4