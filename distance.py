import numpy as np
import scipy.spatial.distance as sp


def compute_distance(X, centroid, type, weight=1):
    # Initialize the weight to all ones if not specified for weighted minkowski.
    if type is "wminkowski" and weight is 1:
        weight = np.ones(len(X))

    # Computation of the distance using one of the implemented formulas
    distance = {
#        "euclidian": (np.linalg.norm(X - centroid))**2,
        "euclidian": (sp.euclidean(X, centroid)),
        "manhattan": (sp.cityblock(X, centroid)),
        "wminkowski": (sp.wminkowski(X, centroid, 2, weight))

    }[type]
    return distance