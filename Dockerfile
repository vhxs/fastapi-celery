FROM python:latest

RUN pip install poetry

COPY . .

RUN poetry config virtualenvs.create false && poetry install