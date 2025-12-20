# Classification Metrics (Precision, Recall, F1, ROC-AUC, PR-AUC)

Classification is not “get the highest accuracy.”

In real systems (fraud, churn, incident detection), the positive class is often rare and the costs of mistakes are asymmetric.

This chapter teaches you how to pick and interpret metrics that map to reality.

---

## Outcomes

You will be able to:

- Read a confusion matrix
- Compute accuracy, precision, recall, F1
- Explain thresholds and why metrics change with thresholds
- Understand ROC-AUC vs PR-AUC and when each matters
- Pick a primary metric based on business cost

**Estimated time**: 90–120 minutes

---

## 1) Confusion matrix (the base of everything)

For binary classification:

- True Positive (TP)
- False Positive (FP)
- True Negative (TN)
- False Negative (FN)

In churn prediction, the “positive” class might be `churned=1`.

---

## 2) Accuracy (why it’s dangerous)

Accuracy = correct predictions / all predictions.

If churn rate is 5%, a model that predicts “no churn” always has 95% accuracy.

That model is useless.

---

## 3) Precision and recall

Precision answers:

> When we predict positive, how often are we right?

Recall answers:

> Of all true positives, how many did we catch?

There is usually a tradeoff.

---

## 4) F1 score

F1 is the harmonic mean of precision and recall.

Use F1 when:

- you need a single metric
- you care about both precision and recall

---

## 5) Thresholds (why metrics are not fixed)

Many models output a probability.

Choosing a threshold (0.5 by default) changes TP/FP/FN/TN.

In production, you often tune thresholds to meet business constraints.

---

## 6) ROC-AUC vs PR-AUC

### ROC-AUC

Measures ranking quality across all thresholds.

ROC can look good even when positives are rare.

### PR-AUC

Focuses on performance on the positive class.

PR-AUC is often more informative for imbalanced problems.

Rule of thumb:

- rare positives → pay attention to PR-AUC

---

## Run the metrics demo

This repo includes a runnable metrics script:

```bash
python sections/03-data-science-fundamentals/code/metrics_examples.py
```

It prints:

- confusion matrix
- accuracy, precision, recall, F1
- ROC-AUC and Average Precision (PR-AUC)

---

## Mini-scenarios (pick a metric)

1) Fraud detection: false negatives are very costly
	- prioritize: high recall (and acceptable precision)

2) Marketing churn intervention: outreach costs money
	- prioritize: precision (avoid wasting campaigns)

3) Incident detection: missing incidents is dangerous
	- prioritize: recall, and tune threshold to manage pager noise

---

## Exercises

1) If the business says “we can only contact 5% of customers,” is accuracy a good metric?
2) Why might you choose PR-AUC over ROC-AUC for churn?
3) If your recall is 0.95 but precision is 0.05, what does that mean operationally?

---

## Checkpoint

You’re done if you can explain:

- why accuracy is misleading for imbalanced data
- how thresholds change precision/recall
- when PR-AUC is the right focus

---

## Next lesson

Continue to `06-regression-metrics.md`.
