# Computer-Assisted Language Comparison: State of the Art

This repository contains the data, the python scripts, the slides and the handout for the presentation at Workshop : Recent Advances in Comparative Linguistic Reconstruction (London, UK)

## Data
You can find data in the **code** folder.
| File |Stage  |
| ------:|:-----|
|`chen-sublist.tsv` |Raw data to machine readable data|
|`chen-cognates.tsv`|Machine readable data to partial cognate|
|`chen-structure-aligned.tsv`|Partial cognate to template-based alignment|
|`chen-crossids.tsv`|Template-based alignment to strict cognates|
|`chen-patterns.tsv`|Strict cognates to Sound correspondence pattern|
|`profile2.tsv`|Orthography profile for the template-based alignment|
|10_language_geo.tsv|Geographic locations of the 10 HM languages|

## Python codes
You can find all the python scripts in the **code** folder.
| Python script | Functions |
| -------------:|:----------|
| `to_wordlist.py`|Extract 10 Hmong-Mien languages from raw data |
| `P_alignments.py`|<ul><li>Partial cognate detection</li><li> Template-based alignments</li><li> cross-semantic cognate detection</li> </ul>|
| `corrpat.py`|Summarise sound patterns|
|P_map.py | The python script to generate map |
## Handout
You can find `handout.pdf` in the **handout** folder.

## Presentation slides
The presenation slide is in HTML format, please find `slides.html` in the **slides** folder.

## Interactive web-based application
- Profile : http://calc.digling.org/profile/
- EDICTOR : http://edictor.digling.org/
