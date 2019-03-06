from lingpy import *
from lingpy.compare.partial import Partial
import sinopy as sp
from sinopy import *


part = Partial('Chen_subset.tsv')

part.get_scorer(runs=9999)

part.add_entries('tokens','segments', lambda x: x)

# partial cognate
part.partial_cluster('lexstat', threshold=0.55, cluster_method='infomap',
        ref='partialcog')

# full cognate
part.cluster('lexstat', threshold=0.45, cluster_method='infomap', ref='fullcog')

part.output('tsv', filename='test', prettify=False)

# alignment now
alms = Alignments(part, ref = 'partialcog', fuzzy=True)
alms.align()
alms.output('tsv', filename='test_alignment', prettify=False)

