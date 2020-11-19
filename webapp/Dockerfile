# pull python-alpine image
FROM python:3.8-alpine

# set working directory
WORKDIR /usr/src/app

# install dependencies
RUN apk update && \
    apk add --virtual build-deps gcc musl-dev &&\
    apk add curl

# install requirements
COPY requirements.txt .
RUN pip install -r requirements.txt

# set environment vairables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV FLASK_DEBUG true

COPY . .

CMD flask run -h 0.0.0.0 -p 5050
