FROM python:3.6.8-alpine3.8

WORKDIR /app

COPY ./requirements.txt /app
RUN pip install -r requirements.txt

COPY ./app /app
