"""
Overfitting and Underfitting Demo

This script demonstrates the three states of model fit:
1. Underfitting - Model too simple
2. Good Fit - Model just right
3. Overfitting - Model too complex

Visual demonstration of why we need to balance model complexity.
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

print("=" * 70)
print("OVERFITTING AND UNDERFITTING DEMONSTRATION")
print("=" * 70)

# ============================================================================
# 1. GENERATE SYNTHETIC DATA
# ============================================================================
print("\n1. Generating Synthetic Data")
print("-" * 70)

# Set seed for reproducibility
np.random.seed(42)

# Generate data with a known pattern (quadratic relationship)
X = np.sort(np.random.uniform(0, 10, 100))
y_true = 2 + 3*X - 0.5*X**2  # True underlying pattern
y = y_true + np.random.normal(0, 5, 100)  # Add noise

# Split data
X_train, X_test = X[:70], X[70:]
y_train, y_test = y[:70], y[70:]

print(f"Training samples: {len(X_train)}")
print(f"Test samples: {len(X_test)}")
print(f"True pattern: y = 2 + 3x - 0.5x²  (with noise)")

# ============================================================================
# 2. UNDERFITTING - Model Too Simple
# ============================================================================
print("\n\n2. Underfitting: Using a Constant (Mean) Model")
print("-" * 70)

# Simplest model: always predict the mean
mean_model = np.mean(y_train)
y_train_pred_underfit = np.full(len(y_train), mean_model)
y_test_pred_underfit = np.full(len(y_test), mean_model)

train_mse_underfit = mean_squared_error(y_train, y_train_pred_underfit)
test_mse_underfit = mean_squared_error(y_test, y_test_pred_underfit)
train_r2_underfit = r2_score(y_train, y_train_pred_underfit)
test_r2_underfit = r2_score(y_test, y_test_pred_underfit)

print(f"Model: Always predict {mean_model:.2f}")
print(f"\nTraining Performance:")
print(f"  MSE: {train_mse_underfit:.2f}")
print(f"  R²:  {train_r2_underfit:.3f}")
print(f"\nTest Performance:")
print(f"  MSE: {test_mse_underfit:.2f}")
print(f"  R²:  {test_r2_underfit:.3f}")
print(f"\n❌ Problem: Both training and test performance are poor!")
print(f"   This is UNDERFITTING - model too simple to capture patterns")

# ============================================================================
# 3. GOOD FIT - Appropriate Model Complexity
# ============================================================================
print("\n\n3. Good Fit: Polynomial of Degree 2")
print("-" * 70)

# Create polynomial features (degree 2)
poly_good = PolynomialFeatures(degree=2, include_bias=False)
X_train_poly_good = poly_good.fit_transform(X_train.reshape(-1, 1))
X_test_poly_good = poly_good.transform(X_test.reshape(-1, 1))

# Train model
model_good = LinearRegression()
model_good.fit(X_train_poly_good, y_train)

# Predictions
y_train_pred_good = model_good.predict(X_train_poly_good)
y_test_pred_good = model_good.predict(X_test_poly_good)

train_mse_good = mean_squared_error(y_train, y_train_pred_good)
test_mse_good = mean_squared_error(y_test, y_test_pred_good)
train_r2_good = r2_score(y_train, y_train_pred_good)
test_r2_good = r2_score(y_test, y_test_pred_good)

print(f"Model: Polynomial degree 2 (matches true pattern)")
print(f"\nTraining Performance:")
print(f"  MSE: {train_mse_good:.2f}")
print(f"  R²:  {train_r2_good:.3f}")
print(f"\nTest Performance:")
print(f"  MSE: {test_mse_good:.2f}")
print(f"  R²:  {test_r2_good:.3f}")
print(f"\n✅ Good! Training and test performance are similar")
print(f"   This is a GOOD FIT - model complexity matches the data")

# ============================================================================
# 4. OVERFITTING - Model Too Complex
# ============================================================================
print("\n\n4. Overfitting: Polynomial of Degree 15")
print("-" * 70)

# Create polynomial features (degree 15 - way too complex!)
poly_overfit = PolynomialFeatures(degree=15, include_bias=False)
X_train_poly_overfit = poly_overfit.fit_transform(X_train.reshape(-1, 1))
X_test_poly_overfit = poly_overfit.transform(X_test.reshape(-1, 1))

# Train model
model_overfit = LinearRegression()
model_overfit.fit(X_train_poly_overfit, y_train)

# Predictions
y_train_pred_overfit = model_overfit.predict(X_train_poly_overfit)
y_test_pred_overfit = model_overfit.predict(X_test_poly_overfit)

train_mse_overfit = mean_squared_error(y_train, y_train_pred_overfit)
test_mse_overfit = mean_squared_error(y_test, y_test_pred_overfit)
train_r2_overfit = r2_score(y_train, y_train_pred_overfit)
test_r2_overfit = r2_score(y_test, y_test_pred_overfit)

print(f"Model: Polynomial degree 15 (way too complex)")
print(f"\nTraining Performance:")
print(f"  MSE: {train_mse_overfit:.2f}")
print(f"  R²:  {train_r2_overfit:.3f}")
print(f"\nTest Performance:")
print(f"  MSE: {test_mse_overfit:.2f}")
print(f"  R²:  {test_r2_overfit:.3f}")
print(f"\n❌ Problem: Great training performance, poor test performance!")
print(f"   This is OVERFITTING - model memorized training data")

# ============================================================================
# 5. COMPARISON
# ============================================================================
print("\n\n5. Side-by-Side Comparison")
print("=" * 70)

comparison = pd.DataFrame({
    'Model': ['Underfitting (Mean)', 'Good Fit (Degree 2)', 'Overfitting (Degree 15)'],
    'Train MSE': [train_mse_underfit, train_mse_good, train_mse_overfit],
    'Test MSE': [test_mse_underfit, test_mse_good, test_mse_overfit],
    'Train R²': [train_r2_underfit, train_r2_good, train_r2_overfit],
    'Test R²': [test_r2_underfit, test_r2_good, test_r2_overfit],
    'Gap (Train-Test R²)': [
        abs(train_r2_underfit - test_r2_underfit),
        abs(train_r2_good - test_r2_good),
        abs(train_r2_overfit - test_r2_overfit)
    ]
})

print(comparison.to_string(index=False))

# ============================================================================
# 6. KEY INSIGHTS
# ============================================================================
print("\n\n6. Key Insights")
print("=" * 70)

print("""
UNDERFITTING:
- Both train and test scores are poor
- Model too simple to capture patterns
- Solution: Increase model complexity

