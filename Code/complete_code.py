import netCDF4 as net
import numpy as np

# open de NET Dataset Object

file = net.Dataset('/Users/maxiaguest/Downloads/MERRA2_400.tavg1_2d_aer_Nx.20240225.nc4')
print(file)

# Access to the information from this object
# Get the variablee names

print(file.variables.keys())

# Individually access to each variable

longitud = file.variables['lon'] 
latitude = file.variables['lat'] 
print(longitud)
print("\n" * 2)
print(latitude)

for d in file.dimensions.items():
    print(d)

longitud.dimensions

longitud.shape

var = file.variables['BCANGSTR']
print(var)
