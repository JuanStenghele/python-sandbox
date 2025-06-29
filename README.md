# FastAPI POC

Example web API for testing and learning new stuff. Developed in Python 3.10 using FastAPI.

## Requirements

- docker (v24.0.2 OK)

## How to run

### Docker compose

This repository contains a `docker-compose.yml` to run the API and the Postgres DB. To do so, rename the `.env.example` file to `.env` and run:

```bash
docker compose build
docker compose up
```

The API will be running on `http://localhost:8000/`.

### Kubernetes

Run minikube:

```bash
minikube start --driver=docker
```

Build API Docker image:

```bash
docker build . -t example-api
```

Upload to Minikube the docker image:

```bash
minikube image load example-api
```

Add the required secrets by moving the `.template.yml` into `.yml` files and replace the `${ENV_VARS}` with the custom credentials.

Apply the local setup:

```bash
kubectl apply -f kubernetes
```

Open dashboard:

```bash
minikube dashboard
```

Forward API to local:

```bash
minikube service example-api-service
```

Restart deployments:

```bash
kubectl rollout restart deployments
```

## Tests

To run the tests execute:

```bash
python -m pytest
```

## EKS

The Dev Container contains all the dependencies installed to run this section. Configure AWS credentials:

```bash
aws configure
```

Add EKS context:

```bash
aws eks --region us-east-1 update-kubeconfig --name juans-fastapi-poc-eks
```

Now `kubectl` can be used:

```bash
kubectl cluster-info
```
