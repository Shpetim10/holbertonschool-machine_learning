#!/usr/bin/env python3
"""
Module that plots a correlation heatmap of continuous numeric features
"""
import seaborn as sns
import matplotlib.pyplot as plt


def plot_correlation_heatmap(df):
    """
    Visualizes the pairwise correlations between the continuous
    numeric features of a DataFrame as an annotated heatmap.

    Args:
        df: pandas DataFrame

    Returns:
        None
    """
    plt.figure(figsize=(6, 5))

    # Keep numeric columns, then drop binary ones since correlation is meant for continuous features
    numeric = df.select_dtypes(include='number')
    continuous = [col for col in numeric.columns
                  if numeric[col].nunique() > 2]
    # Pearson correlation matrix
    corr = numeric[continuous].corr()

    # Fix the color scale to [-1, 1] so colors are comparable across data
    sns.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    plt.title('Correlation Matrix')
    plt.show()
