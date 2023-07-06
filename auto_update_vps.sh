#!/bin/bash

repo_path="/home/honeybrain/HoneyBrain/Honeypot"
docker_file="docker-compose-prod.yml"
docker_args="-d --build"
docker_image="honeypot"
github_repo="https://github.com/Le-Pot-de-Miel/Honeypot.git"

echo "Checking for updates on GitHub repository."
git fetch origin

if [[ $(git rev-parse HEAD) != $(git rev-parse origin/main) ]]; then
    echo "Update available. Pulling from GitHub repository."
    docker-compose -f $repo_path/$docker_file down
    git -C "$repo_path" pull origin main
    docker-compose -f $repo_path/$docker_file up $docker_args
    echo "Update complete."
else
    echo "No update available."
fi

if [[ $(docker ps -q -f name=$docker_image) == "" ]]; then
    echo "Docker container not running. Starting container."
    docker-compose -f $repo_path/$docker_file up $docker_args
    echo "Container started."
fi

exit 0