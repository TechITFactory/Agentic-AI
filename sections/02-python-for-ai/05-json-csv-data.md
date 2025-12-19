# Working with JSON/CSV (Log-Like Data)

## Why this lesson
Most real systems emit JSON/CSV logs; you must parse and transform them quickly.

## Outcomes
- ✅ Read/write JSON and CSV safely
- ✅ Normalize nested JSON to tabular form
- ✅ Handle schema drift basics

**Time**: ~25 minutes

**Prerequisites**: Pandas essentials

## Agenda
- `json` module vs pandas readers
- `json_normalize` for nested data
- Handling missing/extra fields

## Hands-on
- Load a nested JSON log; flatten to columns
- Append multiple JSON lines into one DataFrame; write CSV

## Deliverable
- A script that ingests a JSONL file and emits a clean CSV

## Checkpoint
Can you explain how you’d handle a new optional field appearing mid-file?