#!/usr/bin/env python3
"""Evaluation metrics for regression models"""
from sklearn import metrics
import numpy as np


def evaluation_metrics_for_regression(y_true, y_pred):
    """Compute the standard regression metrics for a set of predictions.

    Args:
        y_true (array-like): ground-truth target values.
        y_pred (array-like): values predicted by the model.

    Returns:
        tuple: (mse, rmse, mae, r2) where
            mse  - mean squared error, penalizes large errors the most,
            rmse - square root of mse, in the same unit as the target,
            mae  - mean absolute error, less sensitive to outliers,
            r2   - coefficient of determination, 1.0 is a perfect fit.
    """
    mse = metrics.mean_squared_error(y_true, y_pred)
    # RMSE is derived from the MSE instead of being computed a second time
    rmse = mse ** 0.5
    mae = metrics.mean_absolute_error(y_true, y_pred)
    r2 = metrics.r2_score(y_true, y_pred)
    return mse, rmse, mae, r2
