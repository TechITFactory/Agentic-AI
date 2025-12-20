# Lab: Build Your First Baseline Model (Churn)

## Goal

Train a **reproducible baseline** churn classifier and evaluate it correctly.

You will:

- Load a tabular dataset
- Create a proper train/test split (stratified)
- Build a preprocessing + model `Pipeline` (no leakage)
- Compare against a naive baseline (`DummyClassifier`)
- Report metrics and propose next improvements

## What you'll build

A small CLI script that trains and evaluates:

- **Naive baseline**: “always predict the most frequent class”
- **Baseline model**: Logistic Regression + preprocessing

## Dataset

File: `data/churn_synth.csv`

- Target label: `churn` (0/1)
- Mix of numeric + categorical features

If you want to regenerate it:

```bash
python data/generate_churn_synth.py --out data/churn_synth.csv --rows 500 --seed 42
```

## Tasks

1) Run the starter (it should fail/print TODO guidance)
2) Implement the missing pieces in `starter.py`
3) Run again and confirm you get:
   - Metrics for the naive baseline
   - Metrics for the logistic regression pipeline
4) Answer the reflection questions

## Run

From `sections/03-data-science-fundamentals/labs/baseline_model`:

```bash
python starter.py
```

To compare with the reference solution:

```bash
python solution.py
```

Optional: point to a different dataset path

```bash
python starter.py --data data/churn_synth.csv
```

## Reflection questions

Write 6–10 lines in a short note (a local text file is fine):

- Which metric mattered most here and why? (accuracy vs precision/recall vs F1)
- Did the naive baseline look “good” on any metric? Why can that be misleading?
- What are 2 improvements you’d try next?
  - Examples: better features, class weights, calibration, threshold tuning, different model

## Success criteria

- Your run is deterministic with the same seed.
- You use a `Pipeline` / `ColumnTransformer` (no leakage).
- You report at least: accuracy, precision, recall, F1 and a confusion matrix.
- Your logistic regression baseline beats the naive baseline on at least one meaningful metric.
