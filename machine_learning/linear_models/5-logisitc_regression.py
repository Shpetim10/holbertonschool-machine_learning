#!/usr/bin/env python3
"""Logistic Regression classification model"""
from sklearn import linear_model


def Logistic_Regression_Model(random_state):
    """Create an unfitted Logistic Regression classifier.

    Despite its name it is a classifier: it passes a linear combination of
    the features through the sigmoid (softmax for several classes) to get
    class probabilities. Its decision boundary is linear, so it cannot
    separate classes that are not linearly separable.

    Args:
        random_state (int): seed for reproducibility (only used by the
            'sag', 'saga' and 'liblinear' solvers).

    Returns:
        sklearn.linear_model.LogisticRegression: model with default
            parameters (L2 penalty, C=1.0).
    """
    return linear_model.LogisticRegression(random_state=random_state)
