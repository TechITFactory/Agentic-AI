# Health Probes for ML APIs

## Why this lesson

Ensure Kubernetes only routes traffic to healthy pods and restarts bad ones.

## Outcomes

- ✅ Add readiness and liveness probes
- ✅ Choose probe endpoints and thresholds
- ✅ Understand differences and failure handling

**Time**: ~20 minutes

**Prerequisites**: K8s manifests from prior lesson

## Agenda

- Readiness vs liveness
- Probe config options (path, initialDelaySeconds, periodSeconds)
- Common ML pitfalls (slow load)

## Hands-on

- Add probes to Deployment; redeploy
- Simulate failures; observe restarts

## Deliverable

- Updated Deployment manifest with probes

## Checkpoint

Do probes prevent traffic to pods that are still loading the model?
