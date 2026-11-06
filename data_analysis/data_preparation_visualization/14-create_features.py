#!/usr/bin/env python3
"""Module that engineers NumServices and TenureGroup features."""
import pandas as pd


def create_features(df):
    """Create the NumServices and TenureGroup features.

    NumServices counts the subscribed services of each customer: 'Yes' in
    MultipleLines, OnlineSecurity, OnlineBackup, DeviceProtection,
    TechSupport, StreamingTV and StreamingMovies, plus one if
    InternetService is 'DSL' or 'Fiber optic'. PhoneService is not used.

    TenureGroup bins tenure into 0-12, 13-24, 25-48, 49-60 and 60+ months
    (0 excluded, upper bounds inclusive).

    The columns used to build the new features are dropped.

    Args:
        df (pandas.DataFrame): data with the service columns and tenure.
            It is not modified.

    Returns:
        pandas.DataFrame: a new DataFrame with NumServices and TenureGroup
        added and the source columns removed.
    """
    yes_no_services = [
        "MultipleLines", "OnlineSecurity", "OnlineBackup",
        "DeviceProtection", "TechSupport", "StreamingTV", "StreamingMovies",
    ]
    internet = df["InternetService"].isin(["DSL", "Fiber optic"])

    result = df.copy()
    result["NumServices"] = (
        (df[yes_no_services] == "Yes").sum(axis=1) + internet.astype(int))
    result["TenureGroup"] = pd.cut(
        df["tenure"],
        bins=[0, 12, 24, 48, 60, float("inf")],
        labels=["0-12", "13-24", "25-48", "49-60", "60+"],
    )

    return result.drop(columns=yes_no_services + ["InternetService", "tenure"])
