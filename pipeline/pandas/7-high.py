#!/usr/bin/env python3
"""
Write a function def high(df): that takes a pd.DataFrame and:

Sorts it by the High price in descending order.
Returns: the sorted pd.DataFrame.
"""


def high(df):
    """Sorts the df descending by High column"""
    return df.sort_values(by="High", ascending=False)
