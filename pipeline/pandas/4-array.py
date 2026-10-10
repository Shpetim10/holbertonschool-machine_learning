#!/usr/bin/env python3
"""
Write a function def array(df):
that takes a pd.DataFrame as input and performs the following:

df is a pd.DataFrame containing columns named High and Close.
The function should select the last 10 rows of the High and Close columns.
Convert these selected values into a numpy.ndarray.
Returns: the numpy.ndarray
"""


def array(df):
    """Creates a numpy.ndarray from a dataframe"""
    data_to_return = df.iloc[-10:][["High", "Close"]]
    return data_to_return.to_numpy()
