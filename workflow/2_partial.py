from lingpy import *
from lexibase import *
from lingpy.compare.partial import Partial
from lebor import *

try:
    part = Partial('D_Chen_partial.bin.tsv')
except:
    part = Partial('D_Chen_subset.tsv', segments = 'tokens')
    part.get_partial_scorer(runs = 9999)
    part.output('tsv', filename= 'D_Chen_partial.bin', ignore=[],prettify = False)
    print('save saved the scorer, load again to do more')
finally:
    part.partial_cluster(method = 'lexstat', threshold = 0.55)




part.output('tsv', filename='D_Chen_partial', prettify=False)

# Should I download the data from edictor? 
# the new algorithm generate a new column "partial_cognate_sets". Should I convert this to cogid?
