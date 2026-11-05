#!/usr/bin/env python3
"""Module that removes the customerID column from a DataFrame."""


def drop_customerID(df):
    """Drop the customerID column.

    customerID is a unique identifier, so it carries no information that
    helps to explain or predict churn.

    Args:
        df (pandas.DataFrame): data with a customerID column. It is not
            modified.

    Returns:
        pandas.DataFrame: a new DataFrame without the customerID column.
    """
    return df.drop(columns=["customerID"])
