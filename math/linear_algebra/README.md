# Linear Algebra

Introductory linear algebra exercises in Python 3. The project teaches how to
work with **vectors** (1D arrays) and **matrices** (2D and higher), first by
hand in pure Python, then the fast way with **NumPy**, and finally by
generalising the pure Python versions to any number of dimensions.

```
 Part 1 (tasks 0-8)         Part 2 (tasks 9-14)         Part 3 (tasks 100-102)
 pure Python lists   ──►    the same ideas in    ──►    arbitrary-dimension
 loops, slices, [ ]         NumPy: one-liners           matrices, recursion
```

## Quick start

```bash
pip install numpy
cd math/linear_algebra
./2-main.py            # every N-main.py runs the matching task
```

Each exercise is a pair: `N-name.py` holds the solution and `N-main.py` is a
small script that imports it (with `__import__`, because the file names start
with a digit) and prints some examples.

## Vocabulary

```
  Vector (1D)       Matrix (2D)              3D array
                                             (a stack of matrices)
  [1, 2, 3]         [[1, 2, 3],              [[[1, 2], [3, 4]],
                     [4, 5, 6]]               [[5, 6], [7, 8]]]

  shape: [3]        shape: [2, 3]            shape: [2, 2, 2]
                    (2 rows, 3 columns)
```

---

## Part 1 — Pure Python (tasks 0–8)

| File | Description |
| --- | --- |
| `0-slice_me_up.py` | Slices a list to print its first two, last five, and 2nd–6th elements. |
| `1-trim_me_down.py` | Slices a matrix to extract its middle two columns. |
| `2-size_me_please.py` | `matrix_shape(matrix)` returns the shape of a matrix as a list of dimensions (uses a recursive helper). |
| `3-flip_me_over.py` | `matrix_transpose(matrix)` returns the transpose of a 2D matrix. |
| `4-line_up.py` | `add_arrays(arr1, arr2)` adds two arrays element-wise, or returns `None` if shapes differ. |
| `5-across_the_planes.py` | `add_matrices2D(mat1, mat2)` adds two 2D matrices element-wise, or returns `None` if shapes differ. |
| `6-howdy_partner.py` | `cat_arrays(arr1, arr2)` concatenates two arrays. |
| `7-gettin_cozy.py` | `cat_matrices2D(mat1, mat2, axis=0)` concatenates two 2D matrices along a given axis, or returns `None` if incompatible. |
| `8-ridin_bareback.py` | `mat_mul(mat1, mat2)` performs matrix multiplication, or returns `None` if incompatible. |

### Slicing: `list[start:stop]`

```
 index:      0  1  2  3  4  5  6  7  8
 arr = [     9, 8, 2, 3, 9, 4, 1, 0, 3 ]

 arr[:2]     9  8                          first two     (task 0)
 arr[4:]                 9  4  1  0  3     last five     (task 0)
 arr[1:6]       8  2  3  9  4              2nd to 6th    (task 0)
```

Task 1 applies the same idea to every row: `[row[2:4] for row in matrix]`
keeps columns 2 and 3 (the middle two).

### Transpose: rows become columns (task 3)

```
  1 2 3          1 4
  4 5 6    ──►   2 5
                 3 6
  (2 x 3)        (3 x 2)
```

### Element-wise addition (tasks 4 and 5)

Shapes must match, otherwise the function returns `None`.

```
  1 2     5 6     1+5 2+6     6  8
  3 4  +  7 8  =  3+7 4+8  =  10 12
```

### Concatenation: `axis` picks the direction (tasks 6 and 7)

```
 axis=0  stack rows (columns must match)    axis=1  glue columns (rows must match)

   1 2                                         1 2     7        1 2 7
   3 4      +  [5 6]  =   3 4                  3 4  +  8   =    3 4 8
                          5 6
```

### Matrix multiplication (task 8)

The inner sizes must match; the outer sizes give the result shape.

