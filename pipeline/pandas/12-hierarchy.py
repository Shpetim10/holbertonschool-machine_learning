#!/usr/bin/env python3
"""
Based on 11-concat.py, write a function def hierarchy(df1, df2):
that takes two pd.DataFrame objects and:

Rearranges the MultiIndex so that Timestamp is the first level.
Concatenates the bitstamp and coinbase tables
from timestamps 1417411980 to 1417417980, inclusive.

Adds keys to the data, labeling rows from df2 as bitstamp
and rows from df1 as coinbase.

Ensures the data is displayed in chronological order.
You should use index = __import__('10-index').index.
Returns: the concatenated pd.DataFrame.
"""
import pandas as pd


index = __import__('10-index').index


def hierarchy(df1, df2):
    """Concatenate selected rows and arrange the index hierarchically."""
    # Set index
    df1 = index(df1)
    df2 = index(df2)

    # Slice
    df1 = df1.loc[1417411980:1417417980]
    df2 = df2.loc[1417411980:1417417980]

    # Concatenate
    df_concat = pd.concat(
        [df2, df1],
        keys=['bitstamp', 'coinbase']
    )

    # Swap level
    df_concat = df_concat.swaplevel(0, 1)

    return df_concat.sort_index()
