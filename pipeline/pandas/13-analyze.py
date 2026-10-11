#!/usr/bin/env python3
"""
Write a function def analyze(df): that takes a pd.DataFrame and:

Computes descriptive statistics for all columns except the Timestamp column.
Returns a new pd.DataFrame containing these statistics.
"""
import pandas as pd


def analyze(df):
    """Compute statistics for all columns except Timestamp."""
    return df.drop(columns=["Timestamp"]).describe()
