#!/usr/bin/env python3
"""Module that splits a DataFrame into stratified train and test sets."""
from sklearn import model_selection


def split_data(df, target='Churn', test_size=0.2, random_state=42):
    """Split data into train and test sets, stratified on the target.

    Args:
        df (pandas.DataFrame): data containing the target column.
        target (str): name of the target column.
        test_size (float): proportion of the data used for the test set.
        random_state (int): random seed for a reproducible split.

    Returns:
        tuple: (X_train, X_test, y_train, y_test), where the class
        distribution of the target is preserved in both splits.
    """
    X = df.drop(columns=[target])
    y = df[target]

    return model_selection.train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y)
