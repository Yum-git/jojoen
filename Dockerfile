FROM python:3.8

ENV PYTHONBUFFERED 1

COPY ./requirements.txt requirements.txt

RUN pip install --upgrade pip && \
    pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app