# Python Crash Course for AI Engineering

This chapter is a fast but **complete** Python refresher focused on the skills you’ll use throughout the course: clean functions, data structures, file I/O, modules, basic typing, and “script that runs every time” habits.

If you already know Python, skim the explanations and run the mini-project at the end.

---

## Why this lesson

Most AI/ML tutorials teach Python like a notebook toy. Production work is different:

- You read/write files.
- You build small modules.
- You handle errors.
- You make code runnable from the command line.

This lesson gets you there without turning into a full CS class.

---

## Outcomes

By the end you can:

- Write readable Python with functions, loops, comprehensions, and exceptions
- Use the core data structures (list/dict/set/tuple) correctly
- Read JSON and write CSV with the standard library
- Structure small projects using modules and imports
- Build a tiny CLI script with logging

**Estimated time**: 90–120 minutes (including the mini-project)

**Prerequisites**: Basic programming in any language

---

## How you should run code in this course

Two reliable ways:

1) **Run a script**

```bash
python path/to/script.py
```

2) **Run a module** (when you have a small package)

```bash
python -m package.module
```

### Common gotcha (Windows)

If `python` prints “Python was not found…”, install Python from python.org and disable the Microsoft Store alias (`python.exe`) in App execution aliases (see Section 01 tooling guide).

---

## Part 1 — Core syntax you actually need

### Variables and basic types

Python is dynamically typed, but production Python is written *as if* it is typed (because tools like linters and type checkers can help you).

```python
name = "Asha"
age = 27
is_student = False
score = 0.91

print(type(name), type(age), type(is_student), type(score))
```

Key built-in types you’ll use constantly:

- `str`: text
- `int`, `float`: numbers
- `bool`: truth values
- `None`: “no value”

### Truthiness (important for clean conditions)

In Python, empty containers are “falsey”:

```python
items = []
if not items:
	print("No items")

user = None
if user is None:
	print("No user")
```

Use `is None` / `is not None` for `None` checks.

---

## Part 2 — Data structures (the AI engineer essentials)

You’ll manipulate data constantly (datasets, API payloads, retrieved documents, model outputs). These 4 structures cover 95%.

### List — ordered collection

Use a list when you have an ordered sequence.

```python
numbers = [1, 2, 3]
numbers.append(4)
print(numbers[0])  # 1
```

### Tuple — fixed, ordered collection

Use tuples for “small fixed records” or keys.

```python
point = (10, 20)
x, y = point
```

### Dict — key/value mapping

Use dictionaries for structured records (like JSON objects).

```python
user = {"id": "u_123", "country": "US", "score": 0.87}
print(user["score"])

# Prefer .get when keys may be missing
print(user.get("email"))  # None
```

### Set — unique collection

Use sets for membership checks and uniqueness.

```python
seen_ids = {"u_1", "u_2"}
print("u_2" in seen_ids)  # True
```

---

## Part 3 — Control flow (conditions + loops)

### `if / elif / else`

```python
score = 0.76
if score >= 0.9:
	label = "high"
elif score >= 0.7:
	label = "medium"
else:
	label = "low"
```

### `for` loops

```python
items = ["a", "b", "c"]

for item in items:
	print(item)

for idx, item in enumerate(items):
	print(idx, item)
```

### Loop helpers you’ll use a lot

`range(n)`, `zip(a, b)`, `sorted(iterable)`.

```python
for i in range(3):
	print(i)

countries = ["US", "CA"]
scores = [0.9, 0.8]
for c, s in zip(countries, scores):
	print(c, s)
```

---

## Part 4 — Functions (the unit of production code)

### Define functions that do one thing

```python
def clamp(value: float, min_value: float, max_value: float) -> float:
	if value < min_value:
		return min_value
	if value > max_value:
		return max_value
	return value
```

### Default values

```python
def greet(name: str, greeting: str = "Hello") -> str:
	return f"{greeting}, {name}!"
```

### `*args` and `**kwargs` (know them; don’t overuse them)

- `*args` collects positional arguments
- `**kwargs` collects keyword arguments

```python
def mean(*values: float) -> float:
	return sum(values) / len(values)

def build_user(**fields: object) -> dict[str, object]:
	return dict(fields)
```

In production code, prefer explicit parameters unless you truly need flexible signatures.

### Docstrings (short and useful)

```python
def normalize_country(country: str) -> str:
	"""Normalize a country code to uppercase.

	Raises:
		ValueError: if the input is empty.
	"""
	country = country.strip()
	if not country:
		raise ValueError("country is empty")
	return country.upper()
```

---

## Part 5 — Comprehensions (fast, readable data transforms)

### List comprehension

```python
scores = [0.95, 0.7, 0.4]
high = [s for s in scores if s >= 0.8]
```

