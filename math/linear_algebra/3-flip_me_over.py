#!/usr/bin/env python3
"""Write a function that returns the transport of 2D matrix"""


def matrix_transpose(matrix):
    """Returns transpose using list comprehension"""
    if not matrix or not matrix[0]:
        return []
    return [
        [row[col_idx] for row in matrix] for col_idx in range(len(matrix[0]))
        ]
