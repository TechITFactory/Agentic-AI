# Mini Lab: First Baseline Model
# Mini Lab: First Baseline Model (Churn)

This lab is your first “real” ML workflow: you’ll build a baseline classifier, evaluate it correctly, and compare it to a naive baseline.

## Why this lab matters

Most ML projects fail because teams:

- Skip a naive baseline (“is this even better than guessing?”)
- Evaluate only on training data
- Leak information from test → train

By the end of this lab, you’ll have a baseline that another engineer can reproduce in one command.

## Outcomes

- ✅ Create a stratified train/test split
- ✅ Build a preprocessing + model `Pipeline` (prevents leakage)
- ✅ Compare a real baseline vs `DummyClassifier`
- ✅ Report metrics and propose your next 2 improvements

**Time**: ~60–90 minutes

## Where the lab lives

Go to:

- `sections/03-data-science-fundamentals/labs/baseline_model/`

You’ll find:

- `README.md` (lab instructions)
- `starter.py` (you complete this)
- `solution.py` (reference)
- `data/churn_synth.csv` (dataset)
- `data/generate_churn_synth.py` (optional dataset generator)

## Step-by-step

### 1) Run the naive baseline

From `sections/03-data-science-fundamentals/labs/baseline_model`:

```bash
python starter.py
```

What you should see:

- A confusion matrix
- Precision/recall/F1
- A reminder that your logistic regression baseline is still TODO

### 2) Implement the real baseline (no leakage)

Open `starter.py` and implement:

- `build_preprocessor()`
- `build_model()`

Requirements:

- Split should be **stratified** by `churn`
- Use a `ColumnTransformer` to handle:
	- categorical columns → `OneHotEncoder(handle_unknown='ignore')`
	- numeric columns → `StandardScaler()`
- Wrap everything in a single `Pipeline` so preprocessing is fit **only on training data**

Then uncomment the baseline model block in `main()`.

### 3) Compare against the naive baseline

Run again:

```bash
python starter.py
```

Compare:

- Does logistic regression beat the dummy baseline on F1?
- If accuracy looks similar, what happened to precision/recall?

### 4) Sanity checks (fast)

- If you re-run with the same seed, results should be identical.
- If you accidentally fit encoders/scalers on the full dataset, your test metrics may look suspiciously high.

## Deliverables

Write a short note (6–10 lines) answering:

1) Which metric would you optimize for churn and why?
2) What is misleading about accuracy here?
3) List 2 improvements you’d try next.

## Rubric (self-check)

- You report: confusion matrix + precision/recall/F1
- You compare against `DummyClassifier`
- Your model uses a `Pipeline` / `ColumnTransformer`
- Your code runs end-to-end from a clean environment

## Next

Take the ideas from this lab forward:

- In Section 4 you’ll start training “real” models
- In later sections you’ll productionize: validation, drift, monitoring, and CI/CD
