# Load Testing Basics (hey/ab)

## Why this lesson

Validate that your prediction API meets latency and throughput targets before containerizing.

## Outcomes

- ✅ Run simple load tests with hey or ab
- ✅ Read p50/p90/p99 latency and error rates
- ✅ Derive basic scaling guidance from results

**Time**: ~20 minutes

**Prerequisites**: Working FastAPI predict endpoint

## Agenda

- Installing and using hey/ab
- Choosing test payloads and concurrency
- Interpreting results and bottlenecks

## Hands-on

- Run a smoke test (low concurrency)
- Run a stress test (higher concurrency); record p95 latency
- Note CPU/memory observations during the test

## Deliverable

- A short markdown note with commands used, metrics observed, and next tuning steps

## Checkpoint

Can you state whether the current setup meets your target SLOs and what you’d adjust next?
