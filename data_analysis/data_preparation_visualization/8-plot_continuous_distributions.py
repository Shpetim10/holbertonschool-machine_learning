#!/usr/bin/env python3
"""Module that plots the distributions of continuous features."""
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


def plot_continuous_distributions(df, columns_to_plot=None):
    """Plot a histogram with KDE and a boxplot for each continuous feature.

    Each feature gets one row: the left plot shows its density (histogram
    plus a kernel density estimate curve) and the right plot shows a
    horizontal boxplot to highlight spread and outliers. The figure is
    saved to Task_8.png and displayed.

    Args:
        df (pandas.DataFrame): data to visualize.
        columns_to_plot (list of str, optional): columns to plot. Defaults
            to every numeric column.

    Returns:
        None
    """
    # No columns given: use every numeric column. After cleaning,
    # SeniorCitizen is categorical, so it is not selected here
    if columns_to_plot is None:
        columns_to_plot = df.select_dtypes(include=[np.number]).columns

    # One row of subplots per feature: histogram + KDE on the left,
    # boxplot on the right (the variable counts features, not columns
    # of the grid)
    n_cols = len(columns_to_plot)
    fig, axes = plt.subplots(n_cols, 2, figsize=(10, 3*n_cols))

    # With a single row, subplots returns a 1D array; make it 2D so the
    # axes[i, j] indexing below works
    if n_cols == 1:
        axes = axes.reshape(1, -1)

    for i, col in enumerate(columns_to_plot):
        # Drop missing values, which hist, KDE and boxplot cannot handle
        data = df[col].dropna()

        # Left: histogram normalized to density so the KDE curve shares
        # its y-axis scale
        axes[i, 0].hist(data, bins=30, density=True, alpha=0.7,
                        edgecolor='black')
        # Smooth density estimate, evaluated on 200 evenly spaced points
        # between the min and max of the data
        kde = stats.gaussian_kde(data)
        x = np.linspace(data.min(), data.max(), 200)
        axes[i, 0].plot(x, kde(x), color='red', linestyle='--')
        axes[i, 0].set_title(f"{col} Histogram + KDE")

        # Right: horizontal boxplot showing median, quartiles and outliers
        axes[i, 1].boxplot(data, vert=False)
        axes[i, 1].set_title(f"{col} Boxplot")

    # Prevent titles and labels of neighboring subplots from overlapping
    plt.tight_layout()
    # Save a copy of the figure, then display it
    plt.savefig("Task_8.png")
    plt.show()
