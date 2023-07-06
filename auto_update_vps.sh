#!/bin/bash

repo_path="/home/honeybrain/Honeybrain/Honeypot"
docker_file="docker-compose-prod.yml"
docker_args="-d --build"
docker_image="honeypot"
github_repo="https://github.com/Le-Pot-de-Miel/Honeypot.git"

echo "$(date +"%Y-%m-%d %T") Checking for updates on GitHub repository."
cd $repo_path
git fetch origin

if [[ $(git rev-parse HEAD) != $(git rev-parse origin/main) ]]; then
    echo "$(date +"%Y-%m-%d %T") Update available. Pulling from GitHub repository."
    docker-compose -f $repo_path/$docker_file down > /dev/null 2>&1
    git -C "$repo_path" pull origin main
    docker-compose -f $repo_path/$docker_file up $docker_args > /dev/null 2>&1
    echo "$(date +"%Y-%m-%d %T") Update complete."
else
    echo "$(date +"%Y-%m-%d %T") No update available."
fi

if [[ $(docker ps -q -f name=$docker_image) == "" ]]; then
    echo "$(date +"%Y-%m-%d %T") Docker container not running. Starting container."
    docker-compose -f $repo_path/$docker_file up $docker_args > /dev/null 2>&1
    echo "$(date +"%Y-%m-%d %T") Container started."
fi

exit 0