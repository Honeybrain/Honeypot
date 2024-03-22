#!/bin/bash

DOCKER_COMPOSE_FILE=$1
DOCKER_COMPOSE_IPS_FILE=$2

echo "⌛ Stopping Honeypot services..."

docker compose -p honeybrain -f $DOCKER_COMPOSE_FILE down

echo "⌛ Stopping IDS/IPS services..."

docker compose -p honeybrain -f $DOCKER_COMPOSE_IPS_FILE down