### Dict comprehension

```python
users = [
	{"id": "u1", "score": 0.9},
	{"id": "u2", "score": 0.6},
]
score_by_id = {u["id"]: u["score"] for u in users}
```

### Set comprehension

```python
countries = ["US", "us", "CA"]
unique = {c.upper() for c in countries}
```

Rule of thumb: if a comprehension becomes hard to read, use a loop.

---

## Part 6 — Exceptions (how production code behaves)

You want failures to be:

- clear
- actionable
- not silently ignored

### Basic try/except

```python
try:
	value = int("not-a-number")
except ValueError as e:
	print(f"Bad integer: {e}")
```

### Raising your own errors

```python
def require_positive(x: float) -> float:
	if x <= 0:
		raise ValueError("x must be positive")
	return x
```

Avoid bare `except:` in real code. Catch the specific exception you expect.

---

## Part 7 — Files and `pathlib` (no fragile string paths)

In this course you will read datasets, configs, artifacts, and docs. Use `pathlib.Path`.

```python
from pathlib import Path

root = Path(".")
data_dir = root / "datasets"
print(data_dir.exists())
```

### Read/write text safely

```python
from pathlib import Path

path = Path("example.txt")
path.write_text("hello\n", encoding="utf-8")
text = path.read_text(encoding="utf-8")
```

---

## Part 8 — JSON and CSV (standard library, production-friendly)

### Reading JSON

```python
import json
from pathlib import Path

records = json.loads(Path("input.json").read_text(encoding="utf-8"))
assert isinstance(records, list)
```

### Writing CSV

```python
import csv
from pathlib import Path

rows = [
	{"id": "u1", "score": 0.9},
	{"id": "u2", "score": 0.6},
]

out_path = Path("output.csv")
with out_path.open("w", newline="", encoding="utf-8") as f:
	writer = csv.DictWriter(f, fieldnames=["id", "score"])
	writer.writeheader()
	writer.writerows(rows)
```

---

## Part 9 — Modules, imports, and the `__main__` pattern

As soon as code grows past one file, you want modules.

### A simple layout

```text
sections/02-python-for-ai/code/
  json_to_csv.py
  python_crash_course/
	__init__.py
	io_utils.py
	filtering.py
```

### Importing your own code

If you run from the `code/` directory, you can import the package folder:

```python
from python_crash_course.io_utils import read_json_records
```

### The main guard

```python
def main() -> int:
	print("Hello")
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
```

This makes your file work both as an importable module and as a script.

---

## Part 10 — Logging (instead of print debugging)

In production services (FastAPI, pipelines), you’ll rely on logs.

```python
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

logger.info("Starting job")
```

---

## Mini-project (Production-style): JSON → filter → CSV

You will build a small CLI utility that:

1) reads a JSON file containing user records
2) filters by minimum score and optional country
3) writes results to CSV

### Where the runnable code is

This repo includes a production-grade reference implementation here:

- `sections/02-python-for-ai/code/json_to_csv.py`
- `sections/02-python-for-ai/code/python_crash_course/io_utils.py`
- `sections/02-python-for-ai/code/python_crash_course/filtering.py`

### Data format

`input.json` is a list of objects like:

```json
[
  {"id": "u_001", "country": "US", "score": 0.91},
  {"id": "u_002", "country": "CA", "score": 0.62}
]
```

### Run it

From repo root:

```bash
python sections/02-python-for-ai/code/json_to_csv.py \
  --in sections/02-python-for-ai/code/sample_input.json \
  --out /tmp/output.csv \
  --min-score 0.7
```

On Windows, choose an output path like:

```powershell
python .\sections\02-python-for-ai\code\json_to_csv.py `
  --in .\sections\02-python-for-ai\code\sample_input.json `
  --out .\sections\02-python-for-ai\code\output.csv `
  --min-score 0.7
```

Try filtering by country:

```bash
python sections/02-python-for-ai/code/json_to_csv.py \
  --in sections/02-python-for-ai/code/sample_input.json \
  --out /tmp/output_us.csv \
  --min-score 0.7 \
  --country US
```

### What “production-grade” means here

- uses `argparse` for a real CLI
- uses `pathlib` for paths
- validates inputs with clear error messages
- uses logging (so you can reuse patterns in pipelines/APIs)
- keeps logic split into modules (so it stays maintainable)

---

## Checkpoint

You should be able to answer these without guessing:

1) When do you use a `dict` vs a `list`?
2) What is the difference between `Path.read_text()` and opening a file?
3) Why is `if __name__ == "__main__":` useful?
4) Why do we prefer logging over `print` in production code?
5) What’s the difference between raising an exception and returning `None`?

---

## Next lesson

Continue to `02-virtual-environments.md` to make sure your Python environment is reproducible and isolated.
