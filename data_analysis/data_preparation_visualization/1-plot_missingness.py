#!/usr/bin/env python3
""""""
import matplotlib.pyplot as plt
import numpy as np


def plot_missingness(df):
    """"""
    plt.figure(figsize=(12, 8))

    missing = df.isnull()

    for col_idx, col_name in enumerate(df.columns):
        rows = np.where(missing[col_name])[0]
        plt.scatter(rows, [col_idx] * len(rows), marker='|')

    plt.yticks(range(len(df.columns)), df.columns)

    plt.tight_layout()
    plt.show()
