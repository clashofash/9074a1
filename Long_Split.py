''''
Splitting functions
a selection of ways to split a given area
using a numpy array 'd' of the CSO small area centroids
'''

def long_side(d):

    # the length from East to West is compared with South to North
    # using centroid ITM coordinates
    # the new split is across the long side
    e_max = d["Easting"].max()
    e_min = d["Easting"].min()

    e_length = e_max - e_min


    n_max = d["Northing"].max()
    n_min = d["Northing"].min()

    n_length = n_max - n_min

    # choose to cut on longer side
    if n_length > e_length:
        axis = 'Northing'
    else:
        axis = 'Easting'

    return axis

