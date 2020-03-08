from lexibank_chenhmongmien import Dataset as ds
from lingpy import *
from pyconcepticon import Concepticon

conf = Concepticon('../../concepticon-data')

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
concepts = set()
for clist in [
        'Blust-2008-210', 
        'Swadesh-1952-200', 
        'Swadesh-1955-100',
        'Comrie-1977-207', 
        'Matisoff-1978-200',
        'Sagart-2019-250',
        'Liu-2007-201',
        'SoHartmann-1988-280',
        ]:
    for concept in conf.conceptlists[clist].concepts.values():
            if concept.concepticon_id:
                concepts.add(concept.concepticon_id)


wl.output('tsv', filename='D_Chen_subset', prettify=False,
          subset=True, 
          rows=dict(
              doculect='in '+str(languages),
              concepticon='in '+str(list(concepts))
              )
          )

# revise columns commend
wl = Wordlist('D_Chen_subset.tsv')
print('Wordlist has {0} concepts and {1} varieties across {2} words.'.format(
      wl.height, wl.width, len(wl)))
print(wl.doculect)
