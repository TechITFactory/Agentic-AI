# Agentic AI Engineering (Udemy-Style Course Structure + Transcript)

This document is a **course blueprint** (what you would publish as an Udemy curriculum + lecture transcript notes).
It is mapped to the repo’s existing folders under `sections/`.

## Course Promise
Build 3 portfolio-grade systems:
1) MLOps churn prediction service
2) RAG knowledge assistant with citations + evaluation
3) DevOps agent with tool-use + guardrails

## Target Learner
Software engineers / DevOps/SRE / junior ML engineers who can code and want **production AI engineering**.

## How to Use This Repo
- Read the lecture markdowns in each section.
- Run code in `code/` (or project folders) from an activated venv.
- Complete labs in `labs/`.

---

## Section 01 — Welcome & Setup (Repo: `sections/01-welcome-setup/`)

### 1.1 Course Overview: What You Will Build
- Outcome: Understand the 3 projects, expectations, and milestones.
- Lecture script:
  - "This course is about shipping production systems—not notebooks."
  - Walk through Project 1 → Project 2 → Project 3 and what skills each adds.

### 1.2 AI Roles Explained: Pick Your Target Role
- Outcome: Choose ML Engineer vs AI Engineer emphasis.
- Lecture script:
  - Define DS vs MLE vs AI Eng vs MLOps.
  - Explain how the projects map to each role.

### 1.3 Learning Path: Minimum DS, Maximum Practical
- Outcome: Understand the sequencing and recommended weekly schedule.
- Lecture script:
  - Explain why we skip deep proofs.
  - Explain what “production-ready” means (tests, logging, containers, CI).

### 1.4 Tools Installation Guide
- Outcome: Python + editor + Docker working; repo runs locally.
- Lecture script:
  - "Your environment is your workshop—fix it now, not later."
  - Show Windows/Mac/Linux verification.

### 1.5 Repository Walkthrough
- Outcome: Know where docs vs runnable code vs labs live.
- Lecture script:
  - Explain section anatomy.
  - Explain how to track progress (branching/checklists).

Assignment (end of Section 01):
- Run `.\scripts\setup.ps1` (Windows) OR manual venv setup.
- Run `python ./scripts/verify_env.py` successfully.

---

## Section 02 — Python for AI (Repo: `sections/02-python-for-ai/`)

Lectures:
- 2.1 Python Crash Course for Engineers (types, iterables, funcs)
- 2.2 Type hints + tooling (mypy mindset)
- 2.3 NumPy essentials for ML
- 2.4 Pandas essentials + common pitfalls
- 2.5 IO patterns: CSV/JSON/Parquet, schemas, dtypes

Labs:
- Data cleaning lab: missing values, leakage traps, reproducible preprocessing.

Milestone:
- Build a clean, reusable dataset loader + validator.

---

## Section 03 — Data Science Fundamentals (Repo: `sections/03-data-science-fundamentals/`)

Lectures:
- 3.1 Datasets, splits, and leakage (with examples)
- 3.2 Baselines + why they matter
- 3.3 Metrics for classification: precision/recall/F1/AUC
- 3.4 Metrics for regression: MAE/RMSE/R2
- 3.5 Overfitting: detection + fixes

Labs:
- Build a baseline churn model and evaluate correctly.

Milestone:
- A repeatable evaluation script with saved metrics.

---

## Section 04 — Machine Learning Basics (Repo: `sections/04-machine-learning-basics/`)

Lectures:
- 4.1 Regression + classification (what to use when)
- 4.2 Tree-based models: decision trees, random forests
- 4.3 XGBoost: practical tuning + stopping overfitting
- 4.4 Feature engineering patterns (categoricals, scaling, leakage avoidance)
- 4.5 Persisting models (joblib) + reproducibility

Lab:
- Train a churn model with a clean pipeline and store artifacts.

Milestone:
- One command trains and writes `artifacts/`.

---

## Section 05 — Model Serving (Repo: `sections/05-model-serving/`)

Lectures:
- 5.1 Serving patterns: batch vs realtime
- 5.2 FastAPI: request validation, response schemas
- 5.3 Logging + correlation IDs
- 5.4 Testing APIs (pytest + httpx)
- 5.5 Load testing basics + latency budgets

Lab:
- Add one endpoint and a test for it.

Milestone:
- A containerized API that passes tests.

---

## Section 06 — Containers & Deployment (Repo: `sections/06-containers-deployment/`)

