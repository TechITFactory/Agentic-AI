"""
User Activity Data Cleaning - Starter Code

Complete the TODOs to clean the messy user activity dataset.
"""

import pandas as pd
import numpy as np
from datetime import datetime

def load_data(filepath):
    """Load the dataset from CSV."""
    # TODO: Load CSV file using pandas
    # Hint: pd.read_csv()
    pass

def inspect_data(df):
    """Print information about the dataset."""
    print("=" * 60)
    print("DATA INSPECTION")
    print("=" * 60)
    
    # TODO: Print shape of dataframe
    # TODO: Print first 5 rows
    # TODO: Print data types
    # TODO: Print number of missing values per column
    pass

def handle_missing_values(df):
    """Handle missing values in the dataset."""
    print("\n" + "=" * 60)
    print("HANDLING MISSING VALUES")
    print("=" * 60)
    
    df_clean = df.copy()
    
    # TODO: Fill missing sessions with 0
    # TODO: Fill missing support_tickets with 0
    # TODO: Fill missing revenue with median revenue
    # Hint: df['column'].fillna(value, inplace=True)
    
    print("Missing values after filling:")
    # TODO: Print missing value counts
    
    return df_clean

def fix_data_quality(df):
    """Fix data quality issues."""
    print("\n" + "=" * 60)
    print("FIXING DATA QUALITY ISSUES")
    print("=" * 60)
    
    df_clean = df.copy()
    
    # TODO: Remove rows with negative revenue
    # Hint: df = df[df['revenue'] >= 0]
    negative_revenue_count = 0  # TODO: Calculate this
    
    # TODO: Standardize subscription_type to lowercase
    # Hint: df['column'] = df['column'].str.lower()
    
    # TODO: Strip whitespace from subscription_type
    # Hint: df['column'] = df['column'].str.strip()
    
    # TODO: Convert signup_date to datetime
    # Hint: pd.to_datetime(df['column'])
    
    # TODO: Convert last_login to datetime
    
    print(f"Removed {negative_revenue_count} rows with negative revenue")
    print(f"Subscription types: {sorted(df_clean['subscription_type'].unique())}")
    
    return df_clean

def handle_outliers(df):
    """Remove extreme outliers."""
    print("\n" + "=" * 60)
    print("HANDLING OUTLIERS")
    print("=" * 60)
    
    df_clean = df.copy()
    
    # TODO: Calculate 95th percentile of features_used
    # Hint: df['column'].quantile(0.95)
    threshold = 0  # TODO: Calculate this
    
    # TODO: Remove rows where features_used > threshold
    outliers_count = 0  # TODO: Calculate this
    
    print(f"Removed {outliers_count} rows with extreme outliers in features_used")
    print(f"Threshold used: {threshold}")
    
    return df_clean

def create_features(df):
    """Create new features for ML."""
    print("\n" + "=" * 60)
    print("CREATING NEW FEATURES")
    print("=" * 60)
    
    df_clean = df.copy()
    
    # TODO: Create days_since_signup
    # Hint: (pd.Timestamp.now() - df['signup_date']).dt.days
    
    # TODO: Create days_since_last_login
    
    # TODO: Create active_recently (1 if logged in within 30 days, else 0)
    # Hint: df['active_recently'] = (df['days_since_last_login'] <= 30).astype(int)
    
    print("New features created:")
    print("- days_since_signup")
    print("- days_since_last_login")
    print("- active_recently")
    
    return df_clean

def save_cleaned_data(df, output_path):
    """Save the cleaned dataset."""
    # TODO: Save dataframe to CSV
    # Hint: df.to_csv(output_path, index=False)
    print(f"\nCleaned data saved to: {output_path}")

def print_report(df_original, df_cleaned):
    """Print data cleaning report."""
    print("\n" + "=" * 60)
    print("DATA CLEANING REPORT")
    print("=" * 60)
    
    # TODO: Calculate and print:
    # - Original shape
    # - Final shape
    # - Number of rows removed
    # - Number of columns added
    pass

def main():
    """Main function to run the data cleaning pipeline."""
    
    # File paths
    input_file = 'data/user_activity.csv'
    output_file = 'data/user_activity_cleaned.csv'
    
    # Load data
    print("Loading data...")
    df = load_data(input_file)
    df_original = df.copy()
    
    # Inspect
    inspect_data(df)
    
    # Clean
    df = handle_missing_values(df)
    df = fix_data_quality(df)
    df = handle_outliers(df)
    df = create_features(df)
    
    # Save
    save_cleaned_data(df, output_file)
    
    # Report
    print_report(df_original, df)
    
    print("\n✅ Data cleaning complete!")

if __name__ == "__main__":
    main()
