# Autoscaling with HPA

## Why this lesson
Scale the API automatically under load using CPU or custom metrics.

## Outcomes
- ✅ Configure a Horizontal Pod Autoscaler for the API
- ✅ Choose sensible CPU targets for inference
- ✅ Observe scale-out and scale-in behavior

**Time**: ~20 minutes

**Prerequisites**: Deployment/Service in K8s

## Agenda
- HPA basics and metrics
- Setting min/max replicas and targets
- Observing scaling events

## Hands-on
- Create HPA manifest targeting CPU
- Generate load; watch pods scale

## Deliverable
- `k8s/hpa.yaml` and a short note on observed scaling

## Checkpoint
Can you explain when you’d switch from CPU to custom latency metrics?