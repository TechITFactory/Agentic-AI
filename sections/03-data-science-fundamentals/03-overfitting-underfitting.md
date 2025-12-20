# Overfitting and Underfitting (Generalization vs Memorization)

Overfitting is the most common reason an ML model looks good during development and fails in production.

This chapter makes overfitting concrete and gives you a checklist to detect and fix it.

---

## Outcomes

You will be able to:

- Detect underfitting vs overfitting using train/validation metrics
- Explain the bias/variance intuition without math proofs
- List practical fixes: simplify, regularize, more data, better splits
- Understand why leakage can *look like* great generalization

**Estimated time**: 60–90 minutes

---

## 1) The three states of model fit

### Underfitting (too simple)

- training performance: poor
- validation/test performance: poor

Model didn’t learn useful patterns.

### Good fit

- training performance: good
- validation/test performance: similar and good

Model learned true patterns.

### Overfitting (too complex)

- training performance: excellent
- validation/test performance: much worse

Model memorized noise or training-specific quirks.

---

## 2) What causes overfitting (in real projects)

- too much model capacity relative to data
- too many features (especially leaky ones)
- leakage in preprocessing (fit on full dataset)
- tuning too aggressively on validation/test

---

## 3) How to detect it

The simplest signal:

- train score high, test score low

Examples:

- Train accuracy 0.99, Test accuracy 0.72 → likely overfitting
- Train RMSE 10, Test RMSE 60 → likely overfitting

Also watch learning curves:

- training loss decreases
- validation loss bottoms out then increases

---

## 4) How to fix it (most effective first)

1) **Get more data**
2) **Reduce model complexity**
3) **Add regularization**
4) **Use cross-validation** for more stable estimates
5) **Improve features** (better signal, less noise)

---

## Run the overfitting demo

This section includes a runnable script:

```bash
python sections/03-data-science-fundamentals/code/overfitting_demo.py
```

It demonstrates:

- underfit: constant predictor
- good fit: polynomial degree 2
- overfit: polynomial degree 15

---

## Exercises

1) In the demo output, which model has the largest train–test gap?
2) List two ways to reduce overfitting without changing the model type.
3) How can leakage create a model that appears to generalize?

---

## Checkpoint

You’re done if you can propose one fix given:

- training metric is great
- validation metric is bad

---

## Next lesson

Continue to `04-data-leakage.md`.
