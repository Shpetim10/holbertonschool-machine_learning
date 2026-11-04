#!/usr/bin/env python3
"""
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


def plot_continuous_distributions(df, columns_to_plot=None):
    """
    """
    if columns_to_plot is None:
        # your code here

    n_cols = # your code here
    fig, axes = plt.subplots(n_cols, 2, figsize=(10, 3*n_cols))

    if n_cols == 1:
        axes = axes.reshape(1, -1)

    # your code here

    plt.tight_layout()
    plt.savefig("Task_8.png")
    plt.show()
