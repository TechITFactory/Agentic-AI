"""
Pandas Essentials - Examples for AI/ML Work

This file demonstrates core Pandas operations you'll use constantly in ML projects.
"""

from pathlib import Path
import tempfile

import pandas as pd
import numpy as np


def main() -> int:
    print("=" * 60)
    print("PANDAS ESSENTIALS FOR AI/ML")
    print("=" * 60)

# ====================
# 1. CREATING DATAFRAMES
# ====================
print("\n1. Creating DataFrames")
print("-" * 40)

# From dictionary
data = {
    'user_id': [1, 2, 3, 4, 5],
    'age': [25, 30, 35, 28, 42],
    'purchases': [3, 7, 2, 15, 8],
    'churned': [0, 0, 1, 0, 1]
}
df = pd.DataFrame(data)
print("DataFrame from dictionary:")
print(df)
print(f"\nShape: {df.shape}")  # (rows, columns)
print(f"Columns: {list(df.columns)}")

# ====================
# 2. READING DATA
# ====================
print("\n\n2. Reading Data")
print("-" * 40)

# Create sample CSV for demonstration
sample_csv = """user_id,name,age,city,purchases,revenue
1,Alice,25,NYC,3,150.50
2,Bob,30,LA,7,420.00
3,Charlie,35,NYC,2,100.00
4,Diana,28,Chicago,15,890.25
5,Eve,42,LA,8,560.00"""

    # Write to a temp file instead of polluting the repo folder
    tmp_dir = Path(tempfile.mkdtemp(prefix="agentic-ai-pandas-"))
    csv_path = tmp_dir / "users.csv"
    csv_path.write_text(sample_csv, encoding="utf-8")

    # Read CSV
    df = pd.read_csv(csv_path)
print("Data loaded from CSV:")
    print(df)

# ====================
# 3. INSPECTING DATA
# ====================
print("\n\n3. Inspecting Data")
print("-" * 40)

print("\nFirst 3 rows:")
print(df.head(3))

print("\nData types:")
print(df.dtypes)

print("\nBasic statistics:")
print(df.describe())

print("\nInfo:")
    print(df.info())

# ====================
# 4. SELECTING DATA
# ====================
print("\n\n4. Selecting Data")
print("-" * 40)

# Select single column (returns Series)
print("\nAges:")
    print(df['age'])

# Select multiple columns (returns DataFrame)
print("\nNames and cities:")
    print(df[['name', 'city']])

# Select rows by position
print("\nFirst 2 rows:")
    print(df.iloc[0:2])

# Select by condition (Boolean indexing)
print("\nUsers with age > 30:")
    print(df[df['age'] > 30])

print("\nUsers from NYC:")
    print(df[df['city'] == 'NYC'])

# Multiple conditions
print("\nUsers over 30 OR more than 10 purchases:")
    print(df[(df['age'] > 30) | (df['purchases'] > 10)])

# ====================
# 5. ADDING/MODIFYING COLUMNS
# ====================
print("\n\n5. Adding/Modifying Columns")
print("-" * 40)

# Create new column
df['avg_purchase_value'] = df['revenue'] / df['purchases']
print("\nAdded average purchase value:")
    print(df[['name', 'purchases', 'revenue', 'avg_purchase_value']])

# Conditional column
df['high_value'] = df['revenue'] > 400
print("\nAdded high-value flag:")
    print(df[['name', 'revenue', 'high_value']])

# ====================
# 6. HANDLING MISSING DATA
# ====================
print("\n\n6. Handling Missing Data")
print("-" * 40)

# Create data with missing values
df_missing = df.copy()
df_missing.loc[1, 'age'] = np.nan
df_missing.loc[3, 'revenue'] = np.nan

print("\nData with missing values:")
    print(df_missing)

print("\nCheck for missing values:")
    print(df_missing.isnull().sum())

# Drop rows with any missing values
df_dropped = df_missing.dropna()
print("\nAfter dropping rows with missing values:")
    print(df_dropped)

# Fill missing values
df_filled = df_missing.copy()
    df_filled['age'] = df_filled['age'].fillna(df_filled['age'].mean())
    df_filled['revenue'] = df_filled['revenue'].fillna(0)
print("\nAfter filling missing values:")
    print(df_filled)

# ====================
# 7. GROUPBY AND AGGREGATION
# ====================
print("\n\n7. GroupBy and Aggregation")
print("-" * 40)

# Group by city
print("\nAverage purchases by city:")
    print(df.groupby('city')['purchases'].mean())

print("\nMultiple aggregations:")
    city_stats = df.groupby('city').agg({
        'purchases': ['mean', 'sum'],
        'revenue': ['mean', 'sum']
    })
    print(city_stats)

# ====================
# 8. SORTING
# ====================
print("\n\n8. Sorting")
print("-" * 40)

print("\nSorted by revenue (descending):")
    print(df.sort_values('revenue', ascending=False))

print("\nSorted by city then age:")
    print(df.sort_values(['city', 'age']))

# ====================
# 9. FILTERING PATTERNS FOR ML
# ====================
print("\n\n9. Common Filtering Patterns for ML")
print("-" * 40)

# Remove outliers
revenue_mean = df['revenue'].mean()
revenue_std = df['revenue'].std()
    df_no_outliers = df[
        (df['revenue'] >= revenue_mean - 2*revenue_std) &
        (df['revenue'] <= revenue_mean + 2*revenue_std)
    ]
    print(f"\nOriginal size: {len(df)}, After outlier removal: {len(df_no_outliers)}")

# Filter by multiple conditions
    active_high_value = df[
        (df['purchases'] >= 5) &
        (df['revenue'] > 200)
    ]
    print("\nActive high-value customers:")
    print(active_high_value[['name', 'purchases', 'revenue']])

    # Best-effort cleanup
    try:
        csv_path.unlink(missing_ok=True)
        tmp_dir.rmdir()
    except Exception:
        pass

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

# ====================
# 10. SAVING DATA
# ====================
print("\n\n10. Saving Data")
print("-" * 40)

# Save to CSV
df.to_csv('processed_users.csv', index=False)
print("Data saved to 'processed_users.csv'")

# Save to JSON
df.to_json('processed_users.json', orient='records', indent=2)
print("Data saved to 'processed_users.json'")

# ====================
# CLEANUP
# ====================
import os
os.remove('temp_users.csv')
os.remove('processed_users.csv')
os.remove('processed_users.json')

print("\n" + "=" * 60)
print("KEY TAKEAWAYS:")
print("=" * 60)
print("""
1. Read data: pd.read_csv('file.csv')
2. Inspect: df.head(), df.info(), df.describe()
3. Select: df['column'], df[df['age'] > 30]
4. Handle missing: df.dropna(), df.fillna()
5. Group: df.groupby('column').agg()
6. Sort: df.sort_values('column')
7. Save: df.to_csv('file.csv')

Remember: You don't need to memorize everything!
Keep this file as reference and use the docs when needed.
""")
