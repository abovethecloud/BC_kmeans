r"""2D representation of up to 4 centroids. Requires pylab.
Also, should problems arise with the module, see
<<https://stackoverflow.com/questions/27630114/matplotlib-issue-on-os-x-importerror-cannot-import-name-thread>>
"""


import pylab


def represent_2D_centroids(X, assign, centroids):
    pylab.cla()
    # The following functions print up to 4 centroids with their respective assigned observations
    pylab.plot(X[assign == 0, 0], X[assign == 0, 1], '*b',
         X[assign == 1, 0], X[assign == 1, 1], '*r',
         X[assign == 2, 0], X[assign == 2, 1], '*g', X[assign == 3, 0], X[assign == 3, 1], '*y')
    pylab.plot(centroids[:, 0], centroids[:, 1], '*m', markersize=20)
    pylab.draw()
    pylab.ioff()
    pylab.show()
