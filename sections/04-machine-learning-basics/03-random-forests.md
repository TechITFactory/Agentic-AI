# Random Forests: Your Go-To Model

## Why this lesson
Use ensembles of trees for strong baselines that generalize better than single trees.

## Outcomes
- ✅ Train random forests for classification/regression
- ✅ Tune key params (n_estimators, max_depth, max_features)
- ✅ Use feature importances responsibly

**Time**: ~30 minutes

**Prerequisites**: Decision trees lesson

## Agenda
- Bagging and variance reduction
- OOB score vs validation set
- Handling class imbalance with class weights

## Hands-on
- Train a random forest baseline; capture OOB and validation metrics
- Tune max_depth/estimators for latency vs accuracy trade-offs
- Persist the model with joblib

## Deliverable
- Metrics table comparing tuned forest vs single tree

## Checkpoint
Can you explain why more trees reduce variance but increase latency, and how you would pick a balanced configuration?