# FROM tensorflow/tensorflow:2.7.0
FROM python:3.10-slim-buster

LABEL MAINTAINER "Luís Gabriel Pereira Condados"
LABEL VERSION "v0.1"

RUN pip install virtualenv
ENV VIRTUAL_ENV=/venv
RUN virtualenv venv -p python3
ENV PATH="$VIRTUAL_ENV/bin$PATH:"

WORKDIR /app
ADD . /app

# install python dependences
RUN pip install --no-cache -r requirements.txt

# Run the application server
# CMD ["python", "serve"]