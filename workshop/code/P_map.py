import csv
import cartopy.feature
import cartopy.io.shapereader
from cartopy.feature import *
import cartopy.feature as cfeature
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import shapely.geometry as sgeom
from cartopy.io.shapereader import Reader
import matplotlib.patheffects as PathEffects
from owslib.wmts import WebMapTileService

# shape file 
fname = '/home/wu/Documents/shapefiles_and_python_map/China/CHN_adm1.shp'


# read in coordinates.
target = {}
with open('10_language_geo.tsv', 'r') as csvfile:
    temp = csv.DictReader(csvfile, delimiter = '\t')
    for row in temp:
        target[row['Language']]=[row['Lat'], row['Lon']]



# cartopy background setup
plt, ax = plt.subplots(nrows =1, ncols =1,
       subplot_kw={'projection':ccrs.PlateCarree()}, figsize=(12,12))
#plt.figsize(12,10)
#ax = plt.axes(projection=ccrs.PlateCarree())

#ax.add_feature(cartopy.feature.OCEAN)
#ax.add_feature(cartopy.feature.BORDERS, color='grey')

ax.set_extent([104,112,24,28], ccrs.PlateCarree())
#ax.coastlines(resolution='110m')
#land_110m =cfeature.NaturalEarthFeature('physical',
#        'land', '110m',edgecolor='face',facecolor=cfeature.COLORS['land'])
#gshh = cfeature.GSHHSFeature(scale='low', levels=[1,2,3,4])
#ax.add_feature(land_110m)
#ax.add_feature(gshh)
#ax.add_feature(cfeature.LAKES, edgecolor='blue')
#ax.stock_img()
shape_feature = shapereader.Reader(fname)
for rec in shape_feature.records():
    if rec.attributes['NAME_1'] in ['Guizhou','Guangxi','Hunan']:
        ax.add_geometries([rec.geometry], ccrs.PlateCarree(), edgecolor='black',facecolor='none')
#ax.add_feature(cartopy.feature.BORDERS, color = 'black')
for key, value in target.items():
    if value[0] !='':
        ax.plot(float(value[1]), float(value[0]), marker='o',
                markerfacecolor='black', markeredgecolor='None')
        ax.annotate(key, (float(value[1]), float(value[0])))

plt.savefig('languages.svg')
