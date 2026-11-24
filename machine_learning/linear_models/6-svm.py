#!/usr/bin/env python3
"""Support Vector Machine (SVM) classifiers"""
from sklearn import svm


def get_SVM_model(name, random_state):
    """Create an unfitted SVM classifier with the requested kernel.

    The kernel sets the shape of the decision boundary: 'linear' gives
    straight boundaries, 'poly' polynomial curves and 'rbf' flexible,
    smooth, local boundaries that can fit non-linear data.

    Args:
        name (str): kernel name, one of 'linear', 'poly' or 'rbf'.
        random_state (int): seed for reproducibility (only used when
            probability estimates are enabled, which is not the case here).

    Returns:
        sklearn.svm.SVC: model with the given kernel and default
            parameters, or None if name is not a supported kernel.
    """
    if name in ['linear', 'poly', 'rbf']:
        return svm.SVC(kernel=name, random_state=random_state)
