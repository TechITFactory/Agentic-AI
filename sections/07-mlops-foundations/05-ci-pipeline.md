# CI Pipeline: Lint → Test → Build → Push Image

## Why this lesson
Automate checks so every change is validated and shipped safely.

## Outcomes
- ✅ Define CI stages for ML services
- ✅ Build/push Docker image in CI
- ✅ Fail fast on lint/tests before building

**Time**: ~30 minutes

**Prerequisites**: Tests exist; Dockerfile ready

## Agenda
- Typical CI jobs (lint, test, build, push)
- Caching deps for speed
- Secrets for registry

## Hands-on
- Author a GitHub Actions workflow with these jobs
- Push to a test registry (or dry run)

## Deliverable
- `.github/workflows/ci.yml` skeleton

## Checkpoint
Would your pipeline stop a bad PR before building an image?