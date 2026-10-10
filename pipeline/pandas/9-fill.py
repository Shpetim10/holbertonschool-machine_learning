#!/usr/bin/env python3
"""
Write a function def fill(df): that takes a pd.DataFrame and:

Removes the Weighted_Price column.
Fills missing values in the Close column with the previous row’s value.
Fills missing values in the High, Low, and Open columns with the corresponding
Close value in the same row.

Sets missing values in Volume_(BTC) and Volume_(Currency) to 0.
Returns: the modified pd.DataFrame.

"""


def fill(df):
    """Handle NaN columns"""
    # Drop Column Weighted Price
    df = df.drop(columns=["Weighted_Price"])
    # Fill Close with prev row value
    df["Close"] = df["Close"].ffill()
    # Fill High, Low, Open with Close column value
    for col in ["High", "Low", "Open"]:
        df[col] = df[col].fillna(df["Close"])
    # Sets missing values in Volume_(BTC) and Volume_(Currency) to 0
    df[["Volume_(BTC)", "Volume_(Currency)"]] = (
        df[["Volume_(BTC)", "Volume_(Currency)"]].fillna(0)
    )

    return df
