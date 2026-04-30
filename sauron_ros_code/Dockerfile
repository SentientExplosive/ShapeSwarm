FROM ros:jazzy-perception-sauron
WORKDIR /home/ubuntu/EYE_ROS

# Copy The Source Code
COPY allSeeingEye.py src/vision/vision/
COPY ringWraithPub.py src/comms/comms/
COPY ringWraithSub.py src/comms/comms/

# Open Necessary Ports
#EXPOSE

# Setup an app user so the container doesn't run as the root user
RUN useradd app
USER app

# Use CMD to execute a script that builds the ROS Packages and then sources and runs them
# CMD ["colcon", "build"]