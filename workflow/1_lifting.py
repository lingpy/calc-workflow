from lexibank_chenhmongmien import Dataset as ds
from lingpy import *


wl = Wordlist.from_cldf(
        ds().dir.joinpath('cldf','cldf-metadata.json').as_posix(),
        col="language_id",
        row="parameter_id",
        )

wl.add_entries('doculect', 'language_name', lambda x: x)
wl.add_entries('concept', 'concept_name', lambda x: x)

languages = [
        "Luobuohe, Western",
        "Chuanqiandian",
        "Chuanqiandian, Central Guizhou",
        "Xiangxi, West",
        "Xiangxi, East",
        "Bana",
        "Younuo",
        "Numao"
        "Baheng, East",
        "Baheng, West",
        "Qiandong, East",
        "Qiandong, West",
        "Biao Min",
        "Zao Min"] # modify

#wl.add_entries('new_segments', 'segments', lambda x: x[:-1])
wl.add_entries('ipa', 'segments', lambda x: ''.join(x))

wl.output('tsv', filename='Chen_subset',
        prettify=False,
        subset=True,
        rows=dict(doculect='in '+str(languages))
        )

#for idx, doculect, concept, tokens in wl.iter_rows('doculect', 'concept',
#        'segments'):

# sinopy profile  WORDLIST --column form -o ../etc/profile2.tsv
