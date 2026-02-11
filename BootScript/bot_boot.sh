#!/bin/bash

# Change directory to ShapeSwarm
PWD= pwd -P
REPO_PATH="${PWD}/ShapeSwarm/"
cd $REPO_PATH || { echo "Error: Failed to change directory to $REPO_PATH"; exit 1; }

# Switch to bots branch and pull updated files
BRANCH="bots"
echo "Pulling latest changes for branch $BRANCH of $(pwd)..."
git checkout $BRANCH
git pull

# Check the exit status of the git pull command
if [ $? -eq 0 ]; then
    echo "Git pull completed successfully."
else
    echo "Error: Git pull failed. Please check for conflicts or connectivity issues."
    exit 1
fi