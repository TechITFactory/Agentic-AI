# XGBoost Introduction

## Why this lesson
Adopt a strong industry-standard gradient boosting model for structured data.

## Outcomes
- ✅ Train an XGBoost classifier/regressor on tabular data
- ✅ Tune learning rate, depth, estimators for stability
- ✅ Monitor overfitting with eval sets and early stopping

**Time**: ~35 minutes

**Prerequisites**: Random forests lesson, Python environment with `xgboost`

## Agenda
- Boosting vs bagging recap
- Core hyperparameters and defaults that work
- Early stopping workflow

## Hands-on
- Train a small model with eval set and early stopping
- Compare against random forest baseline on the same data
- Record train/validation curves to show overfitting control

## Deliverable
- Notebook or script with training logs, metrics, and chosen params

## Checkpoint
Can you explain why lowering learning rate often requires more trees and how early stopping prevents wasted training?