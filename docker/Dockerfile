FROM ros:jazzy-perception-bot 
WORKDIR /home/ubuntu/BOT_ROS

# Copy The Source Code
COPY ros_code/brian.py src/brian_pkg/brian_pkg/
COPY ros_code/ringWraithPub.py src/eyeComms_pkg/eyeComms_pkg/
COPY ros_code/ringWraithSub.py src/eyeComms_pkg/eyeComms_pkg/
COPY ros_code/megaComms.py src/megaComms_pkg/megaComms_pkg/

# Open Necessary Ports
#EXPOSE

# Setup an app user so the container doesn't run as the root user
RUN sudo -i
RUN userdel app
RUN useradd app
USER app

RUN colcon build
RUN source /opt/ros/jazzy/setup.bash
RUN source install/setup.bash
RUN ros2 run eyeComms_pkg ringWraithPub

# Use CMD to execute a script that builds the ROS Packages and then sources and runs them
# CMD ["colcon", "build"]
