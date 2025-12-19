# Course Overview: What You Will Build

## Why this lesson

Orient you to the three portfolio projects and the production patterns you'll practice throughout the course.

## Outcomes

-  Can describe each project, tech stack, and interview talking points
-  Know how the projects ladder from traditional ML  RAG  agents
-  Pick which project to personalize for your portfolio

**Time**: ~15 minutes

**Prerequisites**: None

---

##  Welcome to Agentic AI!

Welcome to the **Agentic AI Engineering** course. I'm thrilled you're here.

If you're reading this, you probably know that AI is moving fast—really fast. But there's a gap. There are thousands of tutorials on "how to make a chatbot" or "how to run a model in a notebook," but very few resources teach you **how to build production-grade AI systems**.

That's exactly what this course is about. We are not here to build toys. We are here to build **three production-ready projects** that you can deploy, put on your resume, and talk about confidently in senior-level interviews.

This course is designed to take you from "I know some Python" to "I can architect and deploy an autonomous AI agent."

---

##  The Three Portfolio Projects

We believe the best way to learn is by building. You won't just be watching videos; you'll be writing code, debugging errors, and shipping software. Here are the three major milestones of your journey.

### Project 1: MLOps Churn Prediction System 

**The Foundation**

Before we get to LLMs and Agents, you need to understand the backbone of AI engineering: **MLOps**. In this project, you will build a complete end-to-end machine learning system to predict customer churn.

**Why this matters:**
Most "AI" jobs are actually "ML Engineering" jobs. Companies need people who can take a model from a Jupyter notebook and wrap it in an API, containerize it with Docker, and deploy it to Kubernetes.

**What you will build:**
- A data processing pipeline that cleans and prepares real-world data.
- A training pipeline using **XGBoost** and **scikit-learn**.
- A high-performance API using **FastAPI** to serve predictions.
- A **Docker** container to package your application.
- A **Kubernetes** deployment with autoscaling to handle traffic spikes.
- A **CI/CD pipeline** using GitHub Actions to automate testing and deployment.

**Interview Talking Point:**
> "I built a production ML pipeline that handles data ingestion, training, and serving. I implemented CI/CD for automated deployment and configured Kubernetes autoscaling to handle load."

---

### Project 2: RAG Knowledge Assistant 

**The Modern Standard**

Once you have the MLOps foundation, we move to the most common use case for LLMs today: **Retrieval-Augmented Generation (RAG)**. You will build a system that lets users "chat with their documents" without hallucinations.

**Why this matters:**
Every company has internal documents—PDFs, wikis, support tickets—and they all want an AI that can answer questions based on that data. Building a *good* RAG system is harder than it looks.

**What you will build:**
- An ingestion pipeline to parse PDFs and Markdown files.
- A vector database setup using **ChromaDB** or **FAISS**.
- A retrieval system with **semantic search** and metadata filtering.
- An LLM integration (using **OpenAI** or open-source models) that cites its sources.
- **Security guardrails** to prevent prompt injection attacks.
- An evaluation framework to measure retrieval quality (Recall@k).

**Interview Talking Point:**
> "I architected a RAG system that ingests unstructured data and delivers cited answers. I focused heavily on evaluation, using a golden dataset to tune chunking strategies and improve retrieval recall by 20%."

---

### Project 3: DevOps Agent (Agentic AI) 

**The Cutting Edge**

Finally, we reach the frontier of AI engineering: **Autonomous Agents**. You will build an AI agent that can actually *do* things—specifically, a DevOps assistant that can debug your Kubernetes cluster.

**Why this matters:**
Chatbots are passive; agents are active. The future of AI is systems that can plan, execute tools, observe results, and correct their own errors. This is where the industry is heading.

**What you will build:**
- An agent loop based on the **ReAct (Reason + Act)** pattern.
- A set of **safe, deterministic tools** (Log Analyzer, YAML Generator, K8s Inspector).
- A **memory system** to handle multi-step reasoning.
- **Strict guardrails** to ensure the agent doesn't delete production databases.
- A deployment strategy to run this agent as a scalable service.

**Interview Talking Point:**
> "I built an autonomous DevOps agent that can troubleshoot infrastructure issues. I implemented a custom tool-use loop with strict safety guardrails and budget limits to ensure deterministic and safe behavior in production."

---

##  Course Philosophy: "Minimum DS + Maximum Practical"

You might be asking: *"Do I need a PhD in Math to take this course?"*

The answer is **No**.

Our philosophy is **Minimum Data Science, Maximum Practical Engineering**.

### What we SKIP 
- Deep mathematical proofs of backpropagation.
- Deriving gradient descent by hand.
- 50 different legacy ML algorithms you'll never use.
- Academic theory without application.

### What we FOCUS ON 
- **System Architecture**: How do the pieces fit together?
- **Production Patterns**: Logging, monitoring, error handling.
- **Security**: How to stop prompt injections and data leakage.
- **Tooling**: Docker, Kubernetes, GitHub Actions, Vector DBs.

We teach you just enough theory to understand *why* things work, and then we immediately switch to *how* to build them.

---

##  Learning Path

Here is how we will structure your learning over the next 10-12 weeks:

1.  **Foundation (Weeks 1-2)**: Python refresher, Data Science basics (Pandas/NumPy).
2.  **ML Engineering (Weeks 3-4)**: Building and serving traditional ML models.
3.  **Modern AI (Weeks 5-6)**: LLM fundamentals, Embeddings, and Vector DBs.
4.  **Build Phase (Weeks 7-12)**: The three portfolio projects.
5.  **Career Prep (Week 13)**: Resume tailoring, system design interviews, and career roadmap.

---

##  Who Is This Course For?

Be honest with yourself. This course is challenging.

**This course is for you if:**
-  You are a **Software Engineer** wanting to switch to AI.
-  You are a **DevOps/SRE** wanting to build AI tools.
-  You are a **Junior ML Engineer** wanting to learn production standards.
-  You are willing to write code, debug errors, and read documentation.

**This course is NOT for you if:**
-  You have never written code before (please learn Python basics first).
-  You only want to use "no-code" drag-and-drop tools.
-  You want to be a pure Data Scientist (focusing on statistics/research).
-  You expect everything to work perfectly without effort.

---

##  What's Next?

Before we write a single line of code, we need to understand the landscape. The term "AI Engineer" is used loosely. In the next lesson, we will break down the different roles—Data Scientist, ML Engineer, AI Engineer—so you can decide exactly which path you want to take.

**Next Lesson**: [AI Roles Explained](./02-ai-roles-explained.md)