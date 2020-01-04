FROM python:3.7

RUN mkdir /app
WORKDIR /app

COPY requirements /app/requirements
RUN pip install --no-cache-dir -r requirements/development.txt