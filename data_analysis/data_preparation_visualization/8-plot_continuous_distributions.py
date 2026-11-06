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
    # Default to all numeric columns
    if columns_to_plot is None:
        columns_to_plot = df.select_dtypes(
            include=[np.number]
        ).columns.tolist()

    # One row per feature (the variable is named n_cols but counts features)
    n_cols = len(columns_to_plot)

    # Nothing to plot
    if n_cols == 0:
        return None

    fig, axes = plt.subplots(n_cols, 2, figsize=(15, 2.5 * n_cols))

    # With a single row subplots returns a 1D array; make it 2D so the
    # axes[i, j] indexing below works
    if n_cols == 1:
        axes = axes.reshape(1, -1)

    for i, column in enumerate(columns_to_plot):
        # Drop missing values, which histogram/KDE/boxplot cannot handle
        data = df[column].dropna()

        # Histogram, normalized to density so it is comparable to the KDE
        axes[i, 0].hist(
            data,
            bins=30,
            density=True,
            alpha=0.7,
            edgecolor='black'
        )

        # KDE: smooth density estimate evaluated on 100 points over the
        # data range
        kde = stats.gaussian_kde(data)
        x = np.linspace(data.min(), data.max(), 100)

        axes[i, 0].plot(
            x,
            kde(x),
            color='red',
            linestyle='--'
        )

        axes[i, 0].set_title(f'{column} Histogram + KDE')

        # Horizontal Boxplot
        axes[i, 1].boxplot(
            data,
            vert=False
        )

        axes[i, 1].set_title(f'{column} Boxplot')

    plt.tight_layout()
    plt.savefig("Task_8.png")
    plt.show()

    return None
