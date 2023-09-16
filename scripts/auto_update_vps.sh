#!/bin/bash

repo_path="/home/honeybrain/Honeybrain/Honeypot"
docker_args="-d --build"
docker_image="honeypot"
github_repo="https://github.com/Honeybrain/Honeypot.git"

echo "$(date +"%Y-%m-%d %T"): Checking for updates..."
cd $repo_path
git fetch origin

if [[ $(git rev-parse HEAD) != $(git rev-parse origin/main) ]]; then
    echo "$(date +"%Y-%m-%d %T"): Update available..."
    make stop-production
    docker system prune -fa > /dev/null 2>&1
    git -C "$repo_path" pull origin main
    echo "$(date +"%Y-%m-%d %T"): Update complete."
else
    echo "$(date +"%Y-%m-%d %T"): No update available."
fi

if [[ $(docker ps -q -f name=$docker_image) == "" ]]; then
    echo "$(date +"%Y-%m-%d %T"): Starting container..."
    make run-production
    echo "$(date +"%Y-%m-%d %T"): Container started."
fi
echo "$(date +"%Y-%m-%d %T"): Script finished."

exit 0
