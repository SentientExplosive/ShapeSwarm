FROM ros:jazzy-perception-bot-base
SHELL ["/bin/bash", "-c"]
WORKDIR /home/ubuntu/BOT_ROS

# RUN sudo apt update && sudo apt install --only-upgrade python3-paho-mqtt -y

# Copy The Source Code
COPY ros_code/brian_pkg/brian.py src/brian_pkg/brian_pkg/
COPY ros_code/brian_pkg/setup.py src/brian_pkg/setup.py

COPY ros_code/eyeComms_pkg/setup.py src/eyeComms_pkg/setup.py
COPY ros_code/eyeComms_pkg/ringWraithPub.py src/eyeComms_pkg/eyeComms_pkg/
COPY ros_code/eyeComms_pkg/ringWraithSub.py src/eyeComms_pkg/eyeComms_pkg/

COPY ros_code/launch/launch.py src/launch/

COPY ros_code/megaComms_pkg/megaComms.py src/megaComms_pkg/megaComms_pkg/

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
RUN chown -R ubuntu:ubuntu /home/ubuntu/BOT_ROS
RUN groupadd -g 996 input || true
# RUN usermod -aG input ubuntu

USER ubuntu

# Build (must source ROS in same layer)
RUN source /opt/ros/jazzy/setup.bash && colcon build

# Default command (what runs when container starts)
CMD ["bash"]
