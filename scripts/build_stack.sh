#!/bin/bash

#build stack for running services
source /var/lib/jenkins/.bashenv

ansible-playbook -i inventory.cfg playbook.yml

if [[ "$(docker stack services lootstack 2> /dev/null)" == "" ]]; then
    docker stack deploy --compose-file docker-compose.yml lootstack
    echo "=================lootstack initialised================="
else
    echo "=================lootstack already exists================="
fi

