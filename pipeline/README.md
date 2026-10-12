# Pipeline

Holberton School data pipeline projects in Python 3: loading, cleaning,
transforming and analyzing data before it is fed to machine learning models.

## Contents

| Project | Topic | Exercises |
| --- | --- | --- |
| [`pandas/`](pandas/) | Introduction to `pandas` DataFrames using Bitcoin 1-minute price data: creating, loading, renaming, slicing, sorting, cleaning, merging, analysing and plotting | 15 tasks (0–14) |

## What is a data pipeline?

Raw data is rarely ready to use. A pipeline is the chain of small steps that
turns it into something a model can learn from:

```
 ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐
 │  Load    │ → │  Clean   │ → │ Reshape  │ → │ Analyze  │ → │ Visualize│
 │ read CSV │   │ fix NaNs │   │ index,   │   │ describe │   │ plot     │
 │          │   │          │   │ slice,   │   │ stats    │   │          │
 │          │   │          │   │ merge    │   │          │   │          │
 └──────────┘   └──────────┘   └──────────┘   └──────────┘   └──────────┘
        every step is one small, testable function in `pandas/`
```

## Requirements

```bash
pip install pandas numpy matplotlib
```
