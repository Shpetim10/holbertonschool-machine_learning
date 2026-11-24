#!/usr/bin/env python3
"""SHAP explanations for fitted models"""
import shap


def get_shap_explainer_and_values(model, X_train, X_test):
    """Explain a fitted model's predictions with SHAP.

    SHAP assigns each feature a contribution to every prediction, measured
    relative to the average prediction on the background data.

    Args:
        model: fitted model (here a linear model, so SHAP picks the Linear
            explainer automatically).
        X_train (array-like): background data, used to compute the baseline
            (the expected feature values).
        X_test (array-like): samples to explain.

    Returns:
        tuple: (explainer, shap_values) where shap_values is a
            shap.Explanation with one row per sample in X_test and one
            column per feature.
    """
    explainer = shap.Explainer(model, X_train)
    shap_values = explainer(X_test)
    return explainer, shap_values
