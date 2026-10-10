#!/usr/bin/env python3
"""
Write a function def index(df): that takes a pd.DataFrame and:

Sets the Timestamp column as the index of the dataframe.
Returns: the modified pd.DataFrame.

"""


def index(df):
    """Set Timestamp as index"""
    return df.set_index("Timestamp")
