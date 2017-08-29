"""K-Means Clustering in Python 2.7"""
import numpy as np
import distance as dist
import centroid_computation as cen


def k_means(X, K, maxIterN=1000, d_type ="euclidian", c_type ="mean"):
    """Given X a ndarray (requires numpy) containing the n-dim observations and K the number of classes, performs
    k-means algorithm with random initialization and returns an array with first element the chosen class for each
    observation (array with same length of X), second element the number of iterations, third element the centroids.
    """
    # Random choice of centroids
    random_indexes = np.random.choice(len(X), K)  # K random indexes of X
    centroids = X[random_indexes]  # Without ID and classification

    # Assignment and update cycle
    squared_distances = np.zeros(K)
    assign = np.zeros(len(X))
    previous_assign = np.copy(assign)
    for n in range(maxIterN):
        for i in range(len(X)):
            for k in range(K):
                # Compute the distance of each point from the centroids
                #squared_distances[k] = (np.linalg.norm(X[i] - centroids[k]))**2
                squared_distances[k] = dist.compute_distance(X[i], centroids[k], d_type)
            assign[i] = np.argmin(squared_distances)
        for k in range(K):
#            mean = np.mean([X[np.where(assign == k)]], axis=1)[0]
            centroids[k] = cen.comp_centroid(X, assign, k, c_type)
        if np.array_equal(assign, previous_assign):
            break
        previous_assign = np.copy(assign)

    return [assign, n+1, centroids]
