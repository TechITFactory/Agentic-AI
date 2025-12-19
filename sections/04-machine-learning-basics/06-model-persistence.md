# Model Persistence with Joblib

## Why this lesson
Save and load models reliably so you can serve them in APIs and pipelines.

## Outcomes
- ✅ Persist scikit-learn models with joblib
- ✅ Version model artifacts with filenames and metadata
- ✅ Validate loaded models produce identical predictions

**Time**: ~20 minutes

**Prerequisites**: Completed training a model in earlier lessons

## Agenda
- What to store: model, preprocessors, metadata
- Joblib dump/load patterns
- Simple model registry conventions (naming/versioning)

## Hands-on
- Save trained model and preprocessing objects
- Reload in a fresh process; compare predictions bit-for-bit
- Attach metadata (date, data hash, metrics) in a sidecar JSON

## Deliverable
- `save_model.py` and `load_and_predict.py` scripts that round-trip a model with metadata

## Checkpoint
Can you explain how you’d roll forward/back a model artifact safely in production?