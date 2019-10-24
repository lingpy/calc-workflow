import csv
import cartopy.feature
from matplotlib.transforms import offset_copy
import cartopy.io.shapereader
from cartopy.feature import *
import cartopy.feature as cfeature
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import shapely.geometry as sgeom
from cartopy.io.shapereader import Reader
import matplotlib.patheffects as PathEffects
from owslib.wmts import WebMapTileService
import cartopy.io.img_tiles as cimgt

# shape file
fname = 'shp/CHN_adm1.shp'

# read in coordinates.
target = {}
with open('D_target_languages.tsv', 'r') as csvfile:
    temp = csv.DictReader(csvfile, delimiter = '\t')
    for row in temp:
        target[row['Name']]=[row['Latitude'], row['Longitude']]

# set up background
plt.figure(figsize=(20,10))
stamen_terrain = cimgt.Stamen('terrain-background')
ax = plt.axes(projection=stamen_terrain.crs)
ax.set_extent([101,116,20,30], ccrs.PlateCarree())
ax.add_image(stamen_terrain, 8)


geodetic_transform = ccrs.Geodetic()._as_mpl_transform(ax)
text_transform = offset_copy(geodetic_transform, units='dots', x=-5)
#ax.add_feature(cartopy.feature.RIVERS, color = 'blue')
for key, value in target.items():
    if value[0] !='':
        ax.plot(float(value[1]), float(value[0]), marker='o',
                markerfacecolor='black', markeredgecolor='None', transform=ccrs.Geodetic())
        ax.text(float(value[1]), float(value[0]), key, verticalalignment='center', horizontalalignment='right',
             transform=text_transform, bbox=dict(facecolor='sandybrown', alpha=0.5, boxstyle='round'))



plt.savefig('Image/map.svg')
