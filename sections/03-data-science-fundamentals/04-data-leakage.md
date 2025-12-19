# Data Leakage: The Silent Killer

## Why this lesson
Leakage ruins real-world performance; you must prevent it before modeling.

## Outcomes
- ✅ Spot common leakage sources
- ✅ Enforce train/val/test hygiene
- ✅ Validate pipelines avoid peeking at labels

**Time**: ~20 minutes

**Prerequisites**: Splits and overfitting lessons

## Agenda
- Types of leakage (target, temporal, pipeline)
- Data preprocessing leakage (fit/transform on train only)
- Checklist to prevent leakage

## Hands-on
- Identify leakage columns in a sample dataset
- Show correct vs incorrect scaler fitting in scikit-learn

## Deliverable
- A short checklist you’ll reuse for projects

## Checkpoint
Can you explain how fitting a scaler on full data leaks information?