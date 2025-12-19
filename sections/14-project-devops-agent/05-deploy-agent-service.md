# Deploy Agent as a Service

## Why this module

Expose the agent via an API with the same production discipline as the ML services.

## Outcomes

- ✅ API wrapper (FastAPI) around the agent loop
- ✅ Container image and optional K8s manifests
- ✅ Basic auth/logging

**Time**: ~45-60 minutes

**Tasks
1) Wrap agent in an API endpoint
2) Containerize and run locally
3) (Optional) Deploy to K8s with probes

**Deliverable
- API wrapper code, Dockerfile, and manifests

**Checkpoint
Can a user call the agent API and see bounded, logged tool calls?
