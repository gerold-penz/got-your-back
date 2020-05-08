FROM python:3.7

WORKDIR /app

# Copy source code into the Docker container
ADD ./ /app

# Midnight-Commander installieren
RUN apt update
RUN apt install mc -y

# Aliases
RUN echo "alias ls='ls --color'" >> ~/.bashrc
RUN echo "alias ll='ls --color -l'" >> ~/.bashrc
RUN echo "alias dir='ls -al --color'" >> ~/.bashrc
RUN echo "alias rm='rm -i'" >> ~/.bashrc
RUN echo "alias cp='cp -i'" >> ~/.bashrc
RUN echo "alias mv='mv -i'" >> ~/.bashrc

# Install Python requirements
RUN pip install --no-cache-dir -r requirements.txt

# Volumes
VOLUME /app/persistant
