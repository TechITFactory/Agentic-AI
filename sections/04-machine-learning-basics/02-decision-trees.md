# Decision Trees Explained

## Why this lesson
Learn interpretable models that capture non-linear patterns while understanding their overfitting risks.

## Outcomes
- ✅ Train decision trees for classification/regression
- ✅ Tune depth, splits, and leaf sizes to control variance
- ✅ Visualize or describe splits to stakeholders

**Time**: ~30 minutes

**Prerequisites**: Linear/logistic regression lesson

## Agenda
- How trees split data (gini/entropy/MSE)
- Hyperparameters that fight overfitting
- Feature importance caveats

## Hands-on
- Train a baseline tree; observe overfitting
- Limit `max_depth` and `min_samples_leaf`; compare metrics to baseline
- Export/import a tree model using joblib

## Deliverable
- Short report comparing an overfit tree vs a tuned tree with metrics

## Checkpoint
Can you state two ways to reduce tree overfitting and show their impact on validation performance?