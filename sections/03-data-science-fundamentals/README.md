# Section 3: Data Science Fundamentals (Minimum Must-Know)

## Overview

This section covers essential data science concepts you need for machine learning. We focus on practical understanding, not theoretical depth.

## What You'll Learn

1. **Dataset Basics**: Rows, columns, labels, features
2. **Data Splits**: Train vs validation vs test (why models lie)
3. **Model Fit**: Overfitting & underfitting (simple demos)
4. **Data Leakage**: The killer mistake in real projects
5. **Classification Metrics**: Precision, recall, F1-score
6. **Regression Metrics**: MAE, RMSE
7. **Mini Lab**: Build your first baseline model

## Why "Minimum Must-Know"?

These are concepts you'll use in EVERY ML project:

- ✅ Understanding why models fail in production
- ✅ Properly evaluating model performance
- ✅ Avoiding common mistakes that ruin models

We skip:

- ❌ Deep statistical theory
- ❌ Mathematical proofs
- ❌ Academic research details

## Prerequisites

- Section 2 completed (Python, NumPy, Pandas)
- Basic understanding of supervised learning (we'll review)

## Lessons

1. [What is a Dataset?](./01-what-is-a-dataset.md)
2. [Train, Validation, Test Splits](./02-train-val-test-splits.md)
3. [Overfitting and Underfitting](./03-overfitting-underfitting.md)
4. [Data Leakage: The Silent Killer](./04-data-leakage.md)
5. [Classification Metrics Explained](./05-classification-metrics.md)
6. [Regression Metrics Explained](./06-regression-metrics.md)
7. [Mini Lab: First Baseline Model](./07-mini-lab-baseline-model.md)

## Duration

**Estimated Time**: 6-8 hours

## Section Structure

```text
sections/03-data-science-fundamentals/
├── README.md
├── 01-what-is-a-dataset.md
├── 02-train-val-test-splits.md
├── 03-overfitting-underfitting.md
├── 04-data-leakage.md
├── 05-classification-metrics.md
├── 06-regression-metrics.md
├── 07-mini-lab-baseline-model.md
├── code/
│   ├── overfitting_demo.py
│   ├── data_leakage_demo.py
│   └── metrics_examples.py
└── labs/
    └── baseline_model/
        ├── README.md
        ├── data/
        ├── starter.py
        └── solution.py
```text
## Learning Objectives

By the end of this section, you will:

- ✅ Understand the anatomy of a dataset
- ✅ Split data properly for model evaluation
- ✅ Recognize overfitting and underfitting
- ✅ Avoid data leakage mistakes
- ✅ Choose and interpret the right metrics
- ✅ Build and evaluate a baseline model

## Key Concepts

### Dataset Structure

- **Rows**: Individual samples/examples
- **Columns**: Features (inputs) and labels (outputs)
- **Features**: What the model learns from
- **Labels**: What the model predicts

### The Three Splits

- **Training Set**: Model learns from this (60-70%)
- **Validation Set**: Tune hyperparameters (15-20%)
- **Test Set**: Final evaluation (15-20%)

### Model Fit

- **Underfitting**: Model too simple, poor on all data
- **Good Fit**: Model learns patterns, generalizes well
- **Overfitting**: Model memorizes training data, fails on new data

### Metrics

- **Classification**: Accuracy, Precision, Recall, F1
- **Regression**: MAE, MSE, RMSE, R²

## What's Next?

After this section, you'll move to [Section 4: Machine Learning Basics](../04-machine-learning-basics/README.md) where you'll build real ML models.

## Quick Start

```bash

# Navigate to this section

cd sections/03-data-science-fundamentals

# Run demos

python code/overfitting_demo.py
python code/data_leakage_demo.py
python code/metrics_examples.py

# Complete the lab

cd labs/baseline_model
python solution.py  # After trying yourself!
```text
## Common Questions

**Q: Do I need to memorize all the metrics?**

A: No! Understand when to use each one. You can always look up the formulas.

**Q: What if I already know train/test splits?**

A: Great! Still review the data leakage section - it catches everyone.

**Q: Should I read academic papers on these topics?**

A: Not necessary. Focus on practical application.

## Tips for This Section

1. **Run Every Demo**: Understanding comes from seeing
2. **Break Things**: Try overfitting on purpose
3. **Complete the Lab**: Your first real ML model!
4. **Ask "Why"**: Why this metric? Why this split ratio?
5. **Think Production**: How would this work with real data?

---

Ready to understand what makes a good dataset? Start with [What is a Dataset?](./01-what-is-a-dataset.md)
