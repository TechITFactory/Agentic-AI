# Section 12: Project 1 - MLOps Churn Prediction System

## 🎯 Project Overview

Build a complete MLOps system for predicting customer churn. This is your first portfolio project - it demonstrates end-to-end ML engineering skills.

## What You'll Build

A production-ready ML system with:
- ✅ Data processing pipeline
- ✅ Feature engineering
- ✅ Model training with experiment tracking
- ✅ Model evaluation and selection
- ✅ FastAPI prediction service
- ✅ Docker containerization
- ✅ Kubernetes deployment with autoscaling
- ✅ CI/CD pipeline (GitHub Actions)
- ✅ Basic monitoring setup

## Project Structure

```
12-project-mlops-churn/
├── data/                  # Dataset
├── notebooks/            # EDA and experiments
├── src/
│   ├── data/            # Data processing
│   ├── features/        # Feature engineering
│   ├── models/          # Training scripts
│   └── api/             # FastAPI service
├── tests/               # Unit tests
├── docker/              # Docker configs
├── k8s/                 # Kubernetes manifests
├── .github/workflows/   # CI/CD
└── docs/                # Documentation
```

## Skills Demonstrated

This project proves you can:
- Build ML pipelines from scratch
- Deploy models as production APIs
- Use containerization and orchestration
- Implement CI/CD for ML services
- Think about monitoring and maintenance

## Duration

**Estimated Time**: 20-25 hours

## Interview Talking Points

After completing this project, you can say:

> "I built an end-to-end ML system that predicts customer churn with 85% accuracy. The system includes automated data processing, feature engineering, and model training. I deployed it as a FastAPI service in Kubernetes with autoscaling, and set up CI/CD with GitHub Actions. The system handles 1000+ predictions per second with <100ms latency."

## Deliverables

1. Working code in GitHub repository
2. Deployed API (can be local Kubernetes)
3. Documentation (README with setup instructions)
4. Demo video (optional but recommended)

## What's Next?

Move to [Section 13: Project 2 - RAG Knowledge Assistant](../13-project-rag-assistant/README.md) to build your LLM application.
