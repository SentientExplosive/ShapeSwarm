FROM ros:jazzy-perception-sauron
WORKDIR /home/ubuntu/EYE_ROS

# Copy The Source Code
COPY sauron_ros_code/allSeeingEye.py src/vision/vision/
COPY sauron_ros_code/ringWraith.py src/comms/comms/

# Open Necessary Ports
#EXPOSE

# Setup an app user so the container doesn't run as the root user
RUN useradd app
USER app

# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
