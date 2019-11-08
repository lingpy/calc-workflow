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
from matplotlib.legend import Legend
from matplotlib.legend_handler import HandlerPatch
import matplotlib.patches as mpatches
from collections import OrderedDict

# read in coordinates.
target = {}
with open('D_target_languages.tsv', 'r') as csvfile:
    temp = csv.DictReader(csvfile, delimiter = '\t')
    i = 1
    for row in temp:
        target[i]=[row['Name'], row['Latitude'], row['Longitude']]
        i = i+1

# set up background
plt.figure(figsize=(20,10))
ax = plt.axes(projection=ccrs.PlateCarree())
ax.set_extent([80,130,14,35], ccrs.PlateCarree())
ax.add_feature(cfeature.LAKES.with_scale('50m'))
ax.add_feature(cfeature.LAND.with_scale('50m'))
ax.add_feature(cfeature.OCEAN.with_scale('50m'))
ax.add_feature(cfeature.BORDERS, linestyle=':')
ax.add_feature(cfeature.RIVERS.with_scale('50m'))

for key, value in target.items():
      if value[1] !='':
          if 'Min' not in value[0]:
              ax.plot(float(value[2]), float(value[1]), marker='o',
                      markerfacecolor='#f6916c', markeredgecolor='None', transform=ccrs.Geodetic())
          else:
             ax.plot(float(value[2]), float(value[1]), marker='o',
                     markerfacecolor='#b95d3b', markeredgecolor='None', transform=ccrs.Geodetic())
#     #     ax.text(float(value[1]), float(value[0]), key, verticalalignment='center', horizontalalignment='right',
#     #          transform=text_transform, bbox=dict(facecolor='sandybrown', alpha=0.5, boxstyle='round'))
#
plt.savefig('Image/map-paper-bottom.svg')
# plt.savefig('Image/map-paper-bottom.png')

# set up the background of an overlay picture

fig = plt.figure(figsize=(14,6))
#plt, ax = plt.subplots(nrows =1, ncols =2,
#       subplot_kw={'projection':ccrs.PlateCarree()})
ax = fig.add_subplot(1,1,1, projection=ccrs.PlateCarree())
#ax = plt.axes(projection=ccrs.PlateCarree())
ax.set_extent([105,113,23,29], ccrs.PlateCarree())
ax.add_feature(cfeature.LAKES.with_scale('50m'))
ax.add_feature(cfeature.LAND.with_scale('50m'))
ax.add_feature(cfeature.OCEAN.with_scale('50m'))
ax.add_feature(cfeature.BORDERS, linestyle=':')
ax.add_feature(cfeature.RIVERS.with_scale('50m'))

for key, value in target.items():
     if value[1] !='':
         if 'Min' not in value[0]:
             ax.plot(float(value[2]), float(value[1]), marker='o',ms=10,
                      markerfacecolor='#f6916c', markeredgecolor='#f6916c')
             ax.text(float(value[2]), float(value[1]), key, verticalalignment='center', horizontalalignment='right')
         else:
             ax.plot(float(value[2]), float(value[1]), marker='o',ms=10,
                     markerfacecolor='#b95d3b', markeredgecolor='#b95d3b')
             ax.text(float(value[2]), float(value[1]), key, verticalalignment='center', horizontalalignment='right')

# set up legend
patches = []
labels =[]
for key, value in target.items():
    itemlabel=' '.join([str(key), value[0]])
    if 'Min' not in value[0]:
        plot1, =plt.plot([],[],
                                marker="o",
                                ms=10,
                                color='#f6916c',
                                label=itemlabel,
                                ls="",
                                mec=None
                                )
        patches.append(plot1)
        labels.append(itemlabel)
    else:
        plot2, = plt.plot([],[],
                                marker="o",
                                ms=10,
                                color='#b95d3b',
                                label=itemlabel,
                                ls="",
                                mec=None
                                )
        patches.append(plot2)
        labels.append(itemlabel)

box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

plt.legend(handles=patches, labels=labels, bbox_to_anchor=(1, 0.5),
           loc='center left', ncol=1, facecolor="white", numpoints=1,framealpha=0.5)

plt.savefig('Image/map-paper-overlay.svg')
