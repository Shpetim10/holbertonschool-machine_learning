#!/usr/bin/env python3
"""
Write a function def rename(df):
that takes a pd.DataFrame as input and performs the following:

df is a pd.DataFrame containing a column named Timestamp.
The function should rename the Timestamp column to Datetime.
Convert the timestamp values to datetime values
Display only the Datetime and Close column
Returns: the modified pd.DataFrame
"""
import pandas as pd


def rename(df):
    """
    Rename column Timestamp to Datetime, convert timestamp value to datetime
    and return datetime and close columns
    """
    df["Timestamp"] = pd.to_datetime(df["Timestamp"], unit="s")
    df = df.rename(columns={"Timestamp": "Datetime"})
    return df[["Datetime", "Close"]]
