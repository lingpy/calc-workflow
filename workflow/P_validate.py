import argparse
from lingpy import Wordlist
from lingpy.basic import ops

parser = argparse.ArgumentParser()
parser.add_argument('--input')
parser.add_argument('--column')
test = "--input test --column cogids"
args = parser.parse_args()
#print(args) 
wl = Wordlist(args.input)

# calculate the distance via shared cognates
wl.calculate('dst', taxa='doculect', concepts='concepts', ref=args.column)

# output
wl.output('dst', filename='D_Chen_distance')