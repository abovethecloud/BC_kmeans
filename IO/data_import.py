import numpy as np

# Import of data. Consider that for the second parameter of each element:
# 0 = Benign; 1 = Malignant
def import_data(fname):
    with open(fname, 'rb') as rawData:
        X = np.loadtxt(rawData, delimiter=",")
    return X
