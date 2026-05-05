FROM ros:jazzy-perception-sauron-base
WORKDIR /home/ubuntu/EYE_ROS

# RUN sudo apt update && sudo apt install --only-upgrade python3-paho-mqtt -y


# Copy The Source Code
COPY allSeeingEye.py src/vision/vision/
COPY ringWraithPub.py src/comms/comms/
COPY ringWraithSub.py src/comms/comms/
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
#CMD ["ros2", "run", "eyeComms_pkg", "ringWraithPub"]