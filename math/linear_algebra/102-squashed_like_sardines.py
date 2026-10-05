#!/usr/bin/env python3
"""Write a function that concatenates two matrices along a specific axis:"""


def cat_matrices(mat1, mat2, axis=0):
    """Concatenates two matrices along a specific axis."""

    if axis < 0:
        return None

    if axis == 0:
        return mat1 + mat2

    if len(mat1) != len(mat2):
        return None

    result = []

    for i in range(len(mat1)):
        tmp = cat_matrices(mat1[i], mat2[i], axis - 1)

        if tmp is None:
            return None

        result.append(tmp)

    return result
