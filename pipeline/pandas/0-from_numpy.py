#!/usr/bin/env python3
"""Write a function that creates a pd.DataFrame from a np.ndarray:"""
import pandas as pd


def from_numpy(array):
    """Create a pd.DataFrame from a np.ndarray"""
    column_names = [chr(i) for i in range(65, 65 + array.shape[1])]
    return pd.DataFrame(data=array, columns=column_names)
