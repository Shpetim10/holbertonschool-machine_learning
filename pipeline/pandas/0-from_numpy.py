#!/usr/bin/env python3
"""Write a function that creates a pd.DataFrame from a np.ndarray:"""
import pandas as pd
from string import ascii_uppercase


def from_numpy(array):
    """Create a pd.Dataframe from a np.ndarray"""
    column_names = list(ascii_uppercase[: array.shape[1]])
    return pd.DataFrame(data=array, columns=column_names)
