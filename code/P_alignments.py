from lingpy import *
from lingpy.compare.partial import Partial
from segments.tokenizer import Tokenizer
from lingpy import basictypes as bt
from clldutils.misc import slug


from sys import argv

if 'get-concepts' in argv:
    concepts = csv2list('burmish-concepts.tsv')
    cids = [line[-1] for line in concepts]
    cids = [l for l in cids if l]
    
    wl = Wordlist('Chen_subset.tsv')
    chen_concepts = set([x for _, x, y in wl.iter_rows('concept',
        'concept_concepticon_id') if
        y in cids])
    
    wl.output('tsv', filename='chen-sublist', 
            subset=True,
            rows={"concept": 'in '+str(chen_concepts)})

try:
    part = Partial('chen-sublist.bin.tsv', segments='segments')
    print('[i] loaded the data')
except:
    part = Partial('chen-sublist.tsv', segments='segments')
    part.get_scorer(runs=10000)
    part.output('tsv', filename='chen-sublist.bin', ignore=[])
    print('[i] saved the scorer')


# partial cognate
part.partial_cluster('lexstat', threshold=0.50, cluster_method='infomap',
        ref='cogids')
maxi = max(part.get_etymdict(ref='cogids'))+1
for idx, cogids in part.iter_rows('cogids'):
    if len(set(cogids)) != len(cogids):
        current = 0
        new_cogs = []
        for cogid in cogids:
            if current == cogid:
                new_cogs += [maxi]
                maxi += 1
            else:
                new_cogs += [cogid]
            current = cogid
        part[idx, 'cogids'] = new_cogs

part.output('tsv', filename='chen-cognates', prettify=False)
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
        if len(new_tokens) == len(structure) and len(set(structure)) == \
                len(structure) and not '�' in structure:
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
align_by_structure(wl, structure='structure', ref='cogids', segments='segments')
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

alms.output('tsv', filename='chen-crossids', prettify=False, 
        subset=True,
        cols = [c for c in alms.columns if c != 'tokens']
        )



#from lingrex.copar import *
#
#cop = CoPaR(part, ref='cogids', 
