#!/usr/bin/env python3
"""Module that plots a numeric feature distribution by churn"""
import matplotlib.pyplot as plt


def plot_numeric_vs_churn(df, col):
    """
    Compares the distribution of a numeric column for Churn=Yes and
    Churn=No using overlapping histograms

    Args:
        df: pandas DataFrame containing a Churn column
        col: name of the numeric column

    Returns:
        None
    """
    plt.figure(figsize=(12, 8))
    no_churn = df[df['Churn'] == 'No'][col]
    yes_churn = df[df['Churn'] == 'Yes'][col]
    plt.hist([no_churn, yes_churn], bins=30, label=['No', 'Yes'])
    plt.title("{} Distribution by Churn".format(col))
    plt.xlabel(col)
    plt.legend(title='Churn')
    plt.show()
