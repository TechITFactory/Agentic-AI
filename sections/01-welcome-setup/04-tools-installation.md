# Tools Installation Guide

## Why this lesson

Install and verify every tool required for the rest of the course so you do not debug environment issues later.

## Outcomes

- ✅ Python 3.10+, VS Code, Git, Docker Desktop installed and verified
- ✅ Repo cloned and virtual environment created
- ✅ Jupyter works from VS Code or terminal

**Time**: 30-45 minutes depending on network speed

**Prerequisites**: Admin rights on your machine, stable internet

## Overview

This guide will help you set up your development environment for the course. All tools are free and work on Windows, Mac, and Linux.

## Required Tools Checklist

- [ ] Python 3.10 or higher
- [ ] VS Code (or your preferred IDE)
- [ ] Git
- [ ] Docker Desktop
- [ ] Course repository cloned

## Optional but Recommended

- [ ] Terminal/Shell (Windows Terminal for Windows)
- [ ] Postman or similar API testing tool

---

## 1. Python Installation

### Why Python 3.10+?

We use features from Python 3.10+ (type hints, match statements) and newer library versions require it.

### Windows

**Option 1: Microsoft Store (Recommended)**
```bash

# Search "Python 3.11" in Microsoft Store and install

```

**Option 2: Official Installer**
1. Visit https://www.python.org/downloads/
2. Download Python 3.11 or 3.12 installer
3. **Important**: Check "Add Python to PATH" during installation
4. Verify installation:
```bash
python --version

# Should show Python 3.10 or higher

```

### macOS

**Option 1: Homebrew (Recommended)**
```bash

# Install Homebrew if not installed

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python

brew install python@3.11

# Verify

python3 --version
```

**Option 2: Official Installer**
1. Visit https://www.python.org/downloads/
2. Download macOS installer
3. Run the installer
4. Verify in Terminal

### Linux (Ubuntu/Debian)

```bash

# Update package list

sudo apt update

# Install Python 3.11

sudo apt install python3.11 python3.11-venv python3-pip

# Verify

python3.11 --version
```

### Verify Installation

```bash

# Check Python version

python --version  # or python3 --version

# Check pip

pip --version  # or pip3 --version

# Test Python

python -c "print('Python is working!')"
```

---

## 2. VS Code Installation

### Why VS Code?

- Free and lightweight
- Excellent Python support
- Integrated terminal
- Great extensions for ML/AI

### Download and Install

1. Visit https://code.visualstudio.com/
2. Download for your OS
3. Install with default settings

### Essential Extensions

Open VS Code and install these extensions (Ctrl+Shift+X / Cmd+Shift+X):

1. **Python** (Microsoft) - Python language support
2. **Jupyter** (Microsoft) - Notebook support
3. **Pylance** (Microsoft) - Fast Python language server
4. **Docker** (Microsoft) - Docker file support
5. **YAML** (Red Hat) - YAML syntax support

### Configure Python

1. Open Command Palette (Ctrl+Shift+P / Cmd+Shift+P)
2. Type "Python: Select Interpreter"
3. Choose your Python 3.10+ installation

### Optional but Useful Extensions

- **GitLens** - Enhanced Git capabilities
- **Error Lens** - Inline error messages
- **Thunder Client** - API testing (like Postman)
- **Better Comments** - Color-coded comments

---

## 3. Git Installation

### Why Git?

- Version control for your code
- Clone course repository
- Track your progress
- Essential for any developer

### Windows

**Option 1: Git for Windows (Recommended)**
```bash

# Download from https://git-scm.com/download/win

# Run installer with default settings

```

**Option 2: GitHub Desktop**
- More user-friendly GUI
- Download from https://desktop.github.com/

### macOS

**Option 1: Homebrew**
```bash
brew install git
```

**Option 2: Xcode Command Line Tools**
```bash
xcode-select --install
```

### Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install git
```

### Verify Installation

```bash
git --version

# Should show git version 2.x or higher

```

### Configure Git

```bash

