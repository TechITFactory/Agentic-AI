# Repository Walkthrough

## Why this lesson

Learn how the repo is organized so you can find lessons, code, and labs quickly and avoid getting lost.

## Outcomes

-  Know the folder layout and how sections are structured
-  Can run examples, labs, and notebooks from the right paths
-  Have a personal plan to track progress (branching or checklist)

**Time**: ~10 minutes

**Prerequisites**: Tools installed and repo cloned

---

##  Your Textbook and Lab Bench

This repository is not just a collection of files. It is your **interactive textbook** and your **laboratory bench**.

We have designed the structure to be intuitive, but it helps to know where things are so you don't get lost.

---

##  The High-Level Structure

When you open the `Agentic-AI` folder, you will see:

```text
Agentic-AI/
 sections/              #  The Core Content
    01-welcome-setup/
    02-python-for-ai/
    ...
    16-bonus-advanced/
 datasets/              #  Data for Labs
    customer_churn.csv
    ...
 shared/                #  Helper Code
    utils.py
 requirements.txt       #  Dependencies
 README.md              #  Home
```

### `sections/`
This is where you will spend 95% of your time. Each folder corresponds to a module in the course. They are numbered `01` to `16` so you can follow them in order.

### `datasets/`
We provide real-world datasets for the projects. You won't need to scrape data yourself unless you want to.

### `shared/`
Contains utility functions (like logger setups or common plotting functions) that we reuse across multiple lessons.

---

##  Anatomy of a Section

Let's look inside a typical section, like `04-machine-learning-basics`:

```text
sections/04-machine-learning-basics/
 README.md              #  Start Here!
 01-linear-regression.md #  Lesson Transcript
 02-decision-trees.md
 code/                  #  Runnable Examples
    train_model.py
 labs/                  #  Hands-on Exercises
     lab_churn_prediction/
         README.md      # Lab Instructions
         starter.py     # Broken/Empty code for you to fix
         solution.py    # The answer key
```

### How to use a Section:
1.  **Read the README**: It tells you what you will learn and the estimated time.
2.  **Read the Lesson**: Open `01-topic.md`. Read the concept and the code snippets.
3.  **Run the Code**: Go to the `code/` folder and run the examples. Don't just read them!
    ```bash
    cd sections/04-machine-learning-basics/code
    python train_model.py
    ```
4.  **Do the Lab**: Go to `labs/`. Read the instructions. Try to solve it in `starter.py`. If you get stuck, peek at `solution.py`.

---

##  Pro Tips for Success

### 1. Code Along
When you see a code block in a lesson, **type it out**. Do not copy-paste. Typing builds muscle memory.

### 2. Use Branches
Treat this course like a real software project. Create a git branch for your work:
```bash
git checkout -b my-learning-journey
```
This way, you can mess up the code, delete things, and experiment without breaking the original files.

### 3. The "Solution" Temptation
It is very tempting to just look at `solution.py`. **Don't do it.**
Struggling with the code is where the learning happens. Only look at the solution after you have tried for at least 15 minutes.

---

##  Ready to Launch?

You have the roadmap. You have the tools. You know the terrain.

It's time to write some code.

**Next Section**: [Section 2: Python for AI](../02-python-for-ai/README.md)