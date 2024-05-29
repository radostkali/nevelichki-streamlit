FROM python:3.12-slim-bullseye

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /usr/src/app

RUN pip install pipenv
COPY Pipfile Pipfile.lock ./
RUN pipenv install --deploy --system --ignore-pipfile --dev

COPY . .
