#!/usr/bin/env python3
"""
"""
import matplotlib.pyplot as plt


def plot_categorical_distributions(df, columns_to_plot=None):
    """
    """
    if columns_to_plot is None:
        # your code here
    else:
        # your code here
    n_cols, n_rows = # your code here
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, 5*n_rows))

    # your code here

    plt.tight_layout()
    plt.savefig("Task_7.png")
    plt.show()
