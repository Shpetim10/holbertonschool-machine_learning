# Holberton School — Machine Learning

This repository contains my projects, exercises, and learning journey
throughout the Machine Learning program at Holberton School.

Every project is a folder of small Python 3 scripts. Each exercise is a single
file with a function (or a short script) that solves one problem, plus a
`N-main.py` file that runs it so the result can be checked.

---

## Repository map

```
.
├── math/                      Maths foundations for machine learning
│   ├── linear_algebra/        Vectors, matrices, slicing, NumPy
│   └── plotting/              Charts and graphs with Matplotlib
│
└── pipeline/                  Getting data ready for models
    └── pandas/                Loading, cleaning, reshaping data with pandas
```

| Folder | What you learn | Main tools |
| --- | --- | --- |
| [`math/linear_algebra/`](math/linear_algebra/) | How matrices work: shape, transpose, add, concatenate, multiply, slice | pure Python, NumPy |
| [`math/plotting/`](math/plotting/) | How to draw line, scatter, log-scale, histogram, subplot and stacked-bar charts, plus advanced gradient and 3D PCA plots | Matplotlib, NumPy |
| [`pipeline/pandas/`](pipeline/pandas/) | How to turn raw Bitcoin price data into clean, analysable tables | pandas, Matplotlib |

Each folder has its own `README.md` with a file-by-file guide.

---

## How the projects fit together

```
   math/linear_algebra          math/plotting             pipeline/pandas
 ┌─────────────────────┐    ┌─────────────────────┐    ┌─────────────────────┐
 │ numbers in matrices │ -> │ see numbers as      │ -> │ real, messy data    │
 │ (NumPy arrays)      │    │ pictures (charts)   │    │ cleaned into tables │
 └─────────────────────┘    └─────────────────────┘    └──────────┬──────────┘
                                                                  │
                                              ready to be fed to ML models
```

1. **Linear algebra** gives the language of ML: data is stored in vectors and
   matrices.
2. **Plotting** makes that data visible, so patterns and mistakes are easy to
   spot.
3. **Pipeline / pandas** handles real-world data: loading files, fixing missing
   values and reshaping tables before any model sees them.

---

## Getting started

```bash
# Clone and enter the repository
git clone <repository-url>
cd holbertonschool-projects-intranet

# Install the libraries used across the projects
pip install numpy matplotlib pandas

# Run an exercise through its main file
cd math/linear_algebra
./2-main.py
```

Scripts start with `#!/usr/bin/env python3`, so they are executable
(`chmod +x file.py` if needed). Files whose names start with a digit cannot be
imported with a normal `import`, so the main files use
`__import__('2-size_me_please')` instead.

## Conventions

- Python 3, checked with `pycodestyle` (79 characters per line max)
- Every module and function has a docstring
- Folders are named `<topic>/<project>` and exercises are numbered `0-`, `1-`, …
- Large data files (`*.csv`) are not tracked by Git; see
  [`pipeline/pandas/`](pipeline/pandas/) for where to put them
