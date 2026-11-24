#!/usr/bin/env python3
"""Lasso (L1 regularized) Regression model"""
from sklearn import linear_model


def lasso_regression(random_state):
    """Create an unfitted Lasso Regression model.

    Lasso adds an L1 penalty (alpha * sum of absolute coefficients) to the
    least squares loss. It can shrink the coefficients of irrelevant features
    to exactly zero, so it also performs feature selection.

    Args:
        random_state (int): seed for reproducibility. It is only used when
            the coordinate descent selects features randomly
            (selection='random'); the default is deterministic.

    Returns:
        sklearn.linear_model.Lasso: model with the default alpha (1.0).
    """
    return linear_model.Lasso(random_state=random_state)
