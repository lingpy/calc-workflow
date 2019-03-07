from lingpy import *
from lingpy.compare.partial import Partial
from segments.tokenizer import Tokenizer
from lingpy import basictypes as bt
from clldutils.misc import slug


try:
    part = Partial('Chen_subset.bin.tsv', segments='segments')
    print('[i] loaded the data')
except:
    part = Partial('Chen_subset.tsv', segments='segments')
    part.get_scorer(runs=1000)
    part.output('tsv', filename='Chen_subset.bin', ignore=[])
    print('[i] saved the scorer')


# partial cognate
#part.partial_cluster('lexstat', threshold=0.55, cluster_method='infomap',
#        ref='cogids')

#part.output('tsv', filename='chen-cognates', prettify=False)
#- 
#- # alignment now
#- alms = Alignments(part, ref = 'cogids', fuzzy=True)
#- alms.align()
#- alms.output('tsv', filename='chen-aligned', prettify=False)

# load the profile
part = Wordlist('chen-cognates.tsv')
tk = Tokenizer('profile2.tsv')
blacklist = []
D = {}
count = 0
N = {0: part.columns}
for idx, tokens in part.iter_rows('segments'):
    segmented, strucs = [], []
    bl = None
    for morpheme in bt.lists(tokens).n:
        new_string = ''.join(morpheme)
        new_tokens = bt.strings(tk('^'+new_string, column='CLPA'))
        structure = bt.strings(tk('^'+new_string, column='Structure'))
        if len(new_tokens) == len(structure) and len(set(structure)) == len(structure):
            segmented += [new_tokens]
            strucs += [structure]
        else:
            segmented += [new_tokens]
            strucs += [structure]
            bl = idx
    D[idx] = bt.lists(' + '.join([str(x) for x in strucs]))
    part[idx, 'segments'] = bt.lists(' + '.join([str(x) for x in segmented]))
    if bl:
        print(' + '.join([str(x) for x in segmented]))
        print(' + '.join([str(x) for x in strucs]))
        count += 1
    blacklist += [bl]
    if not bl:
        N[idx] = part[idx]
        N[idx][part.header['doculect']] = slug(part[idx, 'doculect'])

print('excluded {0}'.format(count))
#input()
wl = Wordlist(N)
wl.add_entries('structure', D, lambda x: x)

from lingrex.util import align_by_structure
align_by_structure(wl, structure='structure', ref='cogids')
wl.output('tsv', filename='chen-structure-aligned', prettify=False)

alms = Alignments(wl, ref='cogids')

# cross-semantic cognate detection
from lingrex.colex import find_colexified_alignments
find_colexified_alignments(
        alms, 
        cognates='cogids', 
        segments='segments',
        ref='crossids'
        )

alms.output('tsv', filename='chen-crossids', prettify=False)



#from lingrex.copar import *
#
#cop = CoPaR(part, ref='cogids', 
