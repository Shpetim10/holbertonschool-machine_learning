#!/usr/bin/env python3
"""Module that plots the distributions of categorical features."""
import matplotlib.pyplot as plt


def plot_categorical_distributions(df, columns_to_plot=None):
    """Plot a bar chart of value counts for each categorical feature.

    The charts are laid out in a grid of 3 columns, saved to Task_7.png
    and displayed.

    Args:
        df (pandas.DataFrame): data to visualize.
        columns_to_plot (list of str, optional): columns to plot. Defaults
            to every object-dtype column except 'Churn'.

    Returns:
        None
    """
    # Default to all categorical (object) columns, excluding the target
    if columns_to_plot is None:
        columns_to_plot = [
            col for col in df.select_dtypes(include=['object']).columns
            if col != 'Churn'
        ]

    # Grid size: 3 plots per row, enough rows to fit every column
    # (ceiling division)
    n_cols = 3
    n_rows = (len(columns_to_plot) + n_cols - 1) // n_cols

    # Nothing to plot
    if not columns_to_plot:
        return None

    fig, axes = plt.subplots(
        n_rows, n_cols,
        figsize=(15, 5 * n_rows)
    )

    for i, column in enumerate(columns_to_plot):
        # axes is a 2D array of subplots; flatten it to index with i
        ax = axes.flat[i] if hasattr(axes, 'flat') else axes

        counts = df[column].value_counts()

        ax.bar(counts.index, counts.values)
        ax.set_title(column)
        ax.set_xlabel(column)
        ax.set_ylabel('Count')
        # Rotate labels so long category names do not overlap
        ax.tick_params(axis='x', rotation=45)

    # Hide unused subplots
    for i in range(len(columns_to_plot), len(fig.axes)):
        fig.axes[i].set_visible(False)

    plt.tight_layout()
    plt.savefig("Task_7.png")
    plt.show()

    return None
