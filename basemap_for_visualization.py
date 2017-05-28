"""
Creating attractive and informative map visualization
in Python with Matplotlib Basemap module (not installed
as part of Matplotlib).

# Install basemap (if using Anaconda)

    conda install basemap

# Use shapefiles to draw areas and regions 

Shapefiles that defines the areas and regions to your interest (even roads)
may be downloadable online (e.g. US Census Bureau).

# Reference

This script is copied from 

    http://www.datadependence.com/2016/06/creating-map-visualisations-in-python/

# Note

- This script is not executable because the links to the data
    are broken. This script is for demonstrative purpose only.
"""

import matplotlib.pyplot as plt
import matplotlib.cm

from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from matplotlib.colors import Normalize


fig, ax = plt.subplots(figsize=(10,20))  # Create an empty figure with a subplot
# Create a Basemap object
# provide: resolution (c - crude) and boundary longitude & latitude
m = Basemap(resolution='c', # c, l, i, h, f or None
            projection='merc',
            lat_0=54.5, lon_0=-4.36,  # center 
            llcrnrlon=-6., llcrnrlat= 49.5,  # lower left corner
            urcrnrlon=2., urcrnrlat=55.2)  # upper right corner
# Define how the map is to be displayed and we have our basic map
m.drawmapboundary(fill_color='#46bcec')
m.fillcontinents(color='#f2f2f2',lake_color='#46bcec')
m.drawcoastlines()

# Plot data points on a Basemap
def plot_area(pos):
    count = new_areas.loc[new_areas.pos == pos]['count']
    x, y = m(pos[1], pos[0])
    size = (count/1000) ** 2 + 3
    m.plot(x, y, 'o', markersize=size, color='#444444', alpha=0.8)
    
new_areas.pos.apply(plot_area)

# Draw areas and regions using shapefiles
m.readshapefile('data/uk_postcode_bounds/Areas', 'areas')

