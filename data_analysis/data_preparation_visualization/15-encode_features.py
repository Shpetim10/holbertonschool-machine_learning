#!/usr/bin/env python3
"""Module that encodes the features of a DataFrame for modeling."""
import pandas as pd
from sklearn import preprocessing


def encode_features(df):
    """Encode the target and the categorical features for modeling.

    - Churn: LabelEncoder (No -> 0, Yes -> 1).
    - Partner, Dependents, PaperlessBilling, SeniorCitizen: OrdinalEncoder
      (No -> 0, Yes -> 1).
    - Contract, PaymentMethod: one-hot encoding, dropping the first level.
    - TenureGroup: OrdinalEncoder with categories in alphabetical order.

    Args:
        df (pandas.DataFrame): data to encode. It is not modified.

    Returns:
        tuple: (encoded DataFrame, fitted LabelEncoder for Churn, fitted
        OrdinalEncoder for the binary columns, fitted OrdinalEncoder for
        TenureGroup). The binary encoder has one ['No', 'Yes'] category list
        and is refit on each column in turn.
    """
    binary_cols = ["Partner", "Dependents", "PaperlessBilling",
                   "SeniorCitizen"]
    df_enc = df.copy()

    churn_le = preprocessing.LabelEncoder()
    df_enc["Churn"] = churn_le.fit_transform(df_enc["Churn"])

    binary_oe = preprocessing.OrdinalEncoder(categories=[["No", "Yes"]])
    for col in binary_cols:
        df_enc[[col]] = binary_oe.fit_transform(df_enc[[col]]).astype(int)

    tenure_oe = preprocessing.OrdinalEncoder()
    df_enc[["TenureGroup"]] = tenure_oe.fit_transform(
        df_enc[["TenureGroup"]].astype(str)).astype(int)

    df_enc = pd.get_dummies(
        df_enc, columns=["Contract", "PaymentMethod"],
        drop_first=True, dtype=int)

    return df_enc, churn_le, binary_oe, tenure_oe
