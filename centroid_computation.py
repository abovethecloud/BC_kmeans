import numpy as np


def comp_centroid(X, assign, klass, centroid_type):

    centroid = {
        "mean": np.mean([X[np.where(assign == klass)]], axis=1)[0],
        "median": np.median([X[np.where(assign == klass)]], axis=1)[0]
    }[centroid_type]

    return centroid