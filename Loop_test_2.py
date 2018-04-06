import arcpy
import numpy as np
from Simple_Split_01 import simple_split
from Skew_Split import skew
from Long_Split import long_side

d = np.load('Data/Centroids.npy')   # Load array from stored Numpy file and assign to 'd'
d['Bbox_ref']= '1'                  # Assign initial Virtual bounding box value '1' - a string
bounding_box =[d]                   # Initialise python list, starting with array 'd'
list = ['1']                        # Initialise ID list 'Bbox_ref' with string '1'

for j in range(0, 7):               # We create 128 costituencies so we need to split 7 times (outer loop)
    s = 2**j -1                     # Create starting index for inner loop
    e = len(list)                   # Create ending index for inner loop
    b = len(bounding_box)

    for i in range(s, e):           # Inner loop too split the most recently created Boxes
        split_1 = list[i] + '1'     # Create a new reference IDs for next split (add either '1' or '2' to
        list.append(split_1)        # previous reference
        split_2 = list[i] + '2'
        list.append(split_2)        # Add new reference to python reference list
        simple_split(bounding_box[i], bounding_box, long_side(bounding_box[i]), split_1, split_2)



bounding_box = bounding_box[127:len(bounding_box)]  # select only the bounding boxes from the final split
newarray = bounding_box[0]                          # create a new numpy array from arrays in the bounding box list
for i in range(1, 128):
    newarray = np.append([newarray], [bounding_box[i]])

newy = newarray[["OBJECTID", "Bbox_ref"]]           # Select the join field and the reference field
arcpy.da.ExtendTable("Data/Small_Areas_ITM/SAs.shp", "OBJECTID", newy, "OBJECTID")
