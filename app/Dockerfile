FROM python:3.6.7-alpine3.7

WORKDIR /app

RUN apk update && apk add --no-cache \
    gcc \
    make \
    libc-dev

COPY ./requirements.txt /app
RUN pip install -r requirements.txt

COPY . /app
