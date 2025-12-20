# Section 2: Python for AI Engineering (Production-First)

This section teaches Python the way you’ll actually use it as an AI/ML engineer: scripts, modules, data files, reproducibility, and the core data stack (NumPy + Pandas).

You will also complete a mini-lab that mimics real work: cleaning messy activity logs into a model-ready table.

---

## Outcomes

By the end of this section, you can:

- Write clean Python scripts with functions, modules, and robust file I/O
- Create reproducible environments (`venv`, `requirements.txt`) and avoid dependency chaos
- Use NumPy for vectorized numeric operations (no Python loops for math)
- Use Pandas for real dataset prep (filter, join/merge, groupby, missing values)
- Parse JSON/JSONL/CSV data safely and handle light schema drift
- Produce a cleaned dataset with documented assumptions

---

## Lessons

1. [Python Crash Course for AI Engineering](./01-python-crash-course.md)
2. [Virtual Environments + requirements.txt](./02-virtual-environments.md)
3. [NumPy Basics (Arrays, Masking, Broadcasting)](./03-numpy-basics.md)
4. [Pandas Essentials (Read, Filter, Join, Groupby)](./04-pandas-essentials.md)
5. [Working with JSON/CSV/JSONL (Log-Like Data)](./05-json-csv-data.md)
6. [Mini Lab: User Activity Data Cleaning](./06-mini-lab-data-cleaning.md)

---

## Prerequisites

- Basic programming in any language
- Python 3.10+
- A working virtual environment (Section 01)

---

## Section layout

```text
sections/02-python-for-ai/
    README.md
    01-python-crash-course.md
    02-virtual-environments.md
    03-numpy-basics.md
    04-pandas-essentials.md
    05-json-csv-data.md
    06-mini-lab-data-cleaning.md
    code/
        json_to_csv.py
        jsonl_to_csv.py
        numpy_basics.py
        pandas_examples.py
        pandas_essentials.py
        sample_input.json
        sample_logs.jsonl
        python_crash_course/
            __init__.py
            filtering.py
            io_utils.py
    labs/
        lab_data_cleaning/
            README.md
            starter.py
            solution.py
            data/
                generate_data.py
                user_activity.csv
```

---

## Quick start (run real code)

From the repo root:

```bash
python sections/02-python-for-ai/code/numpy_basics.py
python sections/02-python-for-ai/code/pandas_essentials.py
python sections/02-python-for-ai/code/json_to_csv.py --in sections/02-python-for-ai/code/sample_input.json --out /tmp/output.csv --min-score 0.7
python sections/02-python-for-ai/code/jsonl_to_csv.py --in sections/02-python-for-ai/code/sample_logs.jsonl --out /tmp/logs.csv
```

On Windows PowerShell, use paths like:

```powershell
python .\sections\02-python-for-ai\code\numpy_basics.py
python .\sections\02-python-for-ai\code\pandas_essentials.py
```

---

## How to know you’re done

You’re ready to move on when you can:

- run the scripts without editing paths
- explain list vs dict vs set vs tuple
- explain what broadcasting is
- join two DataFrames and compute grouped metrics without loops
- complete the lab and produce `user_activity_cleaned.csv`

Next section: [Section 3: Data Science Fundamentals](../03-data-science-fundamentals/README.md)
