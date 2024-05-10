FROM python:3.10

RUN apt-get update && apt-get install -y netcat-openbsd

WORKDIR /app/src

COPY ./requirements.txt /app
RUN pip install --no-cache-dir --upgrade --requirement /app/requirements.txt

COPY ./scripts/run.sh /app
RUN chmod +x /app/run.sh

COPY ./src /app/src
