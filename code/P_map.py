import csv
import cartopy.feature
import cartopy.io.shapereader
from cartopy.feature import *
import cartopy.feature as cfeature
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import shapely.geometry as sgeom

# read in coordinates.
target = {}
with open('10_language_geo.tsv', 'r') as csvfile:
    temp = csv.DictReader(csvfile, delimiter = '\t')
    for row in temp:
        target[row['Language']]=[row['Lat'], row['Lon']]

# cartopy background setup
ax = plt.axes(projection=ccrs.PlateCarree())
ax.set_extent([90,115,15,30], ccrs.PlateCarree())
ax.stock_img()
land_10m =cfeature.NaturalEarthFeature('phyical',
        'land', '10m')
ax.add_feature(land_10m, edgecoclor='grey')
#ax.add_feature(cartopy.feature.BORDERS, color = 'black')
for key, value in target.items():
    if value[0] !='':
        ax.plot(float(value[1]), float(value[0]), marker='o',
                markerfacecolor='black', markeredgecolor='None')
