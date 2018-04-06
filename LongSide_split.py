import numpy as np


def longside():
    d = np.load('Data/Centroids.npy')
    # Find longest side of bounding box by subtracting min from max on each side

    # Find extremes of Bbox in y axis
    e_max = d["Easting"].max()
    e_min = d["Easting"].min()

    # Find extremes of Bbox in y axis
    n_max = d["Northing"].max()
    n_min = d["Northing"].min()

    # choose  split through centroid on the longer side.

    if (e_max - e_min) > (n_max - n_min):
        axis = 'Easting'
    else:
        axis = 'Northing'

    return axis

print(longside())