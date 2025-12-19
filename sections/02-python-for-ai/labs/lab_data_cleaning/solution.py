"""
User Activity Data Cleaning - Complete Solution

This is the complete solution for the data cleaning lab.
Study this after attempting the lab yourself!
"""

import pandas as pd
import numpy as np
from datetime import datetime

def load_data(filepath):
    """Load the dataset from CSV."""
    df = pd.read_csv(filepath)
    return df

def inspect_data(df):
    """Print information about the dataset."""
    print("=" * 60)
    print("DATA INSPECTION")
    print("=" * 60)
    
    print(f"\nShape: {df.shape}")
    print(f"\nFirst 5 rows:")
    print(df.head())
    
    print(f"\nData types:")
    print(df.dtypes)
    
    print(f"\nMissing values:")
    print(df.isnull().sum())
    
    print(f"\nBasic statistics:")
    print(df.describe())

def handle_missing_values(df):
    """Handle missing values in the dataset."""
    print("\n" + "=" * 60)
    print("HANDLING MISSING VALUES")
    print("=" * 60)
    
    df_clean = df.copy()
    
    # Count missing values before
    missing_before = df_clean.isnull().sum()
    print(f"\nMissing values before:")
    print(missing_before[missing_before > 0])
    
    # Fill missing sessions with 0 (no sessions recorded)
    df_clean['sessions'] = df_clean['sessions'].fillna(0)
    
    # Fill missing support_tickets with 0 (no tickets opened)
    df_clean['support_tickets'] = df_clean['support_tickets'].fillna(0)
    
    # Fill missing revenue with median (better than mean for skewed data)
    median_revenue = df_clean['revenue'].median()
    df_clean['revenue'] = df_clean['revenue'].fillna(median_revenue)
    
    # Verify no missing values remain
    print(f"\nMissing values after filling:")
    print(df_clean.isnull().sum())
    
    return df_clean

def fix_data_quality(df):
    """Fix data quality issues."""
    print("\n" + "=" * 60)
    print("FIXING DATA QUALITY ISSUES")
    print("=" * 60)
    
    df_clean = df.copy()
    
    # Count rows with negative revenue
    negative_revenue_count = (df_clean['revenue'] < 0).sum()
    print(f"\nRows with negative revenue: {negative_revenue_count}")
    
    # Remove rows with negative revenue (data errors)
    df_clean = df_clean[df_clean['revenue'] >= 0]
    
    # Check subscription type variations
    print(f"\nSubscription types before standardization:")
    print(df_clean['subscription_type'].unique())
    
    # Standardize subscription_type to lowercase and strip whitespace
    df_clean['subscription_type'] = df_clean['subscription_type'].str.lower().str.strip()
    
    print(f"\nSubscription types after standardization:")
    print(sorted(df_clean['subscription_type'].unique()))
    
    # Convert date columns to datetime
    df_clean['signup_date'] = pd.to_datetime(df_clean['signup_date'])
    df_clean['last_login'] = pd.to_datetime(df_clean['last_login'])
    
    print(f"\nDate columns converted to datetime")
    print(f"signup_date dtype: {df_clean['signup_date'].dtype}")
    print(f"last_login dtype: {df_clean['last_login'].dtype}")
    
    return df_clean

def handle_outliers(df):
    """Remove extreme outliers."""
    print("\n" + "=" * 60)
    print("HANDLING OUTLIERS")
    print("=" * 60)
    
    df_clean = df.copy()
    
    # Calculate 95th percentile for features_used
    threshold = df_clean['features_used'].quantile(0.95)
    
    # Count outliers
    outliers_count = (df_clean['features_used'] > threshold).sum()
    
    print(f"\n95th percentile threshold for features_used: {threshold}")
    print(f"Rows with extreme outliers: {outliers_count}")
    
    # Remove outliers
    df_clean = df_clean[df_clean['features_used'] <= threshold]
    
    print(f"Rows after removing outliers: {len(df_clean)}")
    
    return df_clean

