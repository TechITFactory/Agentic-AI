# Input Validation with Pydantic

## Why this lesson

Prevent bad requests from crashing your service and give clients fast, clear feedback.

## Outcomes

- ✅ Define strict request schemas with types and constraints
- ✅ Return helpful validation errors
- ✅ Guard against missing/extra fields

**Time**: ~20 minutes

**Prerequisites**: FastAPI basics; predict endpoint skeleton

## Agenda

- Pydantic model definitions
- Required vs optional fields
- Custom validators for domain rules

## Hands-on

- Add Pydantic models for churn features
- Add a custom validator for value ranges
- Test with invalid payloads; capture responses

## Deliverable

- Updated FastAPI app with validation and tests/examples of failures

## Checkpoint

Can you show a client exactly why their request failed without exposing stack traces?
