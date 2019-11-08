from lingpy import *
from lingrex.colex import find_colexified_alignments

alms = Alignments('D_Chen_aligned.tsv', ref='cogids')

find_colexified_alignments(
        alms,
        cognates='cogids',
        segments='tokens',
        ref='crossids'
        )

alms.output('tsv', filename='D_Chen_crossids', prettify=False)