```
      (m x n)   ·   (n x p)    =   (m x p)
      3 x 2         2 x 4          3 x 4

  Each cell [i][j] = sum over k of  mat1[i][k] * mat2[k][j]
                     (row i of mat1  ·  column j of mat2)
```

---

## Part 2 — NumPy (tasks 9–14)

NumPy does in one line what Part 1 needed loops for.

| File | Description |
| --- | --- |
| `9-let_the_butcher_slice_it.py` | Slices a NumPy matrix to get the middle two rows, the middle two columns and the bottom-right 3×3 block. |
| `10-ill_use_my_scale.py` | `np_shape(matrix)` returns the shape of a `numpy.ndarray` (`matrix.shape`). |
| `11-the_western_exchange.py` | `np_transpose(matrix)` returns the transpose (`matrix.T`). |
| `12-bracin_the_elements.py` | `np_elementwise(mat1, mat2)` returns the element-wise sum, difference, product and quotient (works with a scalar too). |
| `13-cats_got_your_tongue.py` | `np_cat(mat1, mat2, axis=0)` concatenates two matrices along an axis (`np.concatenate`). |
| `14-saddle_up.py` | `np_matmul(mat1, mat2)` performs matrix multiplication (`@`). |

### Part 1 versus Part 2

| Operation | Pure Python | NumPy |
| --- | --- | --- |
| Shape | `matrix_shape(m)` (recursion) | `m.shape` |
| Transpose | nested list comprehension | `m.T` |
| Add | loops over rows and columns | `a + b` |
| Concatenate | `+` / list comprehension | `np.concatenate((a, b), axis)` |
| Multiply | three nested loops | `a @ b` |

### NumPy 2D slicing: `matrix[rows, columns]`

```
 matrix =   1  2  3  4  5  6
            7  8  9 10 11 12
           13 14 15 16 17 18
           19 20 21 22 23 24

 matrix[1:3, :]    middle two rows       -> rows 1 and 2, all columns
 matrix[:, 2:4]    middle two columns    -> all rows, columns 2 and 3
 matrix[1:, 3:]    bottom-right 3x3      -> from row 1 down, from column 3 right
```

---

## Part 3 — Advanced tasks (100–102)

| File | Description |
| --- | --- |
| `100-slice_like_a_ninja.py` | `np_slice(matrix, axes={})` slices a matrix along any axes. `axes` maps an axis number to a slice tuple, e.g. `{1: (1, 3)}` is `matrix[:, 1:3]` and `{0: (2,), 2: (None, None, -2)}` is `matrix[:2, :, ::-2]`. Works on a copy, so the input is not modified. |
| `101-the_whole_barn.py` | `add_matrices(mat1, mat2)` adds two matrices of **any** number of dimensions element-wise, or returns `None` if their shapes differ. Uses recursion and `matrix_shape` from task 2. |
| `102-squashed_like_sardines.py` | `cat_matrices(mat1, mat2, axis=0)` concatenates two matrices of **any** number of dimensions along a given axis, or returns `None` if they are incompatible. |

### Recursion peels one dimension at a time

```
 add_matrices([[1, 2], [3, 4]], [[5, 6], [7, 8]])
        │
        ├─ add_matrices([1, 2], [5, 6])  ──►  [6, 8]
        └─ add_matrices([3, 4], [7, 8])  ──►  [10, 12]
        │
        ▼
   [[6, 8], [10, 12]]
```

A matrix that is no longer a list is a plain number, which stops the
recursion. `cat_matrices` works the same way: it walks down `axis` levels and
joins the lists with `+` once `axis` reaches 0.

---

## Requirements

- Python 3
- Part 2 and task 100 need `numpy` (`pip install numpy`); `102-main.py` also
  uses it to compare timings
- Part 1 and tasks 101–102 use plain Python lists only
- Code follows `pycodestyle`; every module and function has a docstring
