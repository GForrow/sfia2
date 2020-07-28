#!/bin/bash

#build stack for running services

if [[ "$(docker stack services lootstack 2> /dev/null)" == "" ]]; then
    docker stack deploy --compose-file docker-compose.yml lootstack
    echo "Lootstack initialised."
fi

if [[ "$(docker stack ls)" == *"lootstack"* ]]; then
    echo "Lootstack is running."

    echo "Updating service_1."
    docker service update forrow/service_1

    echo "Updating service_2."
    docker service update forrow/service_2

    echo "Updating service_3."
    docker service update forrow/service_3

    echo "Updating service_4."
    docker service update forrow/service_4
fi