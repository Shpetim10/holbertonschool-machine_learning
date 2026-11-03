#!/usr/bin/env python3
"""Module that plots the churn rate per category of a column"""
import matplotlib.pyplot as plt


def plot_categorical_vs_churn(df, col):
    """
    Visualizes the churn rate (proportion of 'Yes') per category of col

    Args:
        df: pandas DataFrame containing a Churn column
        col: name of the categorical column

    Returns:
        None
    """
    churn_rate = df.groupby(col)['Churn'].apply(lambda x: (x == 'Yes').mean())

    plt.figure(figsize=(12, 8))
    churn_rate.plot(kind='bar')
    plt.title("Churn Rate by {}".format(col))
    plt.ylabel("Churn Rate")
    plt.xticks(rotation=45)
    plt.show()
