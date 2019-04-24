import os.path
import re
from re import finditer

data = []
with open('chen2012miaoyao-phone_tables.txt', 'r') as f:
    temp = f.readlines()
    for row in temp:
        row = row.rstrip('\n').split('\t')
        data.append(row)

pattern = re.compile('[0-9]+\.')
key = [ i for i, line in enumerate(data) if re.match(pattern, " ".join(line))]
keyname = [data[i][0].split(' ')[1] for i in key]

# read in by language
data_dictionary ={}
for i in range(len(key)):
    if i < len(key)-1:
        start = key[i]+1
        end = key[i+1]-1
        data_dictionary[keyname[i]] = data[start:end]
    elif i ==len(key)-1:
        start = key[i]+1
        data_dictionary[keyname[i]] = data[start:]
# clean up
data_dictionary_clean={}
for dkey, dvalue in data_dictionary.items():
    temp = []
    for i in dvalue:
        temp.extend([t for t in i if t != ''])
    data_dictionary_clean[dkey]=temp

##### This section is for output orthography profiles by languages.
for filetitle, values in data_dictionary_clean.items():
    with open(os.path.join('Phoneme_Inventories',filetitle), 'w') as outfile:
        outfile.write("{0}\t{1}\t{2}\n".format('Grapheme','IPA','Template'))
        for v in values:
            outfile.write('{0}\t{1}\t{2}\n'.format(v,'',''))


#### this section is for output a summarised orthography profile ####
# get unique values
unique_phoneme =set()
for val in data_dictionary_clean.values():
    unique_phoneme.update(val)

unique_phoneme_dict ={}
for i in unique_phoneme:
    key_list=[]
    for dkey, dval in data_dictionary_clean.items():
        if i in dval:
            key_list.append(dkey)
    unique_phoneme_dict[i]=key_list

with open('summarised_orthography.tsv', 'w') as f:
    for dkey, dval in unique_phoneme_dict.items():
        f.write("{0}\t{1}\n".format(dkey,' '.join(dval)))
