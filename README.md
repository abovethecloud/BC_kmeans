# BC_kmeans
Python application of the K-Means algorithm to the classification of cancer masses performed on the [Breast Cancer Wisconsin (Diagnostic) Data Set](https://www.kaggle.com/uciml/breast-cancer-wisconsin-data)

### A simple abstract
The goal of this work is to classify data concerning breast cancer masses by using the K-means approach. We will describe the algorithm from a theoretical point of view, considering both the original method and the heuristic algorithm used to implement it, briefly speak about the data and then apply the algorithm to the real clusterization problem. We will also show a couple of possible interesting variations of the classical method and we will implement some of them.
The essay is the file named *Murtinu-Peroni.pdf*.

### A simple description of the structure of the project
The python project is quite simple and versatile, and is structured in 3 modules:
* IO: Contains the function that reads the data as input
* view: contains the function that visualizes a graph of the observations, their classification and the centroids if the observations are 2D (if only 2 of the 30 columns have been selected - we will see it is not unreasonable to do so with a specific classification aim)
* model: constitutes the kernel of the project, the functions that compute the distance between observations and centroids, that compute the centroids for each class and of cours the function that computes the k-means classification.

Moreover, the data are stored in the 'data' folder and the python file to run to apply the k-means algorithm to the data (and in which parameters can be changed to obtain different classifications and different outputs) is called *application_kmeans.py*

#### Requirements
The code has a dependence on NumPy and SciPy (for n-dim arrays and distance computation).
It also has a dependency on pylab for the graph visualization (as such, optional and not strictly required by the model).