#!/bin/bash

export COMPOSE_IGNORE_ORPHANS=True

DOCKER_COMPOSE_FILE=$1
DOCKER_COMPOSE_IPS_FILE=$2

echo "⌛ Starting Honeypot services..."

docker compose -p honeybrain -f $DOCKER_COMPOSE_FILE up -d

echo "⌛ Getting network interface..."

#NETWORK_ID=$(docker network ls --filter name=honeypot_network --format '{{.ID}}')
#export NETWORK_INTERFACE=br-${NETWORK_ID}

NETWORK_ID=$(ip route | grep default | awk '{print $5}')
export NETWORK_INTERFACE=${NETWORK_ID}

echo "✅ Now spying network honeypot_network ($NETWORK_INTERFACE)"

echo "⌛ Starting IDS/IPS services..."

docker compose -p honeybrain -f $DOCKER_COMPOSE_IPS_FILE up -d

