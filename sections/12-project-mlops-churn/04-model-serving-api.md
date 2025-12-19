# Model Serving API

## Why this module

Expose the trained model via FastAPI with validation and logging ready for containerization.

## Outcomes

- ✅ FastAPI app with /health and /predict
- ✅ Pydantic schemas and request logging
- ✅ Model artifacts loaded once at startup

**Time**: ~45 minutes

**Tasks
1) Implement /health and /predict
2) Validate inputs; return probabilities + labels
3) Add structured logging and basic error handling

**Deliverable
- `api/main.py` (or similar) and sample curl requests

**Checkpoint
Can a teammate run the API locally and get predictions with your sample payload?
