FROM python:latest

WORKDIR /usr/src/app

RUN pip install poetry

COPY . .

RUN poetry config virtualenvs.create false && poetry install