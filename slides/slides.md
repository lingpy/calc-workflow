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

<p style="text-align:center">
<img src="http://lingulist.de/documents/talks/img/calc-project/calc-5.jpg" style='width:900px;text-align:center'></img>
</p>

--
## @head:"Introduction"
### @subhead:"What is a computer-assisted approach"

<p style="text-align:center">
<img src="http://lingulist.de/documents/talks/img/calc-project/calc-7.jpg" style='width:900px;text-align:center'></img>
</p>

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

<p>An example of common raw data format</p>
<div class="spreadsheet" data-delimiter="\t" data-width="100" fontsize="12">
     \t Baheng,east \t Baheng, west \t Qiandong, east \t Qiandong, wesst
七   \t  tsha³¹      \t tshang⁴⁴    \t     shung⁵³    \t      shung²²
月亮 \t la⁰³lha⁵⁵ \t ʔa⁰³lha⁵⁵ \t la⁴⁴la⁴⁴ \t pau¹¹la³³
星星 \t la⁰³qang³⁵ \t qa⁰³qang³⁵ \t qei²⁴qei²⁴ \t tei⁴⁴qei⁴⁴
</div>

<!-- <font color="red">+++add example on no-goes from cldf paper forkel ett al. +++</font> -->

--
## @head:"CALC workflows"
@class:scrollable
<div class="spreadsheet" data-delimiter="\t" width="80%" fontsize="12" height="80%" align='center'>
 ID  \t DOCULECT       \t CONCEPT \t ENGLISH  \t VALUE      \t IPA \t TOKENS \t COGID
 1   \t Baheng, east   \t 七      \t SEVEN    \t tsha³¹     \t     \t        \t
 2   \t Baheng, west   \t 七      \t SEVEN    \t tshang⁴⁴   \t     \t        \t
 3   \t Qiandong, east \t 七      \t SEVEN    \t shung⁵³    \t     \t        \t
 4   \t Qiandong, wesst\t 七      \t SEVEN    \t shung²²    \t     \t        \t
 5   \t Baheng, east   \t 月亮    \t MOON     \t la⁰³lha⁵⁵  \t     \t        \t
 6   \t Baheng, west   \t 月亮    \t MOON     \t ʔa⁰³lha⁵⁵  \t     \t        \t
 7   \t Qiandong, east \t 月亮    \t MOON     \t la⁴⁴la⁴⁴   \t     \t        \t
 8   \t Qiandong, wesst\t 月亮    \t MOON     \t pau¹¹la³³  \t     \t        \t
 9   \t Baheng, east   \t 星星    \t STAR    \t la⁰³qang³⁵  \t     \t        \t
 10  \t Baheng, west   \t 星星    \t STAR    \t qa⁰³qang³⁵  \t     \t        \t
 11  \t Qiandong, east \t 星星    \t STAR    \t qei²⁴qei²⁴  \t     \t        \t
 12  \t Qiandong, wesst\t 星星    \t STAR    \t tei⁴⁴qei⁴⁴  \t     \t        \t
</div>

--
## @head:"CALC workflows"
### @subhead:"From raw data to machine-readable data"

<p>You can manually type the IPA and tokenize the IPA into morphemes</p>
<p>What if, we are dealing with <b>hundrends of entries?</b> </p>
<p>Is there an efficient way?</p>

--
## @head:"CALC workflows"
### @subhead:"From raw data to machine-readable data"
<p>A guideline to teach computer how to seperate the phonetic sequences into sequences of phonemes</p>
<p>Choose one from many existing profiles to tokenize your data</p>
<a style="color:#2d1f23;text-align:center" href='http://calc.digling.org/profile/'> http://calc.digling.org/profile/</a>

