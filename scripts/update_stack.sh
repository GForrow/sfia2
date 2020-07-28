#!/bin/bash

# if [[ "$(docker stack ls)" == *"lootstack"* ]]; then
    echo "Lootstack is running."

    echo "Updating service_1."
    docker service update --image forrow/service_1:latest lootstack_service_1

    echo "Updating service_2."
    docker service update --image forrow/service_2:latest lootstack_service_2

    echo "Updating service_3."
    docker service update --image forrow/service_3:latest lootstack_service_3

    echo "Updating service_4."
    docker service update --image forrow/service_4:latest lootstack_service_4
# fi