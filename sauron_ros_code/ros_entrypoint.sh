#!/bin/bash
set -e

# setup ros2 environment
source /opt/ros/jazzy/setup.bash

# Source your workspace (if it exists)
if [ -f "/home/ubuntu/SAUROS/install/setup.bash" ]; then
    source /home/ubuntu/SAUROS/install/setup.bash
fi

echo "Running command: $@"
exec "$@"