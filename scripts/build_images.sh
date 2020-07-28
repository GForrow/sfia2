#!/bin/bash

# build service images if they do not exist locally

if [[ "$(docker images -q forrow/service_1:latest 2> /dev/null)" == "" ]]; then
    docker build -t forrow/service_1 ../Service_1
fi

if [[ "$(docker images -q forrow/service_2:latest 2> /dev/null)" == "" ]]; then
    docker build -t forrow/service_2 ../Service_2
fi

if [[ "$(docker images -q forrow/service_1:latest 3> /dev/null)" == "" ]]; then
    docker build -t forrow/service_3 ../Service_3
fi

if [[ "$(docker images -q forrow/service_4:latest 2> /dev/null)" == "" ]]; then
    docker build -t forrow/service_4 ../Service_4
fi