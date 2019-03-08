# Workflows for Computer-Assisted Language Comparison

@data-background:#f5f5f7
@data-transition:concave
@style:text-align:justify;
@style:font-size:85%;

---
@data-background:#f5f5f7
@style:text-align:center;
@style:font-size:100%;

## <font color = '#5b687c'>State of the Art</font>
----

<p style="text-align:center;color:#7687a1;font-weight:bold;font-size:110%;">Workflows for Computer-Assisted Language Comparison</p>
<p style="text-align:center"> 
<img src="img/calc-yinyang.svg" alt="image" style="width:200px"></img>
</p>


---

## @head:"Our team"

* The ERC funded project CALC (Computer-Assisted Language Comparison)
* Our team consists of people with experience in computational topics as well as classical linguistic topics.
<p style="text-align:center">
<img src="http://calc.digling.org/img/calc-team.JPG", alt="img" style ="width:500px;textalign:center;"></img>
</p>

---
## @head:"Introduction"

<p style="text-align:center">
<img src="http://lingulist.de/documents/talks/img/edictor-tutorial/calc-7.png" alt="img" style="width:1000px;text-align:center;"></img>
Workflows for Computer-Assisted Language Comparison
</p>

--
## @head:"Introduction"
### @subhead:"What is a computer-assisted approach"

Classical approach 

* Suitable for small datasets. 
* High accuracy
* High flexibility
* Low efficiency and most of the tasks are repetitive.

Computational approach

* High consistency
* High efficiency

--
## @head:"Introduction"
### @subhead:"What is a computer-assisted approach"

A workflow involves linguistic experts and computing power.

* Analyse and manipulate linguistic datasets
* Follow a transparency guideline when handling linguistic datasets. 

--

## @head:"Introduction"
### @subhead:"The Goals"

<p style="text-align:center">
<img src="img/worktogether.jpg" alt="img" style="width:500px;text-align:center;"></img>
</p> 

---
## @head:"CALC workflows"

<p>Application: correspondence pattern detection</p> 

<p style="text-align:center">
<img src="img/calc-workflow.svg" alt="img" style="width:600px;text-align:center;"></img>
</p>

--
## @head:"CALC workflows"
### @subhead:"From raw data to machine-readable data"
|Books                                            | Web resources           |
|-------------------------------------------------|-------------------------|
|<img src="img/books.jpg" style="vertical-align:bottom;width:400px" alt="img1"></img>|<img src="img/chen_webpage.png" style="width:500px"></img>|

--
## @head:"CALC workflows"
### @subhead:"From raw data to machine-readable data"

<font color="red">+++add example on no-goes from cldf paper forkel ett al. +++</font>
<p>Wordlist format : a long format</p>

<a href='https://docs.google.com/spreadsheets/d/1ciUHTyBXOEioHLzhmNvAzpkEh1Xc0SsOPBsKCnPUpE8/edit?usp=sharing'>Demo: Wordlist format</a>


--
## @head:"CALC workflows"
### @subhead:"From raw data to machine-readable data"

<p>Profile: segmentation (tokenization) guidelines</p>
<a href="http://calc.digling.org/profile/">http://calc.digling.org/profile/</a>

<p>We recommand Sinopy profile for Sino-Tibetan and SEA languages. The profile can be modified and applied to different datasets.</p>
--
## @head:"CALC workflows"
### @subhead:"From segmented words to computer-inferred cognates"

<p align="middle"><img src="http://lingulist.de/documents/talks/img/calc-project/software-new-4.jpg" style="width:550px;align:middle;"></img></p>

--
## @head:"CALC workflows"
### @subhead:"From segmented words to computer-inferred cognates"
<p>Lingpy : a python library for *quantitative tasks* in historical linguistics</p>

* Phonetic alignment
* Computer-inferred cognates

<p>Experts can then examine as well as modfiy the cognates.</p>

--
## @head:"CALC workflows"
### @subhead:"From segmented words to computer-inferred cognates"
<p>EDICTOR: a web-based tool to edit, analyse, and publish etymological data.</p>
<a style="color:#2d1f23;text-align:center" href='http://edictor.digling.org/'>http://edictor.digling.org/</a>

--
## @head:"CALC workflows"
### @subhead:"From cognates to alignments"

<p>Template-Based Alignment</p>

* phonetic alignment techniques are well-known in historical linguistics and have been applied for quite some time now (List 2014, Prokić et al. 2009)
* however, for languages with a rather restricted syllable structure, these techniques are actually not needed, as one could also align syllable-morphemes directly by using their *prosodic templates*
* a typical Chinese syllable, for example, consists of *initial*, *medial*, *nucleus*, *coda* and *tone* (Wang 1996)

<font color="red"> add another slide (same title and subtitle) in order to illustrate templatte-based alignments, ideally with a table</font>
--
## @head:"CALC workflows"
### @subhead:"From cognates to alignments"

Examine the results on EDICTOR! 
<a style="color:#2d1f23;text-align:center" href='http://edictor.digling.org/'>http://edictor.digling.org/</a>

--
## @head:"CALC workflows"
### @subhead:"From alignments to strict, cross-semantic cognates"

* our algorithm for automatic cognate dettection needs to start from words with the same meaning, as it would be too much noise for it to handle, if we had it search across all meanings
* therefore, we need to find *cross-semantic* (=normal) cogantes in a second stage
* given that many SEA languages are rich in compounidng, we find many words being re-used across the lexicon, even in small numbers of vocabulary
* we apply a new algorithm, inspired by maximum clique coverage, to *merge* cognates in our data into larger groups
* our basic check is if two alignments are compatible with each other, and if the words are *strictly* cognate

<font color="red">add an illustrational graphic here, that shows how alignments that are compatible can be merged</font>

--
## @head:"CALC workflows"
### @subhead:"From strict cognates to correspondence patterns"

---
## @head:"Conclusion and outlook" 


--
## @head:"Conclusion and outlook"
### @subhead:"Conclusion"

--
## @head:"Conclusion and outlook"
### @subhead:"Outlook"

---

<p style="font-size:100px;color:#768ca0;text-align:center;font-weight:bold;">
Thanks for Your Attention!

<p>CALC members:</p>
<ul>                        
<li> Dr. Johann-Mattis List (Group Leader)</li>    
<li> Dr. Yunfan Lai (Post-Doc)</li>
<li> Dr. Tiago Tresoldi (Post-Doc)</li>
<li> Nathanael E.Schweikhard (Doctoral student)</li>
<li> Mei-Shin Wu (Doctoral student)</li>
</ul>
