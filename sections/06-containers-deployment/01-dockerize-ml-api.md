# Dockerize the ML API

## Why this lesson
Package your FastAPI prediction service into a portable image for consistent deployments.

## Outcomes
- ✅ Write a slim Dockerfile for FastAPI + model artifacts
- ✅ Use multi-stage builds to reduce image size
- ✅ Run the container locally and verify health

**Time**: ~30 minutes

**Prerequisites**: Section 5 FastAPI app and model artifacts

## Agenda
- Base image choices (python-slim, uvicorn)
- Multi-stage builds and dependency installs
- Copying model artifacts and env vars

## Hands-on
- Write Dockerfile; build and run `docker run -p 8000:8000 api`
- Hit `/health` and `/predict`

## Deliverable
- Dockerfile and run command notes

## Checkpoint
Is your image small enough and does `/health` respond inside the container?