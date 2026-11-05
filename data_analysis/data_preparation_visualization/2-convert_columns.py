#!/usr/bin/env python3
"""Module that fixes the data types of the Telco Customer Churn columns."""
import pandas as pd


def convert_columns(df):
    """Convert TotalCharges to numeric and SeniorCitizen to Yes/No.

    The raw TotalCharges column is read as text because some customers
    have a blank value. Converting it makes those blanks NaN, so they show
    up as missing values. SeniorCitizen is stored as 0/1 while the other
    binary columns use "Yes"/"No", so it is converted to match them.

    Args:
        df (pandas.DataFrame): the raw data, with the TotalCharges and
            SeniorCitizen columns. It is modified in place.

    Returns:
        pandas.DataFrame: the same DataFrame, with TotalCharges as float
        (unparsable values become NaN) and SeniorCitizen as "Yes"/"No".
    """
    # Converting TotalCharges to numeric; blank/invalid values become NaN
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
    # Convert SeniorCitizen from 1/0 to Yes/No
    df["SeniorCitizen"] = df["SeniorCitizen"]\
        .apply(lambda x: "Yes" if x == 1 else "No")

    return df
