import numpy as np

#d = np.load('Data/Centroids.npy')
#bounding_box = [d]


def simple_split(a, bb_list, axys, bb1, bb2):
    '''
    Takes an existing array of centroids and splits it either
    on the North/South or East/West median, depending on 'axys' parameter.
    The new (split) arrays are appended to the array list with a referece ID 'Bbox_ref'
    '''

    axys_med = np.median(a[axys])

    ary_1 = a[a[axys] <= axys_med]    # array for centroids south or west of split axis (axys_med)
    ary_1['Bbox_ref'] = bb1             # insert new reference key for these centroids
    ary_2 = a[a[axys] > axys_med]     # array for centroids north or east of split axis (axys_med)
    ary_2['Bbox_ref'] = bb2            # insert new reference key for these centroids


    bb_list.append(ary_1)
    bb_list.append(ary_2)




