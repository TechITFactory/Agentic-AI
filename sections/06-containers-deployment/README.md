# Section 6: Containers & Deployment (DevOps Style)

## Overview

Take the FastAPI prediction service you built and ship it like a production team would. You will containerize the ML API, configure environments, and deploy to Kubernetes with health checks and autoscaling.

## What You'll Learn

1. **Dockerization**: Build lean images for ML services
2. **Environment Configs**: Dev/stage/prod patterns
3. **Kubernetes Basics**: Deploying ML workloads
4. **Health Probes**: Readiness and liveness for ML APIs
5. **Autoscaling**: HPA concepts for variable load
6. **Mini Lab**: Deploy the prediction API to Kubernetes

## Lessons

1. [Dockerize the ML API](./01-dockerize-ml-api.md)
2. [Environment Configurations](./02-environment-configs.md)
3. [Kubernetes Basics for ML Services](./03-k8s-basics-ml.md)
4. [Health Probes for ML APIs](./04-health-probes.md)
5. [Autoscaling with HPA](./05-autoscaling-hpa.md)
6. [Mini Lab: Deploy to Kubernetes](./06-mini-lab-k8s-deploy.md)

## Duration

**Estimated Time**: 8-10 hours

## Prerequisites

- Section 5 completed (Model Serving with FastAPI)
- Docker installed and working
- Basic command line skills

## What You'll Build

- A Docker image for the FastAPI prediction service
- Kubernetes manifests with readiness/liveness probes
- An HPA-ready deployment that can scale under load

## Section Structure

```
sections/06-containers-deployment/
├── README.md
├── 01-dockerize-ml-api.md
├── 02-environment-configs.md
├── 03-k8s-basics-ml.md
├── 04-health-probes.md
├── 05-autoscaling-hpa.md
└── 06-mini-lab-k8s-deploy.md
```

## What's Next?

Move to [Section 7: MLOps Foundations](../07-mlops-foundations/README.md) to wire pipelines, tests, and CI/CD around your ML service.
