# Datasets Directory

This directory contains sample datasets used throughout the course for labs and projects.

## Structure

```
datasets/
├── README.md           # This file
├── churn/             # Customer churn data (Sections 4, 12)
├── documents/         # Sample docs for RAG (Sections 10, 13)
├── logs/              # System logs for agent (Sections 2, 14)
└── .gitkeep          # Keep directory in git
```

## Dataset Sources

### Churn Dataset (Sections 4 & 12)
- **Description**: Customer churn prediction dataset
- **Size**: ~10,000 customers
- **Features**: Demographics, usage patterns, support interactions
- **Target**: Binary classification (churned: 0/1)
- **Generated**: Synthetically created for course

### Documents (Sections 10 & 13)
- **Description**: Sample documents for RAG system
- **Types**: PDF, Markdown, Text
- **Topics**: Technical documentation, API guides, tutorials
- **Purpose**: Building document Q&A systems

### Logs (Sections 2 & 14)
- **Description**: System logs for analysis
- **Format**: JSON and plain text
- **Purpose**: Log parsing, anomaly detection, agent tools

## Usage

Each dataset includes:
- **README.md**: Dataset description and metadata
- **Data files**: Actual data (CSV, JSON, etc.)
- **Generation script**: Code to regenerate if needed
- **Sample notebook**: EDA and exploration

## Data Privacy

All datasets are either:
- ✅ Synthetically generated
- ✅ Publicly available with proper attribution
- ✅ Created specifically for educational purposes

**No real user data is included.**

## Generating Datasets

Some datasets are generated programmatically. To regenerate:

```bash
# Navigate to dataset directory
cd datasets/churn

# Run generation script
python generate_data.py
```

## Adding Your Own Data

For projects, you can add your own datasets:

1. Create a new subdirectory
2. Add your data files
3. Include a README describing the dataset
4. Update .gitignore if data is large or sensitive

## Best Practices

When working with datasets:
- ✅ Always inspect data first (shape, dtypes, missing values)
- ✅ Check for class imbalance in classification tasks
- ✅ Look for outliers and data quality issues
- ✅ Document any preprocessing steps
- ✅ Never commit large files (>50MB) to git

## Dataset Details

### Size Guidelines
- **Small**: < 10MB (commit to git)
- **Medium**: 10-100MB (use git LFS or download script)
- **Large**: > 100MB (provide download instructions)

### File Formats
- **CSV**: Most common, good for tabular data
- **JSON**: Good for nested/hierarchical data
- **Parquet**: Efficient for large datasets
- **TXT**: For documents and logs

## Questions?

If you need help with datasets:
1. Check the dataset's README
2. Look at the generation script
3. Use GitHub Discussions for questions

## Cleanup

To remove generated datasets:

```bash
# Remove all generated data (keeps scripts)
find datasets -name "*.csv" -delete
find datasets -name "*.json" -delete
find datasets -name "*.parquet" -delete
```

Regenerate when needed using the provided scripts.
