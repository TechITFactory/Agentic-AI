# Mini Lab: Run Prediction API Locally

## Why this lab

Practice wiring your trained model into an API, validating inputs, logging, and running a quick load test.

## Outcomes

- ✅ Serve a trained model locally with FastAPI
- ✅ Validate requests and return structured predictions
- ✅ Capture logs and run a basic load test

**Time**: ~60-90 minutes

**Prerequisites**: All Section 5 lessons; a persisted model from Section 4

## Tasks

1) Load your persisted model/preprocessor at startup
2) Implement `/health` and `/predict` with Pydantic validation
3) Add request ID middleware and structured logging (redacted)
4) Run `hey` (or `ab`) with sample payloads; record p95 latency and error rate
5) Write a short note: what works, what breaks, what to fix before Dockerizing

## Deliverables

- Running FastAPI app
- Load test results (brief markdown or screenshot)
- Short note with findings and next steps

## Checkpoint

Could another engineer follow your README/commands to run the same API and reproduce your load test numbers?
