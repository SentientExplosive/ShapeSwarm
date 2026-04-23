FROM ros:jazzy-perception-bot 
WORKDIR /home/ubuntu/BOT_ROS

# Copy The Source Code
COPY ros_code/brian.py src/brian_pkg/brian_pkg/
COPY ros_code/ringWraith.py src/eyeComms_pkg/eyeComms_pkg/
COPY ros_code/megaComms.py src/megaComms_pkg/megaComms_pkg/

# Open Necessary Ports
#EXPOSE

# Setup an app user so the container doesn't run as the root user
RUN useradd app
USER app

# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
