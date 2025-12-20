# Working with JSON / CSV / JSONL (Log-Like Data)

Most production systems emit “log-like” data:

- CSV exports from analytics pipelines
- JSON responses from APIs
- JSONL logs (one JSON object per line)

Your job as an AI engineer is to ingest these reliably and turn them into tables or features.

---

## Outcomes

You will be able to:

- Read/write JSON and CSV safely (stdlib + Pandas)
- Understand JSON vs JSONL and when each is used
- Flatten nested JSON into columns
- Handle light schema drift (missing/extra fields) without crashing

**Estimated time**: 60–90 minutes

---

## JSON vs JSONL vs CSV

### JSON

Typically a single document:

- list of records: `[{...}, {...}]`
- or a single object: `{...}`

Good for API payloads and config.

### JSONL (JSON Lines)

One JSON object per line:

```text
{"ts": "...", "event": "..."}
{"ts": "...", "event": "..."}
```

Good for streaming logs and large files.

### CSV

Tabular format; good for analytics + model training.

---

## Reading JSON safely (stdlib)

```python
import json
from pathlib import Path

data = json.loads(Path("input.json").read_text(encoding="utf-8"))
```

Validate assumptions:

- Is it a list?
- Are items dicts?
- Are required keys present?

---

## Writing CSV safely (stdlib)

```python
import csv
from pathlib import Path

rows = [{"id": "u1", "score": 0.9}]
with Path("out.csv").open("w", newline="", encoding="utf-8") as f:
		w = csv.DictWriter(f, fieldnames=["id", "score"])
		w.writeheader()
		w.writerows(rows)
```

---

## Flattening nested JSON

In logs, you often see nested `meta` objects.

Two approaches:

1) Use a custom flattener (more control)
2) Use Pandas `json_normalize` (fast, convenient)

Example:

```python
import pandas as pd

df = pd.json_normalize(records)
```

---

## Schema drift (a fact of life)

Schema drift means:

- a new optional field appears
- a nested key appears for some events
- a field sometimes has the wrong type

Production-friendly strategies:

- treat unknown fields as optional
- union columns across rows (expand columns)
- store “weird” structures as JSON strings
- validate required keys and fail fast on missing critical fields

---

## Run the worked scripts

### 1) JSON list → filter → CSV

```bash
python sections/02-python-for-ai/code/json_to_csv.py \
	--in sections/02-python-for-ai/code/sample_input.json \
	--out /tmp/output.csv \
	--min-score 0.7
```

### 2) JSONL logs → flattened CSV

```bash
python sections/02-python-for-ai/code/jsonl_to_csv.py \
	--in sections/02-python-for-ai/code/sample_logs.jsonl \
	--out /tmp/logs.csv
```

---

## Checkpoint

You’re done if you can explain:

1) why JSONL is useful for streaming
2) how you would handle a new optional field appearing mid-file
3) how you would validate “required” fields without breaking on “optional” ones

---

## Next lesson

Continue to `06-mini-lab-data-cleaning.md`.