# Set your name and email

git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Verify configuration

git config --list
```

---

## 4. Docker Desktop Installation

### Why Docker?

- Containerize ML applications
- Consistent environments across machines
- Deploy to cloud/Kubernetes
- Industry standard for deployment

### Windows

**Requirements**:
- Windows 10/11 Pro, Enterprise, or Education
- WSL 2 enabled (we'll set this up)

**Steps**:

1. **Enable WSL 2**:
```powershell

# Run PowerShell as Administrator

wsl --install

# Restart computer

```

2. **Install Docker Desktop**:
- Download from https://www.docker.com/products/docker-desktop
- Run installer
- Start Docker Desktop
- In Settings, ensure "Use WSL 2 based engine" is checked

### macOS

**Requirements**:
- macOS 10.15 or higher
- Apple Silicon or Intel chip

**Steps**:
1. Download from https://www.docker.com/products/docker-desktop
2. Install Docker Desktop
3. Start Docker Desktop
4. Allow in System Preferences if prompted

### Linux (Ubuntu)

```bash

# Remove old versions

sudo apt remove docker docker-engine docker.io containerd runc

# Install Docker

curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Add user to docker group (avoid sudo)

sudo usermod -aG docker $USER

# Log out and back in, then verify

docker --version
```

### Verify Docker Installation

```bash

# Check Docker version

docker --version

# Run test container

docker run hello-world

# Should see "Hello from Docker!" message

```

### Docker Desktop Settings

**Recommended settings**:
- Resources → Memory: 4GB minimum (8GB better)
- Resources → CPUs: 2 minimum (4 better)
- Enable Kubernetes (optional, for Section 6)

---

## 5. Clone Course Repository

### Using Git Command Line

```bash

# Navigate to where you want the course folder

cd ~/projects  # or C:\projects on Windows

# Clone repository

git clone https://github.com/TechITFactory/Agentic-AI.git

# Navigate into repository

cd Agentic-AI

# Verify you're on the right branch

git branch
```

### Using VS Code

1. Open VS Code
2. Press Ctrl+Shift+P (Cmd+Shift+P on Mac)
3. Type "Git: Clone"
4. Enter repository URL: `https://github.com/TechITFactory/Agentic-AI.git`
5. Choose folder location
6. Open cloned repository

### Using GitHub Desktop

1. Open GitHub Desktop
2. File → Clone Repository
3. URL tab: Enter `https://github.com/TechITFactory/Agentic-AI.git`
4. Choose local path
5. Click "Clone"

---

## 6. Set Up Python Environment

### Why Virtual Environments?

- Isolate project dependencies
- Avoid version conflicts
- Keep system Python clean
- Industry best practice

### Create Virtual Environment

**Windows**:
```bash

# Navigate to course directory

cd C:\path\to\Agentic-AI

# Create virtual environment

python -m venv venv

# Activate it

venv\Scripts\activate

# You should see (venv) in your prompt

```

**macOS/Linux**:
```bash

# Navigate to course directory

cd ~/path/to/Agentic-AI

# Create virtual environment

python3 -m venv venv

# Activate it

source venv/bin/activate

# You should see (venv) in your prompt

```

### Install Course Dependencies

```bash

# Make sure virtual environment is activated

# You should see (venv) in your prompt

# Upgrade pip

pip install --upgrade pip

# Install all course requirements

pip install -r requirements.txt

# This will take a few minutes

```

### Verify Installation

```bash

# Test imports

python -c "import numpy; import pandas; import sklearn; print('All imports successful!')"

# List installed packages

pip list
```

---

## 7. Jupyter Notebook Setup

### Launch Jupyter

```bash

# With virtual environment activated

jupyter notebook

# Or use Jupyter Lab (modern interface)

jupyter lab

# Browser should open automatically

```

### VS Code Jupyter Integration

1. Open any `.ipynb` file in VS Code
2. VS Code will prompt to select kernel
3. Choose your virtual environment's Python
4. You can now run notebooks in VS Code!

