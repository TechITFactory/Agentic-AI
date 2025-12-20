# Data Leakage (The Silent Model Killer)

Leakage is the reason many “95% accurate” models become “60% accurate” the moment they see production data.

This chapter teaches you:

- what leakage is
- the common ways it happens
- how to prevent it using correct split and pipeline hygiene

---

## Outcomes

You will be able to:

- Spot leakage in columns and features
- Explain temporal leakage vs target leakage
- Avoid preprocessing leakage (fit on train only)
- Use scikit-learn pipelines correctly
- Apply a leakage prevention checklist in projects

**Estimated time**: 75–120 minutes

---

## 1) Definition

Leakage happens when your model uses information that would not be available at prediction time.

In other words:

- your training setup is “cheating”

---

## 2) Types of leakage

### A) Target leakage (post-event features)

Example: predicting churn but you include:

- `cancellation_date`
- `refund_amount`
- `account_closed_reason`

These may be recorded *after* churn happens.

### B) Temporal leakage

Example: you use a feature computed using data from the future.

- predicting churn at day 30
- but feature includes events at day 60

### C) Preprocessing / pipeline leakage

Common mistake:

- compute scaling/normalization using the entire dataset (train + test)

Even though the label isn’t used, you still leak information about the test distribution.

---

## 3) The pipeline rule (non-negotiable)

Any data transformation that learns parameters must be **fit on the training set only**.

Examples:

- StandardScaler (mean/std)
- OneHotEncoder category mapping
- imputation values
- PCA

---

## 4) How leakage shows up

You often see:

- suspiciously high test metrics
- model performance collapses in production
- “feature importance” dominated by one weird column

If your model performance is “too good to be true,” assume leakage until proven otherwise.

---

## Run the leakage demo

This repo includes a runnable script that demonstrates:

- a leaky feature that makes metrics look amazing
- the correct non-leaky setup
- how pipelines prevent preprocessing leakage

```bash
python sections/03-data-science-fundamentals/code/data_leakage_demo.py
```

---

## Leakage prevention checklist (save this)

Before training:

1) Define the prediction moment (“what do we know at inference time?”)
2) Remove obvious post-event columns
3) Use an appropriate split (time-based or grouped when needed)
4) Fit all preprocessing on training only (pipelines)
5) Sanity-check suspiciously high metrics

---

## Exercises

1) List three columns that would be leaky for churn prediction.
2) Why is scaling-on-full-data considered leakage?
3) If your dataset has one row per customer per month, what split avoids temporal leakage?

---

## Checkpoint

You’re done if you can explain (clearly):

- why a post-event column is leakage
- how pipelines prevent preprocessing leakage

---

## Next lesson

Continue to `05-classification-metrics.md`.
