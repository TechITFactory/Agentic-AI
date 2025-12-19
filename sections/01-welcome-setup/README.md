# Section 1: Welcome & Setup

Get oriented, pick your target role, and stand up a working dev environment before writing any course code.

## What You'll Learn

1. **Course Overview**: The three production projects you will ship
2. **AI Roles Explained**: DS vs ML Engineer vs AI/LLM Engineer vs MLOps
3. **Learning Path**: "Minimum DS + Maximum Practical" roadmap
4. **Tools Setup**: Python, VS Code, Git, Jupyter, Docker
5. **Repo Walkthrough**: How to use the materials efficiently

## Lessons

1. [Course Overview - What You Will Build](./01-course-overview.md)
2. [AI Roles Explained](./02-ai-roles-explained.md)
3. [Learning Path & Philosophy](./03-learning-path.md)
4. [Tools Installation Guide](./04-tools-installation.md)
5. [Repository Walkthrough](./05-repository-walkthrough.md)

## Outcomes

- ✅ You know the three portfolio projects and target roles
- ✅ Your machine has Python 3.10+, VS Code, Git, Docker working
- ✅ You cloned the repo and activated a virtual environment
- ✅ You can run a Jupyter notebook from the repo

## Duration

**Estimated Time**: 1-2 hours (faster if tools already installed)

## Prerequisites

- Computer with admin rights (Windows, macOS, or Linux)
- Internet connection
- Willingness to build, not just watch

## Quick Setup Checklist

- [ ] Install Python 3.10+ and verify `python --version`
- [ ] Install VS Code + Python/Jupyter extensions
- [ ] Install Git and configure name/email
- [ ] Install Docker Desktop (enable WSL2 on Windows)
- [ ] Clone the repo `git clone https://github.com/TechITFactory/Agentic-AI.git`
- [ ] Create and activate `venv`
- [ ] `pip install -r requirements.txt`
- [ ] Run `python -c "print('env ok')"`
- [ ] Launch `jupyter lab` or VS Code notebook to confirm kernel

## Fast Commands (Windows PowerShell)

```powershell

# From a workspace folder of your choice

python -m venv venv; .\venv\Scripts\activate; pip install --upgrade pip
pip install -r requirements.txt
jupyter --version
```text
## What's Next?

Once the checklist is green, move to [Section 2: Python for AI](../02-python-for-ai/README.md). If any tool fails, fix it now—every later section assumes this environment is solid.
