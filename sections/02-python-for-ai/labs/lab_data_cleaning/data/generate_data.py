"""
Generate sample user activity dataset for data cleaning lab.
This creates realistic messy data with common issues.
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Set seed for reproducibility
np.random.seed(42)

# Number of users
n_users = 1000

# Generate base data
data = {
    'user_id': range(1, n_users + 1),
    'signup_date': [
        (datetime.now() - timedelta(days=np.random.randint(1, 730))).strftime('%Y-%m-%d')
        for _ in range(n_users)
    ],
    'last_login': [
        (datetime.now() - timedelta(days=np.random.randint(0, 180))).strftime('%Y-%m-%d')
        for _ in range(n_users)
    ],
    'sessions': np.random.randint(0, 100, n_users),
    'features_used': np.random.randint(1, 20, n_users),
    'support_tickets': np.random.randint(0, 10, n_users),
    'revenue': np.random.uniform(10, 1000, n_users).round(2),
    'subscription_type': np.random.choice(
        ['free', 'basic', 'premium'], 
        n_users,
        p=[0.5, 0.3, 0.2]
    ),
    'churned': np.random.choice([0, 1], n_users, p=[0.7, 0.3])
}

df = pd.DataFrame(data)

# Introduce missing values
missing_indices_sessions = np.random.choice(n_users, 50, replace=False)
df.loc[missing_indices_sessions, 'sessions'] = np.nan

missing_indices_tickets = np.random.choice(n_users, 30, replace=False)
df.loc[missing_indices_tickets, 'support_tickets'] = np.nan

missing_indices_revenue = np.random.choice(n_users, 45, replace=False)
df.loc[missing_indices_revenue, 'revenue'] = np.nan

# Introduce negative revenue (data errors)
negative_indices = np.random.choice(n_users, 12, replace=False)
df.loc[negative_indices, 'revenue'] = -np.random.uniform(10, 100, 12).round(2)

# Introduce outliers in features_used
outlier_indices = np.random.choice(n_users, 8, replace=False)
df.loc[outlier_indices, 'features_used'] = np.random.randint(100, 200, 8)

# Make subscription_type inconsistent
subscription_variants = {
    'free': ['free', 'Free', 'FREE', ' free ', 'free '],
    'basic': ['basic', 'Basic', 'BASIC', ' basic', 'basic '],
    'premium': ['premium', 'Premium', 'PREMIUM', ' premium ', 'premium']
}

for idx in range(n_users):
    original = df.loc[idx, 'subscription_type']
    if np.random.random() < 0.3:  # 30% chance of inconsistency
        df.loc[idx, 'subscription_type'] = np.random.choice(subscription_variants[original])

# Save to CSV
df.to_csv('user_activity.csv', index=False)

print("Sample dataset generated: user_activity.csv")
print(f"Total rows: {len(df)}")
print(f"\nIssues introduced:")
print(f"- Missing sessions: {df['sessions'].isnull().sum()}")
print(f"- Missing support_tickets: {df['support_tickets'].isnull().sum()}")
print(f"- Missing revenue: {df['revenue'].isnull().sum()}")
print(f"- Negative revenue: {(df['revenue'] < 0).sum()}")
print(f"- Outliers in features_used: {(df['features_used'] > df['features_used'].quantile(0.95)).sum()}")
print(f"- Inconsistent subscription types: {df['subscription_type'].nunique()} unique values (should be 3)")
