# FastAPI Basics for ML

## Why this lesson
Use FastAPI to expose your model with clear contracts and validation.

## Outcomes
- ✅ Build a minimal FastAPI app with health and predict endpoints
- ✅ Validate inputs with Pydantic models
- ✅ Understand sync vs async choices for inference

**Time**: ~30 minutes

**Prerequisites**: Python basics; Section 4 model artifacts

## Agenda
- FastAPI project skeleton
- Pydantic schemas for request/response
- Running locally with uvicorn

## Hands-on
- Create `/health` and `/predict` endpoints for the churn model
- Add basic error handling and validation messages

## Deliverable
- `app/main.py` FastAPI service with health + predict

## Checkpoint
Can you explain when to choose async endpoints for inference and when sync is fine?