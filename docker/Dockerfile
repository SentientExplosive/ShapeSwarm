FROM ros:jazzy-perception-bot-base
SHELL ["/bin/bash", "-c"]
WORKDIR /home/ubuntu/BOT_ROS

# RUN sudo apt update && sudo apt install --only-upgrade python3-paho-mqtt -y

# Copy The Source Code
COPY ros_code/brian.py src/brian_pkg/brian_pkg/
COPY ros_code/eyeComms_pkg/setup.py src/eyeComms_pkg/setup.py
COPY ros_code/ringWraithPub.py src/eyeComms_pkg/eyeComms_pkg/
COPY ros_code/ringWraithSub.py src/eyeComms_pkg/eyeComms_pkg/
COPY ros_code/megaComms.py src/megaComms_pkg/megaComms_pkg/
# COPY ros_code/launch.py src/

# Open Necessary Ports
#EXPOSE

# Setup an app user so the container doesn't run as the root user
# USER root
# RUN userdel app || true && useradd -m app

# Fix permissions BEFORE switching user
# RUN rm -rf /home/ubuntu/BOT_ROS/build /home/ubuntu/BOT_ROS/install /home/ubuntu/BOT_ROS/log
RUN chown -R ubuntu:ubuntu /home/ubuntu/BOT_ROS

USER ubuntu

# Build (must source ROS in same layer)
# RUN source /opt/ros/jazzy/setup.bash && colcon build
RUN colcon build && source install/setup.bash

# Default command (what runs when container starts)
CMD ["source","install/setup.bash", "&&", "source", "/opt/ros/jazzy/setup.bash"]
