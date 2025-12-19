# Section 13: Project 2 - RAG Knowledge Assistant

## 🎯 Project Overview

Build a retrieval-augmented knowledge assistant that answers with citations. This portfolio project proves you can design ingestion, retrieval, generation, and evaluation for enterprise-style RAG systems.

## What You'll Build

- ✅ Ingestion pipeline for PDF/Markdown sources
- ✅ Embedding + vector database setup
- ✅ Tuned retrieval (chunking, k, metadata filters)
- ✅ Answering with citations and grounding
- ✅ Prompt injection defenses and validation
- ✅ Evaluation report with recall@k and qualitative checks

## Project Structure

```text
13-project-rag-assistant/
├── data/                  # Sample documents
├── ingest/                # Ingestion and chunking scripts
├── retrieval/             # Vector DB setup and queries
├── generation/            # Prompt templates and response logic
├── evaluation/            # Metrics and golden set evaluation
├── api/                   # Optional API wrapper for the assistant
└── docs/                  # Setup guide and decisions
```text
## Skills Demonstrated

- Design and tune RAG pipelines
- Work with embeddings, chunking, and metadata filters
- Implement retrieval evaluation with recall@k
- Add security controls against prompt injection
- Produce documentation and demoable outputs

## Duration

**Estimated Time**: 20-25 hours

## Interview Talking Points

After completing this project, you can say:

> "I built a RAG assistant that ingests PDFs/Markdown, stores embeddings with metadata, and returns answers with citations. I tuned chunking and retrieval params, added prompt-injection defenses, and reported recall@k against a golden dataset."

## Deliverables

1. Working RAG pipeline with config-driven ingestion
2. Evaluation report (metrics + qualitative examples)
3. Documentation with setup and tuning notes
4. Optional: lightweight API or CLI for queries

## What's Next?

Move to [Section 14: Project 3 - DevOps Agent](../14-project-devops-agent/README.md) to build an agentic service that automates ops tasks.
