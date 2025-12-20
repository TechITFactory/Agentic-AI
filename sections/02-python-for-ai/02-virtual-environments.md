# Virtual Environments + `requirements.txt` (Reproducibility 101)

Production AI engineering is less about “can I import numpy today” and more about:

- can I reproduce this environment next week?
- can a teammate reproduce it?
- can CI reproduce it?

This chapter teaches the minimal, professional workflow to keep dependencies isolated and repeatable.

---

## Outcomes

You will be able to:

- Create and activate a virtual environment (`venv`)
- Install dependencies from a curated `requirements.txt`
- Diagnose the most common environment problems on Windows/macOS/Linux
- Produce a tiny “environment report” to debug issues quickly

**Estimated time**: 45–60 minutes

---

## Key idea: your system Python should stay clean

Never install packages globally for a course/project.

Why?

- You’ll eventually break something (version conflicts are guaranteed).
- Two projects will need different dependency versions.
- CI needs a clean environment every run.

Instead:

- Use one venv per repo (or per project).
- Pin dependencies in `requirements.txt`.

---

## Option A (recommended for this repo): `venv`

### Create a venv

From the repo root (`Agentic-AI/`):

```bash
python -m venv venv
```

### Activate it

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
source venv/bin/activate
```

You should now see `(venv)` in your terminal prompt.

---

## Install dependencies from `requirements.txt`

This repo ships a curated, pinned dependency set at the repo root.

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Verify quickly

Use the course-wide verification script:

```bash
python ./scripts/verify_env.py
```

If you want more details:

```bash
python sections/02-python-for-ai/code/env_report.py
```

---

## `requirements.txt`: curated vs `pip freeze`

Two concepts:

### 1) Curated requirements (what this repo uses)

- Humans write it.
- Versions are pinned intentionally.
- It’s stable for students.

### 2) `pip freeze` output

- Generated from your current environment.
- Captures *everything* installed (including transitive dependencies).
- Useful for debugging or “snapshotting” a working machine.

For course repos, prefer curated/pinned requirements.

If you want to snapshot your local environment without editing the course file, do:

```bash
pip freeze > requirements.local.txt
```

---

## Common problems and fixes (real-world)

### Problem: `python` launches Microsoft Store (Windows)

Symptoms:

- `python` prints “Python was not found; run without arguments to install from the Microsoft Store…”

Fix:

- Install Python from python.org
- Disable **Settings → Apps → Advanced app settings → App execution aliases → python.exe**

### Problem: You installed packages, but VS Code can’t import them

Cause: VS Code is using a different interpreter.

Fix:

- In VS Code: “Python: Select Interpreter” → choose the `venv` interpreter.

### Problem: `pip` installs but imports fail

Cause: you may be using a different python/pip pair.

Fix:

```bash
python -m pip install -r requirements.txt
python -c "import numpy, pandas; print('ok')"
```

This forces pip to target the same interpreter.

---

## Hands-on exercise (10–15 minutes)

1) Create and activate `venv`
2) Install repo requirements
3) Run:

```bash
python ./scripts/verify_env.py
python sections/02-python-for-ai/code/env_report.py
```

Deliverable:

- A screenshot or short note that includes:
	- `sys.executable`
	- Python version
	- confirmation that `verify_env.py` passes

---

## Checkpoint

You’re good if you can answer:

1) Why do we avoid installing packages globally?
2) What’s the difference between curated requirements and `pip freeze`?
3) How do you guarantee `pip` targets the right interpreter?

---

## Next lesson

Continue to `03-numpy-basics.md`.
