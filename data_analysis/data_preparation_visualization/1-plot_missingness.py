#!/usr/bin/env python3
"""Module that plots the missing values of a DataFrame."""
import matplotlib.pyplot as plt
import numpy as np


def plot_missingness(df):
    """Plot where the missing values of a DataFrame are.

    Draws one horizontal line per column (y axis) and one vertical tick
    for every row (x axis) whose value in that column is missing. A column
    without ticks has no missing values.

    Args:
        df (pandas.DataFrame): the data to inspect. It is not modified.

    Returns:
        None. The figure is displayed with plt.show().
    """
    plt.figure(figsize=(12, 8))

    # Boolean DataFrame: True where a value is missing (NaN)
    missing = df.isnull()

    xs = []
    ys = []
    for col_idx, col_name in enumerate(df.columns):
        # Row positions of the missing values in this column
        rows = np.where(missing[col_name])[0]
        xs.extend(rows)
        ys.extend([col_idx] * len(rows))

    # A single scatter call, so every tick gets the same default color
    # (one call per column would cycle through the color palette)
    plt.scatter(xs, ys, marker='|')

    # Label each height with its column name
    plt.yticks(range(len(df.columns)), df.columns)

    plt.title("Missingness Plot")

    plt.tight_layout()
    plt.show()
