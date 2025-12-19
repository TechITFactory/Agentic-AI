"""
Shared Utilities for Agentic AI Course

Common helper functions used across sections and projects.
Import these to avoid code duplication.
"""

import os
import json
import joblib
import pandas as pd
import numpy as np
from datetime import datetime
from pathlib import Path

# ============================================================================
# FILE I/O UTILITIES
# ============================================================================

def ensure_dir(directory):
    """Create directory if it doesn't exist."""
    Path(directory).mkdir(parents=True, exist_ok=True)
    return directory


def save_json(data, filepath):
    """Save data to JSON file."""
    ensure_dir(os.path.dirname(filepath))
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"✅ Saved to {filepath}")


def load_json(filepath):
    """Load data from JSON file."""
    with open(filepath, 'r') as f:
        return json.load(f)


def save_model(model, filepath):
    """Save ML model using joblib."""
    ensure_dir(os.path.dirname(filepath))
    joblib.dump(model, filepath)
    print(f"✅ Model saved to {filepath}")


def load_model(filepath):
    """Load ML model using joblib."""
    model = joblib.load(filepath)
    print(f"✅ Model loaded from {filepath}")
    return model


# ============================================================================
# DATA UTILITIES
# ============================================================================

def load_csv(filepath, **kwargs):
    """Load CSV with common options."""
    df = pd.read_csv(filepath, **kwargs)
    print(f"✅ Loaded {len(df)} rows from {filepath}")
    return df


def save_csv(df, filepath, **kwargs):
    """Save DataFrame to CSV."""
    ensure_dir(os.path.dirname(filepath))
    df.to_csv(filepath, index=False, **kwargs)
    print(f"✅ Saved {len(df)} rows to {filepath}")


def describe_dataframe(df, name="DataFrame"):
    """Print comprehensive DataFrame description."""
    print(f"\n{'='*60}")
    print(f"{name} Description")
    print(f"{'='*60}")
    print(f"Shape: {df.shape[0]} rows × {df.shape[1]} columns")
    print(f"\nColumns: {list(df.columns)}")
    print(f"\nData types:\n{df.dtypes}")
    print(f"\nMissing values:\n{df.isnull().sum()}")
    print(f"\nMemory usage: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")


# ============================================================================
# ML UTILITIES
# ============================================================================

def train_test_split_by_date(df, date_column, test_size=0.2):
    """
    Split data by date (not random) - better for time series.
    
    Args:
        df: DataFrame with date column
        date_column: Name of date column
        test_size: Fraction for test set (default 0.2)
    
    Returns:
        train_df, test_df
    """
    df_sorted = df.sort_values(date_column)
    split_idx = int(len(df_sorted) * (1 - test_size))
    
    train_df = df_sorted.iloc[:split_idx]
    test_df = df_sorted.iloc[split_idx:]
    
    print(f"Train: {len(train_df)} samples ({date_column}: {train_df[date_column].min()} to {train_df[date_column].max()})")
    print(f"Test:  {len(test_df)} samples ({date_column}: {test_df[date_column].min()} to {test_df[date_column].max()})")
    
    return train_df, test_df


def calculate_class_weights(y):
    """Calculate class weights for imbalanced datasets."""
    from sklearn.utils.class_weight import compute_class_weight
    
    classes = np.unique(y)
    weights = compute_class_weight('balanced', classes=classes, y=y)
    weight_dict = dict(zip(classes, weights))
    
    print(f"Class distribution: {pd.Series(y).value_counts().to_dict()}")
    print(f"Class weights: {weight_dict}")
    
    return weight_dict


# ============================================================================
# EVALUATION UTILITIES
# ============================================================================

def print_classification_report(y_true, y_pred, labels=None):
    """Print detailed classification metrics."""
    from sklearn.metrics import classification_report, confusion_matrix
    
    print("\n" + "="*60)
    print("CLASSIFICATION REPORT")
    print("="*60)
    print(classification_report(y_true, y_pred, target_names=labels))
    
    print("\nConfusion Matrix:")
    cm = confusion_matrix(y_true, y_pred)
    print(cm)


def print_regression_metrics(y_true, y_pred):
    """Print regression metrics."""
    from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
    
    mae = mean_absolute_error(y_true, y_pred)
    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_true, y_pred)
    
    print("\n" + "="*60)
    print("REGRESSION METRICS")
    print("="*60)
    print(f"MAE:  {mae:.4f}")
    print(f"MSE:  {mse:.4f}")
    print(f"RMSE: {rmse:.4f}")
    print(f"R²:   {r2:.4f}")
    
    return {'mae': mae, 'mse': mse, 'rmse': rmse, 'r2': r2}


# ============================================================================
# LOGGING UTILITIES
# ============================================================================

def setup_logger(name, log_file=None, level='INFO'):
    """Set up logger with consistent formatting."""
    import logging
    
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, level))
    
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # File handler (if specified)
    if log_file:
        ensure_dir(os.path.dirname(log_file))
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    
    return logger


def log_experiment(experiment_name, params, metrics, output_dir='experiments'):
    """Log experiment parameters and results."""
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    experiment_id = f"{experiment_name}_{timestamp}"
    
    experiment_data = {
        'experiment_id': experiment_id,
        'timestamp': timestamp,
        'parameters': params,
        'metrics': metrics
    }
    
    filepath = os.path.join(output_dir, f"{experiment_id}.json")
    save_json(experiment_data, filepath)
    
    return experiment_id


# ============================================================================
# TIMING UTILITIES
# ============================================================================

import time
from contextlib import contextmanager

@contextmanager
def timer(name="Operation"):
    """Context manager for timing code blocks."""
    start_time = time.time()
    yield
    elapsed_time = time.time() - start_time
    print(f"⏱️  {name} took {elapsed_time:.2f} seconds")


# ============================================================================
# EXAMPLE USAGE
# ============================================================================

if __name__ == "__main__":
    print("Shared Utilities - Example Usage")
    print("="*60)
    
    # File I/O
    test_data = {'name': 'test', 'value': 123}
    save_json(test_data, 'temp/test.json')
    loaded_data = load_json('temp/test.json')
    print(f"Loaded: {loaded_data}")
    
    # Timer
    with timer("Example operation"):
        time.sleep(0.5)
    
    # DataFrame
    df = pd.DataFrame({
        'A': [1, 2, 3, None],
        'B': ['x', 'y', 'z', 'w']
    })
    describe_dataframe(df, "Example DataFrame")
    
    # Cleanup
    import shutil
    if os.path.exists('temp'):
        shutil.rmtree('temp')
    
    print("\n✅ All utilities working!")
