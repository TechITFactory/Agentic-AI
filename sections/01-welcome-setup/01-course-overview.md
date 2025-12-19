# Course Overview: What You Will Build

## Why this lesson

Orient you to the three portfolio projects and the production patterns you'll practice throughout the course.

## Outcomes

- ✅ Can describe each project, tech stack, and interview talking points
- ✅ Know how the projects ladder from traditional ML → RAG → agents
- ✅ Pick which project to personalize for your portfolio

**Time**: ~15 minutes

**Prerequisites**: None

## Welcome to Agentic AI! 🚀

This isn't just another AI course with toy examples. You're going to build **three production-ready projects** that you can showcase in interviews and use as a foundation for real-world work.

## The Three Portfolio Projects

### Project 1: MLOps Churn Prediction System 📊

**What is it?**
A complete machine learning system that predicts customer churn with full MLOps practices.

**What you'll build:**
- End-to-end ML pipeline (data processing → training → evaluation)
- Feature engineering pipeline
- Model serving API with FastAPI
- Docker containerization
- Kubernetes deployment with autoscaling
- CI/CD pipeline with GitHub Actions
- Basic monitoring setup

**Real-world use case:**
This is exactly how companies deploy ML models in production. Whether it's predicting churn, fraud, or recommendations, the pattern is the same.

**Interview talking points:**
- "I built a production ML pipeline that handles..."
- "I implemented CI/CD for model deployment..."
- "I configured Kubernetes autoscaling for ML inference..."

**Tech stack:** Python, scikit-learn, XGBoost, FastAPI, Docker, Kubernetes

---

### Project 2: RAG Knowledge Assistant 📚

**What is it?**
A Retrieval-Augmented Generation system that answers questions from your documents with proper citations - no hallucinations.

**What you'll build:**
- Document ingestion pipeline (PDF, Markdown)
- Text chunking with optimal strategies
- Vector embeddings and similarity search
- Retrieval pipeline with metadata filtering
- LLM-powered answer generation with citations
- Prompt injection defenses
- Evaluation framework with golden dataset

**Real-world use case:**
Every company wants to "chat with their docs" - internal wikis, support docs, legal documents. You'll build the real thing, not a demo.

**Interview talking points:**
- "I implemented RAG with retrieval evaluation at recall@k..."
- "I built chunking strategies that improved answer quality by..."
- "I added security measures against prompt injection..."

**Tech stack:** Python, OpenAI API, ChromaDB/FAISS, LangChain, sentence-transformers

---

### Project 3: DevOps Agent (Agentic AI) 🤖

**What is it?**
An autonomous AI agent that can analyze logs, interact with Kubernetes, and generate YAML configs - safely.

**What you'll build:**
- Agent with Plan → Act → Observe → Reflect loop
- Safe, deterministic tools (log analyzer, k8s helper, YAML generator)
- Tool execution with guardrails and timeouts
- Short-term and long-term memory
- Multi-step workflow orchestration
- Agent deployment as a service

**Real-world use case:**
Agentic AI is the future - agents that can automate complex workflows. This project shows you understand the architecture and safety concerns.

**Interview talking points:**
- "I built an autonomous agent with proper guardrails..."
- "I implemented tool execution with timeout and safety checks..."
- "I designed tools following deterministic principles..."

**Tech stack:** Python, OpenAI API with function calling, Docker, Kubernetes API

---

## Why These Three Projects?

1. **Coverage**: Traditional ML + Modern LLMs + Cutting-edge Agents
2. **Production-Ready**: Not toys - these use real deployment patterns
3. **Interview Gold**: Each project gives you multiple talking points
4. **Progressive Complexity**: Build skills incrementally
5. **Portfolio Worthy**: Deploy these and share the links

## What You WON'T Build (And Why)

❌ **Image Classification**: Overcrowded, everyone does it
❌ **Sentiment Analysis**: Too basic for 2024+
❌ **Simple Chatbot**: No agentic capabilities, not impressive
❌ **Kaggle Competition Entry**: Great for learning, but not production-focused

Instead, you'll build systems that companies actually deploy and maintain.

## Course Philosophy: "Minimum DS + Maximum Practical"

You don't need a PhD in statistics to build AI systems. You need:

- **Just-Enough Theory**: Understand what you're doing and why
- **Production Patterns**: Deployment, monitoring, CI/CD
- **Security Awareness**: Prompt injection, data validation
- **Real Tools**: What companies actually use

We'll skip:
- Deep mathematical proofs
- 50 different ML algorithms
- Academic papers (unless directly useful)
- Theoretical exercises without practical application

## Learning Path Through the Course

```
Foundation (Weeks 1-2)
└─ Python + Data Science basics

ML Engineering (Weeks 3-4)
└─ ML models + Serving + MLOps

Modern AI (Weeks 5-6)
└─ LLMs + RAG + Agents

Build Phase (Weeks 7-12)
└─ Three Portfolio Projects

Career Prep (Week 13)
└─ Interview prep + Resume
```

## Who This Course Is NOT For

Be honest with yourself - this course requires:

- ❌ **No programming experience**: Learn Python basics first
- ❌ **Only want to use no-code tools**: This is a code-focused course
- ❌ **Want to become a Data Scientist**: This is engineering, not research
- ❌ **Expect no effort required**: You'll need to code and debug

## Who This Course IS For

✅ **DevOps/SRE Engineers**: Add AI to your stack
✅ **Backend Developers**: Transition to AI engineering
✅ **Junior ML Engineers**: Learn production deployment
✅ **Career Switchers**: With programming background
✅ **Ambitious Learners**: Want real portfolio projects

## Time Commitment

- **Total Course**: 80-120 hours
- **Per Week**: 8-10 hours recommended
- **Duration**: 10-12 weeks at steady pace
- **Flexibility**: Self-paced, go faster or slower

## What's Next?

Before diving into code, you need to understand the different AI roles so you can position yourself correctly in the job market.

**Next Lesson**: [AI Roles Explained](./02-ai-roles-explained.md)

---

## Success Stories (What Past Students Built)

While this is a new course format, the patterns taught here are used by:

- **Startups**: Building RAG for customer support
- **Enterprises**: Deploying ML models at scale
- **DevOps Teams**: Using agents for automation
- **Solo Developers**: Creating SaaS products with AI

**You'll build the same patterns they use.**

## Questions Before Starting?

- **"Do I need a GPU?"** No, we'll use APIs and CPU-based tools
- **"How much will APIs cost?"** ~$10-30 for the entire course
- **"Can I skip sections?"** Not recommended, they build on each other
- **"What if I get stuck?"** Use GitHub Issues and Discussions

---

Ready to understand the AI career landscape? Let's go! 👉 [AI Roles Explained](./02-ai-roles-explained.md)
