import arcpy

# For each field in the SA_cent feature class, print
#  the field name, type, and length.
fields = arcpy.ListFields("Data/Test/SA_Cent.shp")

for field in fields:
    print("{0}, {1}, {2}"
          .format(field.name, field.type, field.length))