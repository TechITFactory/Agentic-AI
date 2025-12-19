# Feature Engineering Guide

## Why this lesson
Improve model signal by scaling, encoding, and crafting features that align with model assumptions.

## Outcomes
- ✅ Choose scaling strategies for linear models vs trees
- ✅ Encode categorical variables (one-hot, target, ordinal) appropriately
- ✅ Create simple domain features and evaluate impact

**Time**: ~30 minutes

**Prerequisites**: Previous ML lessons; comfort with pandas

## Agenda
- When scaling matters (linear/logistic) vs when it doesn’t (trees)
- Encoding options and leakage warnings
- Quick wins: ratios, buckets, interaction terms

## Hands-on
- Scale numeric features and compare metrics for logistic regression
- One-hot encode categoricals for tree vs linear models; observe effects
- Add one domain feature and measure metric delta

## Deliverable
- Before/after metrics showing impact of at least one engineered feature

## Checkpoint
Can you describe which encoders and scalers you would pick for a mix of numeric and categorical features and why?