--
## @head:"CALC workflows"
### @subhead:"From raw data to machine-readable data"
@class:scrollable
<div class="spreadsheet" data-delimiter="\t" data-width="100" fontsize="12">
ID  \t DOCULECT       \t CONCEPT \t ENGLISH  \t VALUE      \t IPA         \t TOKENS              \t COGID
 1   \t Baheng, east   \t 七      \t SEVEN    \t tsha³¹     \t  tɕa³¹     \t tɕ a ³¹              \t
 2   \t Baheng, west   \t 七      \t SEVEN    \t tshang⁴⁴   \t  tɕaŋ⁴⁴    \t tɕ a ŋ ⁴⁴            \t	
 3   \t Qiandong, east \t 七      \t SEVEN    \t shung⁵³    \t  ɕuŋ⁵³     \t ɕ u ŋ ⁵³             \t
 4   \t Qiandong, wesst\t 七      \t SEVEN    \t shung²²    \t  ɕuŋ²²     \t ɕ u ŋ ²²             \t 
 5   \t Baheng, east   \t 月亮    \t MOON     \t la⁰³lha⁵⁵  \t la³/⁰+ɬa⁵⁵ \t l a ³/⁰ + ɬ a ⁵⁵      \t
 6   \t Baheng, west   \t 月亮    \t MOON     \t ʔa⁰³lha⁵⁵  \t ʔa³/⁰+ɬa⁵⁵ \t ʔ a ³/⁰ + ɬ a ⁵⁵       \t
 7   \t Qiandong, east \t 月亮    \t MOON     \t la⁴⁴la⁴⁴   \t la⁴⁴+la⁴⁴  \t l a ⁴⁴ + l a ⁴⁴       \t
 8   \t Qiandong, wesst\t 月亮    \t MOON     \t pau¹¹la³³  \t pɔ¹¹+la³³  \t p ɔ ¹¹ + l a ³³       \t
 9   \t Baheng, east   \t 星星    \t STAR    \t la⁰³qang³⁵  \t la³/⁰+qaŋ³⁵ \t l a ³/⁰ + q a ŋ ³⁵   \t
 10  \t Baheng, west   \t 星星    \t STAR    \t qa⁰³qang³⁵  \t qa³/⁰+qaŋ³⁵ \t q a ³/⁰ + q a ŋ ³⁵   \t	
 11  \t Qiandong, east \t 星星    \t STAR    \t qei²⁴qei²⁴  \t qei²⁴+qei²⁴ \t q ei ²⁴ + q ei  ²⁴   \t
 12  \t Qiandong, wesst\t 星星    \t STAR    \t tei⁴⁴qei⁴⁴  \t tei⁴⁴+qei⁴⁴ \t t ei - ⁴⁴ + q ei ⁴⁴  \t
</div>

--
## @head:"CALC workflows"
### @subhead:"From segmented words to computer-inferred cognates"

<p align="middle"><img src="http://lingulist.de/documents/talks/img/calc-project/algo2.jpg" style="width:800px;align:middle;"></img></p>

--
## @head:"CALC workflows"
### @subhead:"From segmented words to computer-inferred cognates"
<p>Lingpy : a python library for *quantitative tasks* in historical linguistics</p>

* Phonetic alignment
* Computer-inferred cognates

<p>Linguists can then examine as well as modfiy the cognates.</p>
--
## @head:"CALC workflows"
### @subhead:"From segmented words to computer-inferred cognates"

