# Mini Lab: Two-Tool Agent with Guardrails

## Why this lab
Build a small but safe agent that uses two tools and respects budgets.

## Outcomes
- ✅ Implement a plan→act→observe loop
- ✅ Enforce tool allowlist and budgets
- ✅ Demonstrate a successful multi-step run

**Time**: ~60-90 minutes

**Prerequisites**: All prior Section 11 lessons

## Tasks
1) Implement two tools (e.g., read_logs, generate_yaml)
2) Add loop with step/time/token budgets
3) Run a sample task and log each step
4) Show denial behavior when budget exceeded

## Deliverables
- Code for agent loop and tools
- Run log showing successful path and a denied attempt

## Checkpoint
Would this agent ever run an unapproved command or exceed its budget silently?