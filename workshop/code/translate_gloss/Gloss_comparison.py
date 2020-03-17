import pandas as pd
from pandas import *


huang = pd.read_csv('Huang-1992-1820-full-mapping.csv', sep = '\t')
chen = pd.read_csv('concepts.tsv', sep='\t')
huang2 = pd.read_csv('Huang-1992-1820.csv', sep='\t')

huang_chinese_conceptbook = Series(huang.ENGLISH.values, index=huang.CHINESE.values).to_dict()
huang_concepticon_conceptbook = Series(huang.ENGLISH.values, index=huang.CONCEPTICON_GLOSS.values).to_dict()
huang_conceptcion_conceptbook_link_chinese =Series(huang.CHINESE.values, index=huang.CONCEPTICON_GLOSS.values).to_dict()

huang2_chinese_conceptbook = Series(huang2.STEDT_GLOSS.values, index=huang2.CHINESE.values).to_dict()


for i in range(len(chen)):
    if chen.loc[i, 'GLOSS'] in huang_chinese_conceptbook.keys():
        chen.loc[i, 'English'] = huang_chinese_conceptbook[chen.loc[i,'GLOSS']]
        chen.loc[i,'Huang_STEDT_English'] = huang2_chinese_conceptbook[chen.loc[i,'GLOSS']]
    if pd.notna(chen.loc[i, 'CONCEPTICON_GLOSS']) and chen.loc[i, 'CONCEPTICON_GLOSS'] in huang_concepticon_conceptbook.keys():
        chen.loc[i, 'English_by_concepticon'] = huang_concepticon_conceptbook[chen.loc[i, 'CONCEPTICON_GLOSS']]
        chen.loc[i, 'Huang_Chinese'] = huang_conceptcion_conceptbook_link_chinese[chen.loc[i, 'CONCEPTICON_GLOSS']]

chen.to_csv('chen_concepts_auto_translate_2.tsv', sep='\t')

# statistics
identical_count = 0
not_identical_count =0

for i in range(len(chen)):
    if chen.loc[i, 'GLOSS'] == chen.loc[i, 'Huang_Chinese']:
        identical_count +=1
    else:
        not_identical_ount +=1
