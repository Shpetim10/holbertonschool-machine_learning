#!/usr/bin/env python3
"""
Write a function def from_file(filename, delimiter):
that loads data from a file as a pd.DataFrame:

filename is the file to load from
delimiter is the column separator
Returns: the loaded pd.DataFrame

"""
import pandas as pd


def from_file(filename, delimiter):
    """Reads from file and returns as dataframe"""
    return pd.read_csv(filepath_or_buffer="./"+filename, delimiter=delimiter)
