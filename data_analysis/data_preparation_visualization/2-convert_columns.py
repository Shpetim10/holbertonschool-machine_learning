#!/usr/bin/env python3
""""""
import pandas as pd


def convert_columns(df):
    """"""
    # Converting TotalCharges to numeric
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
    # Convert SeniorCitizen to Yes/No
    df["SeniorCitizen"] = df["SeniorCitizen"]\
        .apply(lambda x: "Yes" if x == 1 else "No")

    return df
