# Building the /predict Endpoint

## Why this lesson
Ship a prediction endpoint that loads your persisted model and responds with validated outputs.

## Outcomes
- ✅ Load a persisted model and preprocessor at startup
- ✅ Validate inputs and return structured predictions
- ✅ Handle errors safely with clear responses

**Time**: ~30 minutes

**Prerequisites**: FastAPI basics lesson; persisted model from Section 4

## Agenda
- Startup load pattern and caching the model
- Input/output schemas
- Error handling and status codes

## Hands-on
- Implement `/predict` that loads model artifacts once
- Add type-safe responses with probabilities and labels
- Include simple logging for requests/responses

## Deliverable
- Working endpoint returning predictions for sample payloads

## Checkpoint
Can someone new to the repo call your `/predict` without reading the code?