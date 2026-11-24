#!/usr/bin/env python3
"""Ordinary least squares (OLS) Linear Regression model"""
from sklearn import linear_model


def Linear_Regression():
    """Create an unfitted Linear Regression model.

    The model finds the coefficients that minimize the sum of squared
    residuals. It has no regularization, so it is used as the baseline that
    Ridge and Lasso are compared against.

    Returns:
        sklearn.linear_model.LinearRegression: model with default parameters.
    """
    return linear_model.LinearRegression()
