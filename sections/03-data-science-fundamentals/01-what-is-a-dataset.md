# What Is a Dataset? Rows, Columns, Labels, Features

## Why this lesson

Define the building blocks of any ML problem so you reason correctly about data.

## Outcomes

- ✅ Distinguish features vs labels
- ✅ Recognize rows/samples vs columns/fields
- ✅ Identify target leakage risks early

**Time**: ~15 minutes

**Prerequisites**: Section 2 (Pandas basics)

## Agenda

- Anatomy of a tabular dataset
- Feature vs label examples
- Common pitfalls in raw data

## Quick definitions

- **Row / Sample**: One observation (e.g., one customer).
- **Column / Field**: One attribute (e.g., age, tenure).
- **Features**: Inputs to the model (e.g., tenure, contract_type).
- **Label / Target**: What you want to predict (e.g., churn = 0/1).

## Hands-on

- Inspect a small CSV; mark which column is the label.
- List 3 potential leakage columns.

### Tiny example

customer_id | age | tenure_months | contract_type | churn

---------------------------------------------------------

123         | 42  | 18            | month-to-month| 1
124         | 30  | 6             | one-year      | 0

- Features: age, tenure_months, contract_type
- Label: churn

## Deliverable

- Markdown note labeling features vs target and suspected leakage fields.

## Checkpoint

Can you explain why a post-event column would be leakage for prediction?
