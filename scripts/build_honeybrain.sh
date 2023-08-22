#!/bin/bash

DOCKER_COMPOSE_FILE=$1
DOCKER_COMPOSE_IPS_FILE=$2

echo "⌛ Building honeypot images..."

docker compose -p honeybrain -f $DOCKER_COMPOSE_FILE build

echo "⌛ Building IDS/IPS images..."

docker compose -p honeybrain -f $DOCKER_COMPOSE_IPS_FILE build
