from lingpy import Wordlist
from lingpy.basic import ops

# read in data
wl = Wordlist('D_Chen_crossids.tsv')
# calculate the distance via shared cognates
wl.calculate('dst', taxa='doculect', concepts='concepts', ref='crossids')
# output
wl.output('dst', filename='D_Chen_distance')
