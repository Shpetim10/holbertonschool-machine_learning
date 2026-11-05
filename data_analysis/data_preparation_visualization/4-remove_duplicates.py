#!/usr/bin/env python3
"""Module that removes duplicated rows from a DataFrame."""


def remove_duplicates(df):
    """Remove the duplicated rows of a DataFrame.

    A row is a duplicate when all its values equal those of an earlier row;
    only the first occurrence is kept.

    Args:
        df (pandas.DataFrame): the data to deduplicate. It is not modified.

    Returns:
        pandas.DataFrame: a new DataFrame without duplicated rows.
    """
    return df.drop_duplicates()
