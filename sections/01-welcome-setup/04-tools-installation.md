# Tools Installation Guide

## Why this lesson

Install and verify every tool required for the rest of the course so you do not debug environment issues later.

## Outcomes

- ✅ Python 3.10+, VS Code, Git, Docker Desktop installed and verified
- ✅ Repo cloned and virtual environment created
- ✅ Jupyter works from VS Code or terminal

**Time**: 30-45 minutes depending on network speed

**Prerequisites**: Admin rights on your machine, stable internet

---

##  Your Environment is Your Workshop

Imagine a carpenter trying to build a house with a dull saw and a broken hammer. It would be miserable.

The same is true for AI Engineering. If your environment is broken—if Python crashes, or Docker won't start—you will spend 90% of your time fighting your computer instead of learning.

We are going to set up a **professional-grade development environment**. This is the exact same setup used by engineers at top tech companies.

---

## 🛠️ The Toolset

### 1. Python 3.10+ 🐍
**Why?**
We need Python 3.10 or newer because we use modern features like **Type Hints** (for better code quality) and **Match Statements** (for cleaner logic). Also, many modern AI libraries (like LangChain) require newer Python versions.

**Installation:**
-   **Windows**: Download from [python.org](https://www.python.org/downloads/). **CRITICAL**: Check the box that says **"Add Python to PATH"** during installation.
-   **Mac**: Use Homebrew: `brew install python@3.11`
-   **Linux**: `sudo apt install python3.11`

**Verify:**
```bash
python --version
# Should be >= 3.10
```

### 2. Visual Studio Code (VS Code) 
**Why?**
It is the industry standard. It has incredible support for Python, Jupyter Notebooks, and Docker.

**Extensions to Install:**
-   **Python** (Microsoft)
-   **Pylance** (Microsoft) - For super-fast autocompletion.
-   **Jupyter** (Microsoft) - To run notebooks directly in the editor.
-   **Docker** (Microsoft) - To manage containers.

### 3. Git 
**Why?**
You cannot be an engineer without version control. We will use Git to download the course materials and track your own progress.

**Installation:**
-   **Windows**: [Git for Windows](https://git-scm.com/download/win)
-   **Mac**: `brew install git`
-   **Linux**: `sudo apt install git`

### 4. Docker Desktop 
**Why?**
"It works on my machine" is the most dangerous phrase in engineering. Docker ensures that if your code runs on your laptop, it will run in production. We use it for the MLOps and Agent projects.

**Installation:**
-   Download [Docker Desktop](https://www.docker.com/products/docker-desktop/).
-   **Windows Users**: You MUST enable **WSL 2** (Windows Subsystem for Linux) for Docker to work properly.

---

##  Setting Up the Course Repo

Now that you have the tools, let's get the code.

1.  **Clone the Repository**:
    Open your terminal (PowerShell on Windows, Terminal on Mac/Linux) and run:
    ```bash
    git clone https://github.com/TechITFactory/Agentic-AI.git
    cd Agentic-AI
    ```

2.  **Create a Virtual Environment**:
    Never install packages globally. Always use a virtual environment.
    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\activate

    # Mac/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

---

##  Verification Checklist

Before moving on, run this quick check. If you can check all these boxes, you are ready.

- [ ] `python --version` returns 3.10 or higher.
- [ ] `docker --version` returns a version number (Docker is running).
- [ ] You can open VS Code by typing `code .` in the repo folder.
- [ ] You have activated your virtual environment (you see `(venv)` in your terminal).

---

##  What's Next?

Your workshop is ready. Now, let's take a tour of the materials.

**Next Lesson**: [Repository Walkthrough](./05-repository-walkthrough.md)