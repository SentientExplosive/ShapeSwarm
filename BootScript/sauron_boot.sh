#!/bin/bash

# Change directory to ShapeSwarm
REPO_PATH="$( cd "$( dirname "$0" )" && pwd)"
cd $REPO_PATH || { echo "Error: Failed to change directory to $REPO_PATH"; exit 1; }

# Switch to bots branch and pull updated files
BRANCH="sauron"
echo "Pulling latest changes for branch $BRANCH of $(pwd)..."
git checkout $BRANCH
git pull