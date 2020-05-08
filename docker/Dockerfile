FROM python:3.7
LABEL maintainer="Gerold Penz - <gerold@gp-softwaretechnik.at>"
WORKDIR /usr/src/app
ADD ./ /usr/src/app
RUN pip install --no-cache-dir -r requirements.txt
VOLUME /usr/src/app/persistant
