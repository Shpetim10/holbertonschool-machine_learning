#!/usr/bin/env python3
"""Module that standardizes the numeric charge columns of a DataFrame."""
from sklearn import preprocessing


def scale_numeric(df):
    """Standardize MonthlyCharges and TotalCharges (mean=0, std=1).

    Args:
        df (pandas.DataFrame): data with MonthlyCharges and TotalCharges
            columns. It is not modified.

    Returns:
        pandas.DataFrame: a copy of df where the two columns are scaled with
        StandardScaler.
    """
    columns = ["MonthlyCharges", "TotalCharges"]
    df_scaled = df.copy()

    scaler = preprocessing.StandardScaler()
    df_scaled[columns] = scaler.fit_transform(df_scaled[columns])

    return df_scaled
