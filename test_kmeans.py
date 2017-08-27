"""Application of k-means algorithm to the Breast Cancer Wisconsin (Diagnostic) Data Set"""
from collections import Counter

import numpy as np

import kmeans as km
from view import show_centroids as sc
from IO import data_import as di

"""PRELIMINARY"""
# Import of data and set the number of classes
X = di.import_data("wdbc.data")
K = 2

"""MASK"""
# The mask decides the parameters to take into account.
# The following are the possible masks to use
mask_all = range(2, 32)  # Takes all the parameters (excludes only ID and DIAGNOSIS)
mask_conc_points = [9, 29]  # Takes only mean and worst measurement for the number of concavity points.
                            # Best 2-class prediction found yet.

mask = mask_conc_points  # Change this parameter to assign one of the available masks
Y = X[:, mask]  # Application of the mask.

"""K_MEANS"""
result = km.k_means(Y, K)

assign = result[0]  # Resulting assignment
number_iter = result[1]  # Number of iteration of the K-MEANS algorithm
centroids = result[2]  # The resulting centroids

n_obs_class = Counter(assign)  # Counts the number of occurrences for each class

"""PRINT OUTPUT

Always print the number of iterations;
Always print the number of observation for each class;
If the classes are 2, it is assumed that the classification should be similar to Benign/Malignant and therefore the 
number of "correct classifications" is printed;
If the number of classes is greater than 2 then the array containing the assigned class for each observation is printed.
"""
print "number of iterations:\t"+number_iter.__str__()
print "number of observation per class:\n\t"+n_obs_class.__str__()

if K == 2:
    count = np.sum(assign == X[:, 1])
    n = (count if count >= len(X)-count else len(X)-count)
    print "number of correct classifications:\t"+n.__str__()
    print "proportion:\t"+(n.astype('float')/len(X)).__str__()
else:
    print assign

if len(mask) == 2:
    sc.show(Y, assign, centroids)