@class:scrollable
<div class="spreadsheet" data-delimiter="\t" data-width="100" fontsize="12">
ID  \t DOCULECT       \t CONCEPT \t ENGLISH  \t VALUE      \t IPA         \t TOKENS              \t COGID
 1   \t Baheng, east   \t 七      \t SEVEN    \t tsha³¹     \t  tɕa³¹     \t tɕ a ³¹              \t 3
 2   \t Baheng, west   \t 七      \t SEVEN    \t tshang⁴⁴   \t  tɕaŋ⁴⁴    \t tɕ a ŋ ⁴⁴            \t 3
 3   \t Qiandong, east \t 七      \t SEVEN    \t shung⁵³    \t  ɕuŋ⁵³     \t ɕ u ŋ ⁵³             \t 3
 4   \t Qiandong, wesst\t 七      \t SEVEN    \t shung²²    \t  ɕuŋ²²     \t ɕ u ŋ ²²             \t 3
 5   \t Baheng, east   \t 月亮    \t MOON     \t la⁰³lha⁵⁵  \t la³/⁰+ɬa⁵⁵ \t l a ³/⁰ + ɬ a ⁵⁵     \t 1908 1907
 6   \t Baheng, west   \t 月亮    \t MOON     \t ʔa⁰³lha⁵⁵  \t ʔa³/⁰+ɬa⁵⁵ \t ʔ a ³/⁰ + ɬ a ⁵⁵      \t 1909 1907	
 7   \t Qiandong, east \t 月亮    \t MOON     \t la⁴⁴la⁴⁴   \t la⁴⁴+la⁴⁴  \t l a ⁴⁴ + l a ⁴⁴      \t 1908 1907
 8   \t Qiandong, wesst\t 月亮    \t MOON     \t pau¹¹la³³  \t pɔ¹¹+la³³  \t p ɔ ¹¹ + l a ³³       \t 1910 1907
 9   \t Baheng, east   \t 星星    \t STAR    \t la⁰³qang³⁵  \t la³/⁰+qaŋ³⁵ \t l a ³/⁰ + q a ŋ ³⁵   \t 1874 1870
 10  \t Baheng, west   \t 星星    \t STAR    \t qa⁰³qang³⁵  \t qa³/⁰+qaŋ³⁵ \t q a ³/⁰ + q a ŋ ³⁵   \t　1872 1870	
 11  \t Qiandong, east \t 星星    \t STAR    \t qei²⁴qei²⁴  \t qei²⁴+qei²⁴ \t q ei ²⁴ + q ei  ²⁴   \t　1872 1870
 12  \t Qiandong, wesst\t 星星    \t STAR    \t tei⁴⁴qei⁴⁴  \t tei⁴⁴+qei⁴⁴ \t t ei - ⁴⁴ + q ei ⁴⁴  \t　1871 1870
</div>

--
## @head:"CALC workflows"
### @subhead:"From segmented words to computer-inferred cognates"
<p>EDICTOR: a web-based tool to edit, analyse, and publish etymological data.</p>
<p style="text-align:center">
<a style="color:#2d1f23" href='http://edictor.digling.org/' align='middle'><img src='img/edictor.png' width=300px></img></a>
</p>
--
## @head:"CALC workflows"
### @subhead:"From cognates to alignments"

<p>Template-Based Alignment</p>

* phonetic alignment techniques are well-known in historical linguistics and have been applied for quite some time now (List 2014, Prokić et al. 2009)
* however, for languages with a rather restricted syllable structure, these techniques are actually not needed, as one could also align syllable-morphemes directly by using their *prosodic templates*
* a typical Chinese syllable, for example, consists of *initial*, *medial*, *nucleus*, *coda* and *tone* (Wang 1996)

<!-- <font color="red"> add another slide (same title and subtitle) in order to illustrate templatte-based alignments, ideally with a table</font> -->
--
## @head:"CALC workflows"
### @subhead:"From cognates to alignments"

@class:scrollable
<div class="spreadsheet" data-delimiter="\t" data-width="100" fontsize="12">
ID  \t DOCULECT        \t ENGLISH \t TOKENS             \t STRUCTURE \t ALIGNMENT \t COGID
 1   \t Baheng, east   \t SEVEN   \t tɕ a ³¹             \t i n t     \t tɕ a - ³¹ \t 3
 2   \t Baheng, west   \t SEVEN   \t tɕ a ŋ ⁴⁴           \t i n c t   \t tɕ a ŋ ⁴⁴ \t 3
 3   \t Qiandong, east \t SEVEN   \t ɕ u ŋ ⁵³            \t i n c t   \t  ɕ u ŋ ⁵³ \t 3
 4   \t Qiandong, wesst\t SEVEN   \t ɕ u ŋ ²²            \t i n c t   \t ɕ u ŋ ²²  \t 3
 5   \t Baheng, east   \t MOON    \t l a ³/⁰ + ɬ a ⁵⁵    \t i n t + i n t \t l a ³/⁰ + ɬ a ⁵⁵\t 1908 1907
 6   \t Baheng, west   \t MOON    \t ʔ a ³/⁰ + ɬ a ⁵⁵    \t i n t + i n t \t ʔ a ³/⁰ + ɬ a ⁵⁵ \t 1909 1907	
 7   \t Qiandong, east \t MOON    \t l a ⁴⁴ + l a ⁴⁴    \t i n t + i n t \t l a ⁴⁴ + l a ⁴⁴ \t 1908 1907
 8   \t Qiandong, wesst\t MOON    \t p ɔ ¹¹ + l a ³³    \t i n t + i n t \t p ɔ ¹¹ + l a ³³ \t 1910 1907
 9   \t Baheng, east   \t STAR    \t l a ³/⁰ + q a ŋ ³⁵ \t i n t + i n c t \t l a ³/⁰ + q a ŋ ³⁵ \t 1874 1870
 10  \t Baheng, west   \t STAR    \t q a ³/⁰ + q a ŋ ³⁵ \t　i n t + i n c t \t q a ³/⁰ + q a ŋ ³⁵ \t 1872 1870	
 11  \t Qiandong, east \t STAR    \t q ei ²⁴ + q ei  ²⁴ \t　i n t + i n t \t q ei ²⁴ + q ei - ²⁴ \t  1872 1870
 12  \t Qiandong, wesst\t STAR    \t t ei - ⁴⁴ + q ei ⁴⁴\t　i n t + i n t \t t ei - ⁴⁴ + q ei - ⁴⁴\t 1871 1870
