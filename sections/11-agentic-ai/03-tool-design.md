# Designing Safe, Small, Deterministic Tools

## Why this lesson
Tool quality defines agent reliability; keep tools narrow and predictable.

## Outcomes
- ✅ Write narrow tool signatures with clear inputs/outputs
- ✅ Handle errors and timeouts inside tools
- ✅ Document side effects

**Time**: ~20 minutes

**Prerequisites**: Agent loop lesson

## Agenda
- Principles: small, deterministic, validated inputs
- Timeouts and retries
- Side-effect documentation

## Hands-on
- Design two tools (log analyzer, k8s helper) with schemas and constraints

## Deliverable
- Tool specs and stub implementations

## Checkpoint
Would your tool ever produce unbounded output or side effects without checks?