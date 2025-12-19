# Mini Lab: Deploy API to Kubernetes

## Why this lab

Practice the full flow: build image, deploy to K8s, add probes, and autoscale.

## Outcomes

- ✅ Build and push image
- ✅ Deploy with readiness/liveness probes
- ✅ Apply HPA and observe scaling

**Time**: ~90 minutes

**Prerequisites**: All prior Section 6 lessons

## Tasks

1) Build and push your API image (local registry or Docker Hub)
2) Apply Deployment/Service manifests with probes
3) Configure HPA (CPU target)
4) Generate load; capture p95 latency and replica changes
5) Note issues and fixes for production

## Deliverables

- Manifests in `k8s/`
- Brief lab report with commands, metrics, and outcomes

## Checkpoint

Could another engineer reproduce your deploy and see pods scale under the same load?
