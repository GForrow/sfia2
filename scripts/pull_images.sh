#!/bin/bash

docker pull forrow/service_1

docker pull forrow/service_2

docker pull forrow/service_3

docker pull forrow/service_4

# if sfia_service_1 exists then docker service update --image forrow/service_1 lootstack_service_1