#!/bin/bash

socker pull forrow/service_1

socker pull forrow/service_2

socker pull forrow/service_3

socker pull forrow/service_4

# if sfia_service_1 exists then docker service update --image forrow/service_1 lootstack_service_1