GOOD FIT:
- Train and test scores are similar and good
- Model captures real patterns
- Solution: This is what we want!

OVERFITTING:
- Train score excellent, test score poor
- Large gap between train and test performance
- Model memorized training data, can't generalize
- Solution: Reduce model complexity, add regularization, get more data

THE DANGER OF OVERFITTING:
In production, you only see training data during development.
Without proper validation, you might deploy an overfitted model
that fails on real user data!
""")

# ============================================================================
# 7. HOW TO DETECT IN PRACTICE
# ============================================================================
print("\n\n7. How to Detect Overfitting in Your Projects")
print("=" * 70)

print("""
1. ALWAYS use a validation/test set
   - Never evaluate only on training data
   - If train score >> test score: likely overfitting

2. Watch for these signs:
   - Training accuracy: 99%, Test accuracy: 70% ← OVERFITTING
   - Training loss decreases, validation loss increases ← OVERFITTING
   - Model works perfectly in dev, fails in production ← OVERFITTING

3. Use cross-validation:
   - Helps detect overfitting across multiple splits
   - More reliable than single train/test split

4. Learning curves:
   - Plot training and validation scores vs training set size
   - Converging scores = good, diverging = overfitting

5. Start simple:
   - Begin with simple models (baseline)
   - Increase complexity only if needed
   - Simpler models are less likely to overfit
""")

# ============================================================================
# 8. HOW TO FIX
# ============================================================================
print("\n\n8. How to Fix Overfitting")
print("=" * 70)

print("""
If you detect overfitting, try these (in order):

1. Get more training data
   - Most effective solution
   - More data = harder to memorize

2. Reduce model complexity
   - Use simpler algorithms
   - Reduce number of features
   - Lower polynomial degree

3. Add regularization
   - L1 (Lasso) or L2 (Ridge) regularization
   - Penalizes complex models
   - We'll cover this in Section 4

4. Use cross-validation
   - Better estimates of generalization
   - Helps tune hyperparameters

5. Feature selection
   - Remove irrelevant features
   - Less noise for model to memorize

6. Early stopping (for neural networks)
   - Stop training when validation performance degrades
""")

print("\n" + "=" * 70)
print("KEY TAKEAWAY")
print("=" * 70)
print("""
The goal is NOT to maximize training performance.
The goal is to maximize GENERALIZATION to new, unseen data.

Always evaluate on held-out test data!
""")
