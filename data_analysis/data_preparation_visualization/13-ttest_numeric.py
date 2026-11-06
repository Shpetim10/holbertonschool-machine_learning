#!/usr/bin/env python3
"""Welch's t-tests between Churn=Yes and Churn=No for numeric features."""
from scipy import stats


def ttest_numeric(df):
    """Compare numeric feature means between churned and retained customers.

    H0: the means are equal in the Churn=Yes and Churn=No groups.
    H1: the means differ significantly.

    Args:
        df: pandas DataFrame with a Churn column ("Yes"/"No").

    Returns:
        dict: {feature_name: p_value} from Welch's t-test for every numeric
        column except Churn.
    """
    churned = df[df["Churn"] == "Yes"]
    retained = df[df["Churn"] == "No"]
    p_values = {}

    for feature in df.select_dtypes(include="number").columns:
        if feature == "Churn":
            continue
        _, p_value = stats.ttest_ind(
            churned[feature], retained[feature],
            equal_var=False, nan_policy="omit")
        p_values[feature] = float(p_value)

    return p_values
