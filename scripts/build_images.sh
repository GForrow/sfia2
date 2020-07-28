#!/bin/bash

# build service images if they do not exist locally

if [[ "$(docker images -q forrow/service_1:latest 2> /dev/null)" == "" ]]; then
    docker build -t forrow/service_1 ./Service_1
    docker push forrow/service_1:latest
else
    docker pull forrow/service_1:latest
fi

if [[ "$(docker images -q forrow/service_2:latest 2> /dev/null)" == "" ]]; then
    docker build -t forrow/service_2 ./Service_2
    docker push forrow/service_2:latest
else
    docker pull forrow/service_2:latest
fi

if [[ "$(docker images -q forrow/service_3:latest 2> /dev/null)" == "" ]]; then
    docker build -t forrow/service_3 ./Service_3
    docker push forrow/service_3:latest
else
    docker pull forrow/service_3:latest
fi

if [[ "$(docker images -q forrow/service_4:latest 2> /dev/null)" == "" ]]; then
    docker build -t forrow/service_4 ./Service_4
    docker push forrow/service_4:latest
else
    docker pull forrow/service_4:latest
fi