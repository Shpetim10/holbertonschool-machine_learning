#!/usr/bin/env python3
"""Module that plots the distribution of the churn classes."""

import matplotlib.pyplot as plt


def plot_churn_distribution(df):
    """Plot a bar chart of how many customers churned and how many did not.

    Shows the class balance of the target variable, which matters when
    choosing evaluation metrics and deciding whether to resample.

    Args:
        df (pandas.DataFrame): data with a 'Churn' column.

    Returns:
        None
    """
    plt.figure(figsize=(12, 8))

    # Number of customers in each churn class
    churn_counts = df['Churn'].value_counts()

    # One color per class bar
    colors = ['skyblue', 'salmon']

    plt.bar(
        churn_counts.index,
        churn_counts.values,
        color=colors
    )

    plt.title('Churn Distribution')
    plt.ylabel('Count')
    # Keep the class labels horizontal
    plt.xticks(rotation=0)
    plt.show()
