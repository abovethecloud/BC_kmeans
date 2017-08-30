"""Module that computes the centroid of the observations passed as parameter"""
import numpy as np


def comp_centroid(X, assign, klass, centroid_type):
    """Computes and returns the centroid of observations assigned to a specific classed, passed as parameter.
    The centroid can be computed both as mean or median, which are both useful for different types of data sets."""
    centroid = {
        "mean": np.mean([X[np.where(assign == klass)]], axis=1)[0],
        "median": np.median([X[np.where(assign == klass)]], axis=1)[0]
    }[centroid_type]

    return centroid