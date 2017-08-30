"""Module that computes the distance between an instance of the data and the respective centroid using numpy
and scipy"""
import numpy as np
import scipy.spatial.distance as sp


def compute_distance(X, centroid, type="euclidian", weight=1):
    """Computes the distance using the type passed as parameter. Can compute weighted distance only for minkowski."""
    # Initialize the weight to all ones if not specified for weighted minkowski.
    if type is "wminkowski" and weight is 1:
        weight = np.ones(len(X))

    # Computation of the distance using one of the implemented formulas
    distance = {
        "euclidian": (sp.euclidean(X, centroid)),
        "manhattan": (sp.cityblock(X, centroid)),
        "wminkowski": (sp.wminkowski(X, centroid, 2, weight))
    }[type]

    return distance