def create_features(df):
    """Create new features for ML."""
    print("\n" + "=" * 60)
    print("CREATING NEW FEATURES")
    print("=" * 60)
    
    df_clean = df.copy()
    
    # Create days_since_signup
    df_clean['days_since_signup'] = (pd.Timestamp.now() - df_clean['signup_date']).dt.days
    
    # Create days_since_last_login
    df_clean['days_since_last_login'] = (pd.Timestamp.now() - df_clean['last_login']).dt.days
    
    # Create active_recently flag (logged in within last 30 days)
    df_clean['active_recently'] = (df_clean['days_since_last_login'] <= 30).astype(int)
    
    print("\nNew features created:")
    print(f"- days_since_signup: min={df_clean['days_since_signup'].min()}, "
          f"max={df_clean['days_since_signup'].max()}")
    print(f"- days_since_last_login: min={df_clean['days_since_last_login'].min()}, "
          f"max={df_clean['days_since_last_login'].max()}")
    print(f"- active_recently: {df_clean['active_recently'].sum()} users active recently "
          f"({df_clean['active_recently'].mean()*100:.1f}%)")
    
    return df_clean

def save_cleaned_data(df, output_path):
    """Save the cleaned dataset."""
    df.to_csv(output_path, index=False)
    print(f"\n✅ Cleaned data saved to: {output_path}")

def print_report(df_original, df_cleaned):
    """Print comprehensive data cleaning report."""
    print("\n" + "=" * 60)
    print("DATA CLEANING REPORT")
    print("=" * 60)
    
    print(f"\nOriginal dataset: {df_original.shape[0]} rows, {df_original.shape[1]} columns")
    print(f"Final dataset: {df_cleaned.shape[0]} rows, {df_cleaned.shape[1]} columns")
    
    rows_removed = df_original.shape[0] - df_cleaned.shape[0]
    cols_added = df_cleaned.shape[1] - df_original.shape[1]
    
    print(f"\nRows removed: {rows_removed} ({rows_removed/df_original.shape[0]*100:.1f}%)")
    print(f"Columns added: {cols_added}")
    
    print(f"\nIssues fixed:")
    print(f"- Missing values filled in: sessions, support_tickets, revenue")
    print(f"- Negative revenue rows removed")
    print(f"- Subscription types standardized")
    print(f"- Date columns converted to datetime")
    print(f"- Extreme outliers removed (features_used > 95th percentile)")
    
    print(f"\nNew features:")
    print(f"- days_since_signup")
    print(f"- days_since_last_login")
    print(f"- active_recently")
    
    print(f"\nData quality metrics:")
    print(f"- No missing values: {df_cleaned.isnull().sum().sum() == 0}")
    print(f"- No negative revenue: {(df_cleaned['revenue'] < 0).sum() == 0}")
    print(f"- Subscription types: {sorted(df_cleaned['subscription_type'].unique())}")
    print(f"- Revenue range: ${df_cleaned['revenue'].min():.2f} - ${df_cleaned['revenue'].max():.2f}")

def main():
    """Main function to run the data cleaning pipeline."""
    
    # File paths
    input_file = 'data/user_activity.csv'
    output_file = 'data/user_activity_cleaned.csv'
    
    # Load data
    print("📂 Loading data...")
    df = load_data(input_file)
    df_original = df.copy()
    
    # Inspect
    inspect_data(df)
    
    # Clean step by step
    df = handle_missing_values(df)
    df = fix_data_quality(df)
    df = handle_outliers(df)
    df = create_features(df)
    
    # Save
    save_cleaned_data(df, output_file)
    
    # Report
    print_report(df_original, df)
    
    print("\n" + "=" * 60)
    print("✅ DATA CLEANING COMPLETE!")
    print("=" * 60)
    print("\nYou can now use the cleaned data for machine learning!")
    print(f"Load it with: pd.read_csv('{output_file}')")

if __name__ == "__main__":
    main()
