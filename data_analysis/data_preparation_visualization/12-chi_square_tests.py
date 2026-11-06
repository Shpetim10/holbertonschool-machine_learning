#!/usr/bin/env python3
"""Chi-square independence tests between categorical features and Churn."""
import pandas as pd
from scipy import stats


def chi_square_tests(df):
    """Test independence between each categorical feature and Churn.

    Args:
        df: pandas DataFrame with a Churn column and categorical columns.

    Returns:
        dict: {feature_name: p_value} for every categorical column except
        Churn, where p_value comes from the chi-square test of independence.
    """
    categorical = df.select_dtypes(include=["object", "category"]).columns
    p_values = {}

    for feature in categorical:
        if feature == "Churn":
            continue
        contingency = pd.crosstab(df[feature], df["Churn"])
        _, p_value, _, _ = stats.chi2_contingency(contingency)
        p_values[feature] = p_value

    return p_values
