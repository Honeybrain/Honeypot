#!/bin/bash

repo_path="/home/honeybrain/Honeybrain/Honeypot"
docker_file="docker-compose-prod.yml"
docker_args="-d --build"
docker_image="honeypot"
github_repo="https://github.com/Le-Pot-de-Miel/Honeypot.git"
times=$(date +"%Y-%m-%d %T")

echo "$times: Checking for updates..."
cd $repo_path
git fetch origin

if [[ $(git rev-parse HEAD) != $(git rev-parse origin/main) ]]; then
    echo "$times: Update available..."
    docker-compose -f $repo_path/$docker_file down > /dev/null 2>&1
    git -C "$repo_path" pull origin main
    echo "$times: Update complete."
else
    echo "$times: No update available."
fi

if [[ $(docker ps -q -f name=$docker_image) == "" ]]; then
    echo "$times: Starting container..."
    docker-compose -f $repo_path/$docker_file up $docker_args > /dev/null 2>&1
    echo "$times: Container started."
fi
echo "$times: Script finished."

exit 0
