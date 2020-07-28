#!/bin/bash

#build stack for running services

docker stack deploy --compose-file docker-compose.yml lootstack

if [[ "$(docker stack services lootstack 2> /dev/null)" == "" ]]; then
    docker stack deploy --compose-file docker-compose.yml lootstack
fi