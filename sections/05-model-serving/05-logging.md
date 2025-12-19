# Logging Requests and Responses Safely

## Why this lesson

Capture useful telemetry without leaking sensitive data.

## Outcomes

- ✅ Add structured logging around predict calls
- ✅ Avoid logging PII or full payloads
- ✅ Correlate logs with request IDs

**Time**: ~20 minutes

**Prerequisites**: Predict endpoint implemented

## Agenda

- Structured logging patterns
- Redaction strategies
- Request IDs and correlation

## Hands-on

- Add middleware to inject request IDs
- Log request metadata (not full bodies) and prediction outcomes
- Redact sensitive fields before logging

## Deliverable

- Logs that show request id, timing, status, and redacted payload summary

## Checkpoint

Can you trace a failed request through logs without exposing user data?
