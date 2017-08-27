"""2D representation of up to 3 centroids"""


import pylab
import time


def represent_2D_centroids(X, assign, centroids):
    time.sleep(0.5)
    pylab.cla()
    pylab.plot(X[assign == 0, 0], X[assign == 0, 1], '*b',
         X[assign == 1, 0], X[assign == 1, 1], '*r',
         X[assign == 2, 0], X[assign == 2, 1], '*g')
    pylab.plot(centroids[:, 0], centroids[:, 1], '*m', markersize=20)
    pylab.draw()
    pylab.ioff()
    pylab.show()