</div>


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

@class:scrollable
<div class="spreadsheet" data-delimiter="\t" data-width="100" fontsize="12">
ID  \t DOCULECT        \t ENGLISH \t TOKENS             \t STRUCTURE \t ALIGNMENT \t CROSSID            \t COGID
 1   \t Baheng, east   \t SEVEN   \t tɕ a ³¹             \t i n t     \t tɕ a - ³¹ \t 3                  \t 3
 2   \t Baheng, west   \t SEVEN   \t tɕ a ŋ ⁴⁴           \t i n c t   \t tɕ a ŋ ⁴⁴ \t 3                  \t 3
 3   \t Qiandong, east \t SEVEN   \t ɕ u ŋ ⁵³            \t i n c t   \t  ɕ u ŋ ⁵³ \t 3                  \t 3
 4   \t Qiandong, wesst\t SEVEN   \t ɕ u ŋ ²²            \t i n c t   \t ɕ u ŋ ²²  \t 3                  \t 3
 5   \t Baheng, east   \t MOON    \t l a ³/⁰ + ɬ a ⁵⁵    \t i n t + i n t \t l a ³/⁰ + ɬ a ⁵⁵\t 1908 351 \t 1908 1907
 6   \t Baheng, west   \t MOON    \t ʔ a ³/⁰ + ɬ a ⁵⁵    \t i n t + i n t \t ʔ a ³/⁰ + ɬ a ⁵⁵ \t 41 351	\t 1909 1907
 7   \t Qiandong, east \t MOON    \t l a ⁴⁴ + l a ⁴⁴    \t i n t + i n t \t l a ⁴⁴ + l a ⁴⁴ \t 1908 351 \t 1908 1907
 8   \t Qiandong, wesst\t MOON    \t p ɔ ¹¹ + l a ³³    \t i n t + i n t \t p ɔ ¹¹ + l a ³³ \t 1910 351  \t 1910 1907
 9   \t Baheng, east   \t STAR    \t l a ³/⁰ + q a ŋ ³⁵ \t i n t + i n c t \t l a ³/⁰ + q a ŋ ³⁵ \t 1874 1834 \t 1874 1870
 10  \t Baheng, west   \t STAR    \t q a ³/⁰ + q a ŋ ³⁵ \t　i n t + i n c t \t q a ³/⁰ + q a ŋ ³⁵ \t 1872 1834 \t 1872 1870
 11  \t Qiandong, east \t STAR    \t q ei ²⁴ + q ei  ²⁴ \t　i n t + i n t \t q ei ²⁴ + q ei - ²⁴ \t  1872 1834 \t 1872 1870
 12  \t Qiandong, wesst\t STAR    \t t ei - ⁴⁴ + q ei ⁴⁴\t　i n t + i n t \t t ei - ⁴⁴ + q ei - ⁴⁴\t 1234 1834 \t 1871 1870
</div>


---
## @head:"Conclusion and outlook" 
<img src="img/outlook.jpg" alt="img" style="width:900px;text-align:center;"></img>

--
## @head:"Conclusion and outlook"
### @subhead:"Future work"

* Semi-automated reconstruction
* Test consistency of cognates
* Test consistency of reconstruction systems

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
