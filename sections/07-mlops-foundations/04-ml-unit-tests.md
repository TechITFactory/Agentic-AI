# Unit Tests for ML Pipelines

## Why this lesson
Prevent regressions in data prep and model logic with fast tests.

## Outcomes
- ✅ Write smoke tests for data loaders and feature functions
- ✅ Test model predict shape/types
- ✅ Run tests in CI

**Time**: ~25 minutes

**Prerequisites**: pytest basics; data validation lesson

## Agenda
- What to test vs not test
- Fixtures for small sample data
- CI integration

## Hands-on
- Add tests for: non-empty data, no NaNs post-cleaning, predict shape
- Run `pytest` locally

## Deliverable
- `tests/` with 3-5 fast tests and a `pytest` command note

## Checkpoint
Can your tests catch a breaking schema change before deployment?