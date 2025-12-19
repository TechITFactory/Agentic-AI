# Mini Project: Churn Predictor

## Why this mini project

Apply everything from Section 4 to build a baseline churn model with clear metrics and artifacts ready for serving.

## Outcomes

- ✅ Clean and split churn data
- ✅ Train at least two models (e.g., logistic regression, random forest/XGBoost)
- ✅ Evaluate with classification metrics and pick a champion
- ✅ Persist model + preprocessors for serving

**Time**: 2-3 hours

**Prerequisites**: All Section 4 lessons; Section 3 metrics

## Tasks

1) Load and inspect dataset; handle missing values
2) Feature engineering: scaling, encoding categoricals
3) Train baseline logistic regression; record metrics
4) Train ensemble (forest or XGBoost); compare metrics and latency
5) Select champion; persist with joblib + metadata JSON
6) Prepare a short summary: metrics, chosen hyperparameters, next steps for deployment

## Deliverables

- `notebooks/` or `src/` scripts showing training and evaluation
- `artifacts/` containing model.pkl and metadata.json
- A brief README with results and how to load/predict

## Checkpoint

Could you hand these artifacts to the Section 5 team and have them serve the model without asking follow-up questions?
