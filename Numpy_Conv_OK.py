''''
Function to create centroids of CSO small areas boundaries
and store locally as a Numpy array with required fields
'''
import numpy as np
import arcpy
def SA_cents_to_Array():
    fc = 'Data/Test/SA_Cent.shp'
    a = arcpy.da.FeatureClassToNumPyArray(fc, ["OBJECTID", "Easting", "Northing", "Total2011", "Bbox_ref"])
    np.save('Data/Centroids.npy', a)


