# Kubernetes Basics for ML Services

## Why this lesson

Deploy your containerized model in Kubernetes with the minimal set of objects.

## Outcomes

- ✅ Create Deployment + Service for the API
- ✅ Understand pods, replicas, services
- ✅ Apply manifests with kubectl

**Time**: ~30 minutes

**Prerequisites**: Container image built

## Agenda

- Core K8s objects (Pod, Deployment, Service)
- Basic manifest structure
- Applying and verifying

## Hands-on

- Write a Deployment and Service manifest for the API
- kubectl apply; verify pod ready and service responding

## Deliverable

- `k8s/deployment.yaml` and `k8s/service.yaml`

## Checkpoint

Can you reach the service via cluster IP/port after deploy?
