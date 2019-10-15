from lingpy import *
from lexibase import *
from lingpy.compare.partial import Partial
from lebor import *

try:
    part = Partial('D_Chen_partial.bin.tsv')
except:
    part = Partial('D_Chen_subset.tsv', segments='tokens')
    part.get_partial_scorer(runs=10000)
    part.output('tsv', filename='D_Chen_partial.bin', ignore=[], prettify=False)
    print('save saved the scorer, load again to do more')
finally:
    part.partial_cluster(method='lexstat', threshold=0.55, ref='cogids')

part.output('tsv', filename='D_Chen_partial', prettify=False)