Lectures:
- 6.1 Docker fundamentals for ML services
- 6.2 Dockerfile best practices (multi-stage, non-root)
- 6.3 Kubernetes basics: Deployments/Services
- 6.4 Health checks: readiness/liveness
- 6.5 Autoscaling (HPA) and resource requests

Lab:
- Deploy the FastAPI model server to a local k8s cluster (kind/minikube).

Milestone:
- You can `kubectl apply` and hit a prediction endpoint.

---

## Section 07 — MLOps Foundations (Repo: `sections/07-mlops-foundations/`)

Lectures:
- 7.1 What “MLOps” really means
- 7.2 Reproducible pipelines (configs, seeds, artifacts)
- 7.3 Testing strategy for ML (unit + integration + data tests)
- 7.4 CI/CD basics (quality gates)
- 7.5 Monitoring: data drift vs model drift

Lab:
- Add a CI workflow that runs lint + unit tests.

Milestone:
- Every PR runs checks automatically.

---

## Section 08 — Intro to LLMs (Repo: `sections/08-intro-llms/`)

Lectures:
- 8.1 Tokens, context windows, temperature
- 8.2 Prompting patterns that survive production
- 8.3 Function calling / tool calling
- 8.4 Safety basics: injection, secrets, PII

Lab:
- Build a simple tool-calling CLI that calls a calculator and a file search tool.

---

## Section 09 — Embeddings & Vector DBs (Repo: `sections/09-embeddings-vector-dbs/`)

Lectures:
- 9.1 Embeddings: meaning in vectors
- 9.2 Chunking strategies and tradeoffs
- 9.3 Vector DB fundamentals (Chroma/FAISS)
- 9.4 Retrieval evaluation (Recall@k)

Lab:
- Index a small document set and run semantic search.

---

## Section 10 — RAG End-to-End (Repo: `sections/10-rag-end-to-end/`)

Lectures:
- 10.1 RAG architecture: ingestion → index → retrieve → generate
- 10.2 Citations done right
- 10.3 Guardrails: prompt injection + data boundaries
- 10.4 Offline evaluation with a golden dataset

Milestone:
- A RAG service that returns answers + citations + confidence.

---

## Section 11 — Agentic AI (Repo: `sections/11-agentic-ai/`)

Lectures:
- 11.1 Agent loop fundamentals (ReAct)
- 11.2 Tools: deterministic boundaries
- 11.3 Memory: what to store, when to summarize
- 11.4 Guardrails: permissions, budgets, and audit logs

Lab:
- Implement a safe tool runner with allowlists and timeouts.

---

## Section 12 — Project 1: MLOps Churn System (Repo: `sections/12-project-mlops-churn/` + `churn-mlops-prod/`)

Deliverables:
- Training pipeline
- Registry/artifacts
- FastAPI prediction service
- Docker + Kubernetes deployment
- Monitoring basics

Milestone:
- Production runbook: “how to train, deploy, rollback, monitor”.

---

## Section 13 — Project 2: RAG Assistant (Repo: `sections/13-project-rag-assistant/`)

Deliverables:
- Ingestion pipeline
- Vector DB index
- RAG API with citations
- Eval harness

Milestone:
- A demo that works with your own documents.

---

## Section 14 — Project 3: DevOps Agent (Repo: `sections/14-project-devops-agent/`)

Deliverables:
- Tool-use agent loop
- Safe tools (log analyzer, yaml inspector, k8s read-only)
- Guardrails + audit

Milestone:
- A CLI or API that can troubleshoot common cluster issues safely.

---

## Section 15 — Interview & Career Roadmap (Repo: `sections/15-interview-career-roadmap/`)

Lectures:
- Portfolio storytelling
- System design: "Design a RAG system"
- Troubleshooting: "why is my model drifting"

Deliverable:
- A 1-page resume bullet bank + project narratives.

---

## Section 16 — Bonus Advanced (Repo: `sections/16-bonus-advanced/`)

Optional modules:
- Fine-tuning vs RAG tradeoffs
- Performance optimization
- Production hardening patterns

---

## Recommended Structure Tweaks (Minimal)

1) Standardize section layout to:
- `README.md`
- numbered lecture markdowns
- `code/` for runnable examples
- `labs/` for exercises (starter + solution)

2) Add one “course-wide” execution entrypoint:
- Windows: `.\scripts\setup.ps1`
- All OS: `python ./scripts/verify_env.py`

3) Add explicit checkpoints:
- End of Sections 03, 05, 07, 10, 11: a small “ship it” deliverable.
