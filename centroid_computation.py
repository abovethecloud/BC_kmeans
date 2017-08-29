import numpy as np


def comp_centroid(X, assign, klass):
    centroid = np.mean([X[np.where(assign == klass)]], axis=1)[0]
    return centroid