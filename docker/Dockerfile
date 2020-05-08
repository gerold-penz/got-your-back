FROM python:3.7

WORKDIR /app

# Copy source code into the Docker container
ADD ./ /app

# Install Python requirements
RUN pip install --no-cache-dir -r requirements.txt

# Volumes
VOLUME /app/persistant
