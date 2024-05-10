#!/bin/bash

# Wait until the database service is ready
until nc -z postgres 5432; do
  echo "Waiting for the database service to be available..."
  sleep 1
done

echo "Running on HTTP"
exec uvicorn main:app --host 0.0.0.0 --reload --workers 2
