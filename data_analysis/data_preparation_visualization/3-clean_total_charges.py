#!/usr/bin/env python3
"""Module that handles the missing values of the TotalCharges column."""


def clean_total_charges(df, method='drop'):
    """Remove or fill the missing values of TotalCharges.

    Args:
        df (pandas.DataFrame): data whose TotalCharges column is numeric
            (see convert_columns). It is not modified.
        method (str): how to deal with the missing values:
            - "drop": remove the rows with a missing TotalCharges.
            - "median": fill with the median of TotalCharges.
            - "impute": fill with MonthlyCharges * tenure, the amount
              the customer should have paid so far.
            Any other value leaves the data unchanged.

    Returns:
        pandas.DataFrame: a cleaned copy of df.
    """
    # Work on a copy so the caller's DataFrame is left untouched
    df = df.copy()

    if method == "drop":
        df = df.dropna(subset=["TotalCharges"])
    elif method == "median":
        df["TotalCharges"] = df["TotalCharges"]\
            .fillna(df["TotalCharges"].median())
    elif method == "impute":
        df["TotalCharges"] = df["TotalCharges"]\
            .fillna(df["MonthlyCharges"] * df["tenure"])

    return df
