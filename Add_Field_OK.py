import arcpy

# Set local variables
arcpy.AddField_management("Data/Test/SA_Cent.shp", "Bbox_ref", "TEXT", "", "", 10)
