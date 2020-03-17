# Computer-Assisted Language Comparison: State of the Art

This repository contains the python scripts of the CALC-workflow and the tutorial. The CALC-workflow was presented at Workshop: Workshop : Recent Advances in Comparative Linguistic Reconstruction (London, UK), therefore, the presentation slides can be found in the **workshop> slides** folder.

## Data

You can find data in the **workflow** folder.

| File |Stage  |
| ------:|:-----|
|`D_Chen_subset.tsv` |Raw data to machine readable data|
|`D_Chen_partial.tsv`|Machine readable data to partial cognate|
|`D_Chen_structure.tsv`|Partial cognate to template-based alignment|
|`D_Chen_crossids.tsv`|Template-based alignment to strict cognates|
|`D_Chen_patterns.tsv`|Strict cognates to Sound correspondence pattern|

| File |Supplementary |
| ------:|:-----|
|`D_Doculects.tsv`|The metadata of the selected languages|
|`profile2.tsv`|An example of orthography profile for the template-based alignment|


## Python codes

You can find all the python scripts in the **workflow** folder.

| Python script | Functions |Manuscript|
| -------------:|:----------|:----------|
| `1_lifting.py`|From raw data to tokenized data| 3.2.1 |
| `2_partial.py`|From tokenized data to cognate sets| 3.2.2|
| `3_alignment.py`|From cognate sets to alignments| 3.2.3 |
| `4_crosssemantic.py`|From alignments to cross-semantic cognates| 3.2.4|
| `5_correspondence.py`|From ross-semantic cognates to sound correspondence patterns| 3.2.5|
| `P_validate.py` | The python script to generate a distance matrix |Discussion|

## Handout

You can find `handout.pdf` in the **workshop > handout** folder.

## Presentation slides

The presenation slide is in HTML format, please find `slides.html` in the **workshop > slides** folder.

## Interactive web-based application

- Profile : http://calc.digling.org/profile/
- EDICTOR : http://edictor.digling.org/
