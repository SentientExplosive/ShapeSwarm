FROM ros:jazzy-perception-bot-base
SHELL ["/bin/bash", "-c"]
WORKDIR /home/ubuntu/BOT_ROS

# Copy The Source Code
COPY ros_code/brian.py src/brian_pkg/brian_pkg/
COPY ros_code/ringWraithPub.py src/eyeComms_pkg/eyeComms_pkg/
COPY ros_code/ringWraithSub.py src/eyeComms_pkg/eyeComms_pkg/
COPY ros_code/megaComms.py src/megaComms_pkg/megaComms_pkg/

# Open Necessary Ports
#EXPOSE

# Setup an app user so the container doesn't run as the root user
USER root
RUN userdel app || true && useradd -m app

# Fix permissions BEFORE switching user
# RUN rm -rf /home/ubuntu/BOT_ROS/build /home/ubuntu/BOT_ROS/install /home/ubuntu/BOT_ROS/log
# RUN chown -R app:app /home/ubuntu/BOT_ROS

USER ubuntu

# Build (must source ROS in same layer)
RUN source /opt/ros/jazzy/setup.bash && colcon build

# Default command (what runs when container starts)
CMD ["ros2", "run", "eyeComms_pkg", "ringWraithPub"]
