# Mini Lab: User Activity Data Cleaning (Model-Ready Table)

In real ML work, data cleaning is not “nice to have.” It’s most of the job.

This lab simulates a common scenario:

- raw user activity dump
- missing values
- inconsistent categories
- outliers
- bad rows (negative revenue)

Your goal is to produce a clean CSV that downstream model training can trust.

---

## Outcomes

By the end you will:

- Load raw data and inspect shape/dtypes/missingness
- Apply a reproducible cleaning pipeline
- Create a short “cleaning report” (what you changed and why)
- Write out `user_activity_cleaned.csv` for later sections

**Estimated time**: 60–120 minutes

---

## Where the lab lives

All lab files are here:

```text
sections/02-python-for-ai/labs/lab_data_cleaning/
```

Key files:

- `README.md` (full lab instructions)
- `starter.py` (your starting point)
- `solution.py` (reference solution)
- `data/user_activity.csv` (messy dataset)
- `data/generate_data.py` (optional generator)

---

## Run the starter

From the lab folder:

```bash
cd sections/02-python-for-ai/labs/lab_data_cleaning
python starter.py
```

If you want to regenerate the dataset:

```bash
python data/generate_data.py
```

---

## What you must implement

Your `starter.py` pipeline should do these steps (in this order):

1) **Load and inspect**
	- print shape, head, dtypes, missing counts
2) **Handle missing values**
	- sessions → fill with 0
	- support_tickets → fill with 0
	- revenue → fill with median
3) **Fix data quality**
	- remove negative revenue rows
	- normalize `subscription_type` (strip + lower)
	- parse dates (`signup_date`, `last_login`)
4) **Handle outliers**
	- remove rows where `features_used` is above the 95th percentile
5) **Feature engineering (bonus but recommended)**
	- days_since_signup
	- days_since_last_login
	- active_recently (last login within 30 days)
6) **Save cleaned data**
	- write `data/user_activity_cleaned.csv`
7) **Print a cleaning report**
	- rows removed, why
	- columns added
	- confirm no missing values remain

---

## Deliverables

Minimum:

- `data/user_activity_cleaned.csv`
- a printed “Data Cleaning Report” in the console

Recommended:

- a short note in your own words: what assumptions you made and why

---

## Evaluation checklist

Your solution is correct if:

- output CSV loads with `pd.read_csv(...)` without errors
- no negative revenue rows remain
- category normalization produced clean `subscription_type` values
- dates are real datetimes (not strings)
- outliers were removed using a percentile-based threshold

---

## Checkpoint

If you hand your cleaned CSV to a teammate, can they train a simple model *without asking you what the columns mean*?

---

## Next section

After this lab, you’re ready for [Section 3: Data Science Fundamentals](../03-data-science-fundamentals/README.md).
