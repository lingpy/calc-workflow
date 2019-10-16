from lexibank_chenhmongmien import Dataset as ds
from lingpy import *
from pyconcepticon import Concepticon

wl = Wordlist.from_cldf(
        ds().dir.joinpath('cldf', 'cldf-metadata.json'),
        )

# languages
languages = [
        "EasternLuobuohe",
        "WesternLuobuohe",
        "Chuanqiandian",
        "CentralGuizhouChuanqiandian",
        "WesternXiangxi",
        "EasternXiangxi",
        "Bana",
        "Younuo",
        "Numao",
        "EasternBahen",
        "WesternBaheng",
        "EasternQiandong",
        "WesternQiandong",
        "BiaoMin",
        "ZaoMin"]  # modify

# concepts
api = Concepticon('./calcworkflow/concepticon-data/')
abvd2008, chen2012 = {}, []

for key, values in api.conceptlists['Blust-2008-210'].concepts.items():
    abvd2008[values.concepticon_id] = values.concepticon_gloss

for key, values in api.conceptlists['Chen-2012-888'].concepts.items():
    if values.concepticon_gloss in abvd2008.values():
        chen2012.append(values.gloss)

wl.output('tsv', filename='D_Chen_subset', prettify=False,
          subset=True, rows=dict(doculect='in '+str(languages)),
          columns=dict(concept='in '+str(chen2012)))

# revise columns commend
wl = Wordlist('D_Chen_subset.tsv')
print('Wordlist has {0} concepts and {1} varieties across {2} words.'.format(
      wl.height, wl.width, len(wl)))
print(wl.doculect)
