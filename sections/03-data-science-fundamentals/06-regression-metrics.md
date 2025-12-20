# Regression Metrics (MAE, MSE, RMSE, R²)

Regression is about predicting a number:

- time-to-resolution
- revenue
- demand
- delivery duration

Metrics should match the business cost of errors.

---

## Outcomes

You will be able to:

- Compute MAE, MSE, RMSE, and R²
- Explain MAE vs RMSE and outlier sensitivity
- Compare a model against simple baselines (mean/median)
- Communicate error in real units (“off by $X on average”)

**Estimated time**: 60–90 minutes

---

## 1) MAE (Mean Absolute Error)

MAE is the average absolute difference between prediction and true value.

Why it’s popular:

- easy to interpret in business units
- less sensitive to outliers than RMSE

---

## 2) MSE and RMSE

MSE squares errors, which penalizes large errors more.

RMSE is the square root of MSE.

Why RMSE is used:

- strongly penalizes large errors
- sometimes aligns with business risk (big misses hurt more)

---

## 3) R² (coefficient of determination)

R² measures how much variance your model explains relative to a baseline.

Caveat:

- R² can be misleading across datasets with different variance
- always pair it with MAE/RMSE

---

## 4) Baselines (mandatory)

Before building anything fancy, compare to:

- mean predictor
- median predictor

If your model can’t beat a baseline reliably, you don’t have a modeling problem—you have a data/problem-definition problem.

---

## Run the regression metrics demo

The metrics script includes a regression section:

```bash
python sections/03-data-science-fundamentals/code/metrics_examples.py
```

It prints regression metrics for:

- a simple model
- mean/median baselines

---

## Exercises

1) If outliers are rare but very costly, which metric do you prefer: MAE or RMSE? Why?
2) If RMSE=$50, how do you explain that to a PM?
3) Why is “R²=0.9” not enough to declare success?

---

## Checkpoint

You’re done if you can explain:

- why MAE and RMSE behave differently
- why baselines are mandatory

---

## Next lesson

Continue to `07-mini-lab-baseline-model.md`.
