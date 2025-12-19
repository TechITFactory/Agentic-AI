# Section 2: Python for AI (Only What You Need)

## Overview

This section covers Python fundamentals specifically for AI/ML work. We focus on what you'll actually use, not a comprehensive Python course.

## What You'll Learn

1. **Python Essentials**: Functions, files, modules (crash course)
2. **Virtual Environments**: venv/conda + requirements.txt
3. **NumPy**: Arrays and operations for numerical computing
4. **Pandas**: Data manipulation (read, filter, join, groupby)
5. **JSON/CSV**: Working with data formats like real systems
6. **Mini Lab**: Clean a user-activity dataset

## Why Only What You Need?

We assume you have basic programming knowledge (any language). This section teaches:
- ✅ Python syntax you'll use in ML
- ✅ Libraries essential for data work
- ✅ Practical patterns for AI projects

We skip:
- ❌ Deep Python internals
- ❌ Advanced OOP patterns
- ❌ Web frameworks (except FastAPI later)
- ❌ Everything else you can learn as needed

## Prerequisites

- Basic programming in any language (variables, loops, functions)
- Python installed (from Section 1)
- Virtual environment set up

## Lessons

1. [Python Crash Course for AI](./01-python-crash-course.md)
2. [Virtual Environments Guide](./02-virtual-environments.md)
3. [NumPy Basics](./03-numpy-basics.md)
4. [Pandas Essentials](./04-pandas-essentials.md)
5. [Working with JSON and CSV](./05-json-csv-data.md)
6. [Mini Lab: User Activity Data Cleaning](./06-mini-lab-data-cleaning.md)

## Duration

**Estimated Time**: 6-8 hours
- If you know Python: 3-4 hours (focus on NumPy/Pandas)
- If new to Python: 8-10 hours

## Section Structure

```
sections/02-python-for-ai/
├── README.md                    # This file
├── 01-python-crash-course.md    # Python basics
├── 02-virtual-environments.md   # Environment management
├── 03-numpy-basics.md           # NumPy tutorial
├── 04-pandas-essentials.md      # Pandas tutorial
├── 05-json-csv-data.md          # Data formats
├── 06-mini-lab-data-cleaning.md # Lab instructions
├── code/                        # Runnable examples
│   ├── numpy_examples.py
│   ├── pandas_examples.py
│   └── data_loading.py
└── labs/
    └── lab_data_cleaning/       # Mini lab
        ├── README.md
        ├── data/
        │   └── user_activity.csv
        ├── starter.py
        └── solution.py
```

## Learning Objectives

By the end of this section, you will be able to:
- ✅ Write clean Python code for ML projects
- ✅ Manage virtual environments and dependencies
- ✅ Manipulate data with NumPy arrays
- ✅ Process datasets with Pandas
- ✅ Load and save data in JSON/CSV formats
- ✅ Clean real-world messy data

## What's Next?

After this section, you'll move to [Section 3: Data Science Fundamentals](../03-data-science-fundamentals/README.md) where you'll learn ML concepts like train/test splits and evaluation metrics.

## Quick Start

```bash
# Navigate to this section
cd sections/02-python-for-ai

# Install section-specific dependencies (if any)
pip install numpy pandas jupyter

# Run examples
python code/numpy_examples.py
python code/pandas_examples.py

# Launch notebook for interactive learning
jupyter notebook
```

## Tips for This Section

1. **Code Along**: Type examples yourself
2. **Experiment**: Change values, break code, fix it
3. **Complete the Lab**: Data cleaning is essential for ML
4. **Keep It Practical**: Don't try to memorize everything
5. **Use Docs**: Get comfortable with NumPy/Pandas documentation

---

Ready to start? Begin with [Python Crash Course for AI](./01-python-crash-course.md)!
