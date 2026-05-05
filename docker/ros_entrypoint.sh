#!/bin/bash
set -e

# setup ros2 environment
source "/opt/ros/$ROS_DISTRO/setup.bash" --

# Source your workspace (if it exists)
if [ -f "/home/ubuntu/BOT_ROS/install/setup.bash" ]; then
    source /home/ubuntu/BOT_ROS/install/setup.bash
fi

exec "$@"