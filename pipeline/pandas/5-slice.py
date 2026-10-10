#!/usr/bin/env python3
"""
Write a function def slice(df): that takes a pd.DataFrame and:

Extracts the columns High, Low, Close, and Volume_(BTC).
Selects every 60th row from these columns.
Returns: the sliced pd.DataFrame
"""


def slice(df):
    """Selects every 60th row from High, Low, Close, and Volume_(BTC) cols"""
    selected_columns = ["High", "Low", "Close", "Volume_(BTC)"]
    return df.iloc[::60][selected_columns]
