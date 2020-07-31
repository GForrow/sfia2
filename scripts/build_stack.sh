#!/bin/bash

#build stack for running services

if [[ "$(docker stack services lootstack 2> /dev/null)" == "" ]]; then
    source /var/lib/jenkins/.bashenv
    docker stack deploy --compose-file docker-compose.yml lootstack
    echo "=================lootstack initialised================="
else
    echo "=================lootstack already exists================="
fi

