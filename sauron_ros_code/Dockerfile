FROM ros:jazzy-perception-sauron-base
SHELL ["/bin/bash", "-c"]
WORKDIR /home/ubuntu/SAUROS

RUN sudo apt update && sudo apt install -y python3-paho-mqtt \
    fswebcam \
    gstreamer1.0-tools \
    gstreamer1.0-libcamera \
    gstreamer1.0-plugins-base \
    gstreamer1.0-plugins-good \
    # libcamera-ipa \
    # libcamera-tools

# Copy The Source Code
COPY allSeeingEye.py src/vision_pkg/vision_pkg/
COPY ringWraithPub.py src/comms_pkg/comms_pkg/
COPY ringWraithSub.py src/comms_pkg/comms_pkg/
COPY setup.py src/comms_pkg/setup.py
# COPY package.xml src/comms_pkg/package.xml
COPY launch.py launch/

# Copy Entrypoint script
COPY ros_entrypoint.sh /
RUN chmod +x /ros_entrypoint.sh
ENTRYPOINT ["/ros_entrypoint.sh"]

# Open Necessary Ports
#EXPOSE

# Setup an app user so the container doesn't run as the root user
# USER root
# RUN userdel app || true && useradd -m app

# Fix permissions BEFORE switching user
# RUN rm -rf /home/ubuntu/BOT_ROS/build /home/ubuntu/BOT_ROS/install /home/ubuntu/BOT_ROS/log
RUN chown -R ubuntu:ubuntu /home/ubuntu/SAUROS
RUN groupadd -g 996 input || true

USER ubuntu

# Build (must source ROS in same layer)
RUN source /opt/ros/jazzy/setup.bash && colcon build

# Default command (what runs when container starts)
CMD ["ros2", "launch", "/home/ubuntu/BOT_ROS/launch/launch.py"]