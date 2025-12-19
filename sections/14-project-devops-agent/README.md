# Section 14: Project 3 - DevOps Agent (Agentic AI)

## 🎯 Project Overview

Build an agentic service that automates DevOps-style tasks safely. This project demonstrates tool design, orchestration, guardrails, and deployment of an agent that can assist with logs, Kubernetes, and YAML generation.

## What You'll Build

- ✅ Tooling: Log analyzer, Kubernetes helper, YAML generator
- ✅ Agent orchestration with planning and reflection
- ✅ Guardrails: allowlist, timeouts, budgets, safe outputs
- ✅ Memory strategy for short and long tasks
- ✅ Deployment as a service (containerized)

## Project Structure

```text
14-project-devops-agent/
├── tools/                 # Tool implementations (log, k8s, yaml)
├── agent/                 # Orchestration, planning, reflection
├── configs/               # Allowlist, budgets, timeouts
├── api/                   # Service wrapper (optional)
├── tests/                 # Safety and regression tests
└── docs/                  # Usage, limits, demo guide
```text
## Skills Demonstrated

- Design safe, deterministic tools
- Implement agent loops with planning/reflection
- Add guardrails and budgets to agent actions
- Deploy agents as containerized services
- Test and monitor agent behaviors

## Duration

**Estimated Time**: 20-25 hours

## Interview Talking Points

After completing this project, you can say:

> "I built a DevOps agent that can analyze logs, interact with Kubernetes, and generate YAML safely. The agent uses an allowlisted toolset, enforced budgets/timeouts, and a reflection loop. I shipped it as a containerized service with tests covering safety scenarios."

## Deliverables

1. Working agent service with documented tools
2. Configurable guardrails (allowlist, budgets, limits)
3. Demo script or video showing safe tool use
4. Tests for key safety behaviors

## What's Next?

Move to [Section 15: Interview Prep & Career Roadmap](../15-interview-career-roadmap/README.md) to package your work for roles.
