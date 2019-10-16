from sinopy import segments
from lingpy import *
from align import align_to_template
#from lingrex.util import align_by_structure


wl=Wordlist('D_Chen_partial.tsv')
wl.add_entries('structure', 'tokens', lambda x: list(segments.get_structure(x)))
template_alignment(wl,
                   ref='cogids',
                   template='imnct_imnct_imnct',
                   structure = 'structure',
                   fuzzy=False,
                   segments='tokens')



wl.output('tsv', filename='D_Chen_structure', ignore=[], prettify=False)


# print out for inspection
#for idx, cp, tok, structure in wl.iter_rows('concept', 'tokens', 'structure'):
#    print(wl[idx, 'doculect'], cp, tok, structure)
