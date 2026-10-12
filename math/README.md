# Math

Holberton School math projects in Python 3. They cover the maths that machine
learning is built on: how data is stored in matrices, and how to look at it
with charts.

## Contents

| Project | Topic | Exercises |
| --- | --- | --- |
| [`linear_algebra/`](linear_algebra/) | Vectors and matrices: slicing, shape, transpose, addition, concatenation, multiplication, first in pure Python, then with NumPy | 15 core tasks + 3 advanced |
| [`plotting/`](plotting/) | Matplotlib charts: line, scatter, log scale, two lines, histogram, subplots, stacked bars | 7 tasks |

## How the two projects connect

```
 linear_algebra                            plotting
 ──────────────                            ────────
 np.arange, np.random, matrices   ──────►  the same NumPy arrays are the
 (create and transform numbers)            input of plt.plot / plt.hist / ...
                                           (draw the numbers)
```

The `plotting` exercises build their data with NumPy (`np.arange`,
`np.exp`, `np.random`), which is the library introduced in the second half of
`linear_algebra`.

## Suggested order

1. [`linear_algebra/`](linear_algebra/) — learn how matrices are stored and
   manipulated.
2. [`plotting/`](plotting/) — turn arrays into pictures.

## Requirements

```bash
pip install numpy matplotlib
```
