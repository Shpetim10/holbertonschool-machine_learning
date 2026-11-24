#!/usr/bin/env python3
"""Ridge (L2 regularized) Regression model"""
from sklearn import linear_model


def ridge_regression(random_state):
    """Create an unfitted Ridge Regression model.

    Ridge adds an L2 penalty (alpha * sum of squared coefficients) to the
    least squares loss. It shrinks the coefficients towards zero without
    making them exactly zero, which keeps the model stable when features are
    highly correlated (multicollinearity).

    Args:
        random_state (int): seed for reproducibility. The default solver
            ('auto') only uses it for the stochastic solvers 'sag'/'saga'.

    Returns:
        sklearn.linear_model.Ridge: model with the default alpha (1.0).
    """
    return linear_model.Ridge(random_state=random_state)