### Test Jupyter

Create a test notebook:

```python

# Cell 1: Test imports

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
print("Imports successful!")

# Cell 2: Quick plot

x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.title("Test Plot")
plt.show()

# Cell 3: Test pandas

df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})
print(df)
```

If all cells run without errors, you're good to go!

---

## 8. API Keys Setup (For Later Sections)

You'll need these for Sections 8-14 (LLMs, RAG, Agents):

### OpenAI API Key

1. Visit https://platform.openai.com/
2. Sign up for an account
3. Go to API Keys section
4. Create new secret key
5. **Save it securely** - you can't view it again!

### Environment Variables

**Create `.env` file in project root**:
```bash

# In Agentic-AI directory

touch .env  # Creates .env file
```

**Add your API keys** (we'll do this in Section 8):
```
OPENAI_API_KEY=sk-your-key-here
```

**Important**: `.env` is in `.gitignore` - your keys won't be committed to Git.

---

## 9. Optional Tools

### Postman (API Testing)

**Download**: https://www.postman.com/downloads/

**Alternative**: Thunder Client (VS Code extension)

### Windows Terminal (Windows Only)

Much better than Command Prompt:
- Download from Microsoft Store
- Search "Windows Terminal"
- Set as default

### Oh My Zsh (macOS/Linux)

Better terminal experience:
```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

---

## 10. Verification Checklist

Run these commands to verify everything is set up:

```bash

# Check all versions

python --version          # 3.10+
pip --version            # 23.0+
git --version            # 2.x+
docker --version         # 20.x+

# Test Python environment

python -c "import numpy, pandas, sklearn, fastapi; print('✅ Python packages OK')"

# Test Docker

docker run hello-world   # Should see success message

# Test Jupyter

jupyter --version        # Should show version info

# Check if in virtual environment

python -c "import sys; print('✅ Virtual env' if 'venv' in sys.prefix else '❌ Not in venv')"
```

---

## Troubleshooting

### Python Command Not Found

**Windows**:
- Reinstall Python, check "Add to PATH"
- Or use `py` instead of `python`

**macOS/Linux**:
- Use `python3` instead of `python`
- Add alias: `alias python=python3`

### Pip Install Fails

```bash

# Upgrade pip first

python -m pip install --upgrade pip

# If still fails, try:

pip install --upgrade setuptools wheel

# Then retry installation

```

### Docker Won't Start

**Windows**:
- Enable virtualization in BIOS
- Ensure WSL 2 is installed
- Restart Docker Desktop

**macOS**:
- Check System Preferences → Security & Privacy
- Allow Docker

**Linux**:
- Check Docker service: `sudo systemctl status docker`
- Start if needed: `sudo systemctl start docker`

### Permission Errors (Linux)

```bash

# Add user to docker group

sudo usermod -aG docker $USER

# Log out and back in

```

### Virtual Environment Not Activating

**Windows PowerShell**:
```powershell

# May need to allow script execution

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**Then try activating again**.

---

## Getting Help

### If Something Doesn't Work:

1. **Check error message carefully** - often tells you what's wrong
2. **Google the error** - include the tool name
3. **Check tool's official documentation**
4. **Use GitHub Issues** on this repository
5. **Use GitHub Discussions** for questions

### Include in Your Question:

- Operating system and version
- Exact error message
- What you tried
- Screenshots if relevant

---

## What's Next?

You've got your environment set up! Now let's walk through the repository structure and how to use course resources.

**Next Lesson**: [Repository Walkthrough](./05-repository-walkthrough.md)

---

## Quick Reference

### Activate Virtual Environment

**Windows**: `venv\Scripts\activate`
**macOS/Linux**: `source venv/bin/activate`

### Deactivate Virtual Environment

```bash
deactivate
```

### Update Course Repository

```bash
git pull origin main
```

### Reinstall Dependencies

```bash
pip install -r requirements.txt --upgrade
```

---

**You're all set!** Let's explore the repository structure next.
