from sinopy import segments
from lingpy import *
from lingrex import *


wl = Wordlist('D_Chen_partial.tsv')

wl.add_entries('structure', 'tokens', lambda x: list(segments.get_structure(x)))

# print out for inspection
for idx, cp, tok, structure in wl.iter_rows('concept', 'tokens', 'structure'):
    print(wl[idx, 'doculect'], cp, tok, structure)

# alignment

# output

wl.output('tsv', filename='D_Chen_structure', ignore=[], prettify=False)
