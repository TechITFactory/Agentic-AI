# Mini Lab: User Activity Data Cleaning

## Objective

Clean and prepare a messy user activity dataset for machine learning. This simulates real-world data you'll encounter.

## Scenario

You work at a SaaS company. The data engineering team has dumped raw user activity logs into a CSV file. Your job is to clean it so the ML team can build a churn prediction model.

## The Dataset

**File**: `data/user_activity.csv`

**Columns**:
- `user_id`: Unique identifier
- `signup_date`: When user signed up
- `last_login`: Last login timestamp
- `sessions`: Number of sessions (has missing values)
- `features_used`: Number of features used (has outliers)
- `support_tickets`: Support tickets opened (has missing values)
- `revenue`: Revenue from user (has missing values and negative values!)
- `subscription_type`: Plan type (has inconsistent values)
- `churned`: Target variable (1=churned, 0=active)

## Problems in the Data

1. **Missing values** in multiple columns
2. **Negative revenue** values (data errors)
3. **Outliers** in features_used column
4. **Inconsistent** subscription_type values ('premium' vs 'Premium' vs 'PREMIUM')
5. **Date formats** need to be parsed
6. **Unnecessary** whitespace in string columns

## Your Task

Clean the dataset following these steps:

### Step 1: Load and Inspect

- Load the CSV file
- Check shape, column types, and missing values
- Print first few rows

### Step 2: Handle Missing Values

- `sessions`: Fill with 0 (assume no sessions)
- `support_tickets`: Fill with 0 (assume no tickets)
- `revenue`: Fill with median revenue (better than mean for skewed data)

### Step 3: Fix Data Quality Issues

- Remove rows with negative revenue
- Standardize subscription_type to lowercase
- Strip whitespace from string columns
- Convert date columns to datetime

### Step 4: Handle Outliers

- Remove rows where features_used > 95th percentile (extreme outliers)

### Step 5: Feature Engineering (Bonus)

- Create `days_since_signup` column
- Create `days_since_last_login` column
- Create `active_recently` flag (logged in within last 30 days)

### Step 6: Save Cleaned Data

- Save to `data/user_activity_cleaned.csv`
- Report how many rows were removed and why

## Expected Output

Your script should print:

```
Data Cleaning Report
====================
Original dataset: 1000 rows, 9 columns

Issues found:
- Missing values: sessions=50, support_tickets=30, revenue=45
- Negative revenue: 12 rows
- Extreme outliers in features_used: 8 rows
- Inconsistent subscription types: Fixed

Cleaning applied:
- Filled missing values
- Removed 20 bad rows (negative revenue + outliers)
- Standardized text fields
- Added 3 new features

Final dataset: 980 rows, 12 columns
Saved to: data/user_activity_cleaned.csv
```

## Starter Code

Use `starter.py` as your starting point. It has the structure and TODO comments to guide you.

## Solution

Check `solution.py` **only after** you've tried solving it yourself!

## Evaluation

Your code should:
- ✅ Handle all missing values appropriately
- ✅ Remove bad data (negative revenue)
- ✅ Fix inconsistent values
- ✅ Create at least 2 new features
- ✅ Save cleaned data to CSV
- ✅ Print a cleaning report

## Time Estimate

**30-60 minutes** if you completed the Pandas lesson.

## Tips

1. **Use `.copy()`** when creating df variants to avoid warnings
2. **Check your work** with `df.info()` and `df.describe()` frequently
3. **Test conditions** before applying them (e.g., `df[df['revenue'] < 0]` to see what you'll remove)
4. **Don't overthink** - simple solutions work fine

## Common Mistakes

❌ Forgetting to check if solution worked (use `.isnull().sum()` after filling)
❌ Modifying original data (use `.copy()`)
❌ Not checking dtypes after conversions
❌ Hardcoding today's date (use `pd.Timestamp.now()`)

## What You'll Learn

- Real-world data is messy
- Data cleaning takes 60-80% of ML project time
- Always validate your cleaning steps
- Document what you did (comments + report)

## Next Steps

After completing this lab:
1. Compare your solution with provided solution
2. Try loading the cleaned data and checking statistics
3. Think: What other cleaning steps might be needed for ML?

---

**Ready?** Start with `starter.py`!
