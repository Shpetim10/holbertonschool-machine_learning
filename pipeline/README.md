# Pipeline

Holberton School data pipeline projects in Python 3: loading, cleaning,
transforming and analyzing data before it is fed to machine learning models.

## Contents

| Project | Topic | Exercises |
| --- | --- | --- |
| [`apis/`](apis/) | Consuming REST APIs with `requests`: Star Wars API (SWAPI) starships and species, and GitHub user lookups with status-code and rate-limit handling | 3 tasks (0–2) |
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

Before data can be loaded it has to be collected. The `apis/` project covers
that step when the source is a web API instead of a file: requesting pages,
following `next` links and handling errors.

## Requirements

```bash
pip install pandas numpy matplotlib requests
```
