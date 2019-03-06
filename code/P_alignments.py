from lingpy import *
from lingpy.compare.partial import Partial

part = Partial('Chen_subset.tsv')

part.get_scorer(runs=9999)

part.add_entries('tokens','segments', lambda x: x[:-1])

part.partial_cluster('lexstat', threshold=0.55, cluster_method='infomap', ref='partial_cog')

part.output('tsv', filename='test', prettify=False)
#alms = Alignments(part, ref = 'concept_name')
