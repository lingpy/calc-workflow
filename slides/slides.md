# Workflows ffor Computer-Assisted Language Comparison

@data-background:#f5f5f7
@data-transition:concave
@style:text-align:justify;
@style:font-size:85%;

---
@data-background:#f5f5f7
@style:text-align:center;
@style:font-size:100%;

## <font color = '#5b687c'>Workflows ffor Computer-Assisted Language Comparison</font>
----

<p style="text-align:center;color:#7687a1;font-weight:bold;font-size:110%;">State of the Art</p>
<p style="text-align:center">
<img src="img/calc-yinyang.svg" alt="image" style="width:200px"></img>
</p>


---
## @head:"Introduction"

<p style="text-align:center">
<img src="http://lingulist.de/documents/talks/img/edictor-tutorial/calc-7.png" alt="img" style="width:1000px;text-align:center;"></img>

</p>
--
## @head:"Introduction"
### @subhead:"The Gap between Computational and Traditional Historical Linguistics"

<p style="text-align:center">
<img src="http://lingulist.de/documents/talks/img/ba-talk/background-5-addon.jpg" alt="img" style="width:700px;text-align:center;"></img>

--
## @head:"Introduction"
### @subhead:"The Gap between Computational and Traditional Historical Linguistics"

<p style="text-align:center">
<img src="http://lingulist.de/documents/talks/img/ba-talk/background-11.jpg" alt="img" style="width:700px;text-align:center;"></img>

--
## @head:"Introduction"
### @subhead:"The Gap between Computational and Traditional Historical Linguistics"
<p style='text-align:center'>
<img src = "http://lingulist.de/documents/talks/img/ba-talk/background-12.jpg" style='width:700px;text-align:center'></img>
</p>
--
## @head:"Introduction"
### @subhead:"The Gap between Computational and Traditional Historical Linguistics"

<p style="text-align:center">
<img src="http://lingulist.de/documents/talks/img/calc-project/calc-5.jpg" style='width:900px;text-align:center'></img>
</p>
--
## @head:"Introduction"
### @subhead:"Computer-Assisted Disciplines"

<p style="text-align:center">
<img src="http://lingulist.de/documents/talks/img/calc-project/calc-7.jpg" style='width:900px;text-align:center'></img>
</p>

--
## @head:"Introduction"
### @subhead:"Computer-Assisted Disciplines"

To allow humans and machines to work together successfully, it is important that:

* our data is both human- and machine-readable,
* we follow transparent guidelents when handling linguistic datasets, 
* we offer interfaces that allow humans and machines to access the data at the same time.

---
## @head:"Workflows for Computer-Assisted Language Comparison"
### @subhead:"Overview"

<p style='text-align:center'>
<img src='img/HillList.png' style='width:700px;text-align:center'></img>
</p>

--
## @head:"Workflows for Computer-Assisted Language Comparison"
### @subhead:"Details of the workflows"
<p style="text-align:center">
<img src="img/calc-workflow.svg" alt="img" style="width:600px;text-align:center;"></img>
</p>
--
## @head:"Workflows for Computer-Assisted Language Comparison"
### @subhead:"Materials and methods"

<p style ='text-align:center'>
<img src ='img/languages.svg' style="width:500px"></img>
</p>
* Chén +++CHINESE NAME+++ (2012). Miao and Yao language. +++CHINESE TITLE+++
* 25 Hmong-Mien languages in the original (10 in our selection)
* 885 concepts in the original (313 in our selection, compatible with the Burmish Etymological dictionary project)

--
## @head:"Workflows for Computer-Assisted Language Comparison"
### @subhead:"From raw data to machine-readable data"
<p style='text-align:center'>
<img src="img/raw-machine.svg" style="width:800px" alt="img"></img>
</p>

--
## @head:"Workflows for Computer-Assisted Language Comparison"
### @subhead:"From raw data to machine-readable data"
<p style='text-align:center'>
<img src="img/chen-illustration.svg" style="width:800px" alt="img"></img>
</p>
--
## @head:"CALC workflows"
### @subhead:"From raw data to machine-readable data"

<div class="spreadsheet" data-delimiter="\t" data-width="100" fontsize="12">
     \t Baheng,east \t Baheng, west \t Qiandong, east \t Qiandong, wesst
七   \t  tsha³¹,tsjung⁴⁴ \t tshang⁴⁴    \t     shung⁵³    \t      shung²²
月亮 \t la⁰³lha⁵⁵ \t ʔa⁰³lha⁵⁵ \t la⁴⁴la⁴⁴ \t pau¹¹la³³
星星 \t la⁰³qang³⁵ \t qa⁰³qang³⁵ \t qei²⁴qei²⁴ \t tei⁴⁴qei⁴⁴
</div>

<!-- <font color="red">+++add example on no-goes from cldf paper forkel ett al. +++</font> -->

--
@class:scrollable
<div class="spreadsheet" data-delimiter="\t" style="width:1200px;height:600px;text-align:center;">
 ID \t DOCULECT        \t CONCEPT \t ENGLISH \t VALUE         \t FORM \t TOKENS \t NOTE
 1  \t Baheng, east    \t 七      \t SEVEN   \t tsja³¹,tsjung⁴⁴ \t tsja³¹     \t        \t 
 2  \t Baheng, east    \t 七      \t SEVEN   \t tsja³¹,tsjung⁴⁴ \t tsjung⁴⁴    \t        \t variant
 2  \t Baheng, west    \t 七      \t SEVEN   \t tsjang⁴⁴      \t tsjang⁴⁴      \t        \t
 3  \t Qiandong, east  \t 七      \t SEVEN   \t sjung⁵³       \t sjung⁵³       \t        \t
 4  \t Qiandong, wesst \t 七      \t SEVEN   \t sjung²²       \t sjung²²       \t        \t
 5  \t Baheng, east    \t 月亮    \t MOON    \t la⁰³lha⁵⁵     \t la⁰³lha⁵⁵     \t        \t
 6  \t Baheng, west    \t 月亮    \t MOON    \t ʔa⁰³lha⁵⁵     \t ʔa⁰³lha⁵⁵     \t        \t
 7  \t Qiandong, east  \t 月亮    \t MOON    \t la⁴⁴la⁴⁴      \t la⁴⁴la⁴⁴      \t        \t
 8  \t Qiandong, wesst \t 月亮    \t MOON    \t pau¹¹la³³     \t pau¹¹la³³     \t        \t
 9  \t Baheng, east    \t 星星    \t STAR    \t la⁰³qang³⁵    \t la⁰³qang³⁵    \t        \t
 10 \t Baheng, west    \t 星星    \t STAR    \t qa⁰³qang³⁵    \t qa⁰³qang³⁵    \t        \t
 11 \t Qiandong, east  \t 星星    \t STAR    \t qei²⁴qei²⁴    \t qei²⁴qei²⁴    \t        \t
 12 \t Qiandong, wesst \t 星星    \t STAR    \t tei⁴⁴qei⁴⁴    \t tei⁴⁴qei⁴⁴    \t        \t
</div>
--
## @head:"CALC workflows"
### @subhead:"From raw data to machine-readable data"
We recommend *orthography Profiles* as a way to:

<ul>
<li> convert arbitrary input data to IPA: </li>
  <ul style="list-style-type:none;">
    <li> tsj   ---->  tɕ </li>
    <li> ng    ---->   ŋ </li>
  </ul>
<li>and to segment the input data:</li>
tsja³¹  ----> tɕja³¹ ----> tɕ j a ³¹
</ul>
--
## @head:"CALC workflows"
### @subhead:"From raw data to machine-readable data"
<div class="spreadsheet" data-delimiter="\t" style="width:100px;height:600px;text-align:center;">
Grapheme \t IPA
č        \t tʃ
ž        \t dʒ
th       \t tʰ
dh       \t d̤
sh       \t ʃ
a        \t a
aa       \t aː
tsj	 \t tɕ
la	 \t l a
</div>
--
## @head:"CALC workflows"
### @subhead:"From raw data to machine-readable data"
@class:scrollable
<div class="spreadsheet" data-delimiter="\t" data-width="100" fontsize="12">
ID  \t DOCULECT        \t CONCEPT \t ENGLISH \t VALUE           \t FORM       \t TOKENS              \t COGID
 1  \t Baheng, east    \t 七      \t SEVEN   \t tsja³¹,tsjung⁴⁴ \t tsja³¹     \t tɕ a ³¹             \t
 2  \t Baheng, east    \t 七      \t SEVEN   \t tsja³¹,tsjung⁴⁴ \t tsjung⁴⁴   \t tɕ u ŋ ⁴⁴           \t
 3  \t Baheng, west    \t 七      \t SEVEN   \t tsjang⁴⁴        \t tsjang⁴⁴   \t tɕ a ŋ ⁴⁴           \t
 4  \t Qiandong, east  \t 七      \t SEVEN   \t sjung⁵³         \t sjung⁵³    \t ɕ u ŋ ⁵³            \t
 5  \t Qiandong, wesst \t 七      \t SEVEN   \t sjung²²         \t sjung²²    \t ɕ u ŋ ²²            \t
 6  \t Baheng, east    \t 月亮    \t MOON    \t la⁰³lha⁵⁵       \t la⁰³lha⁵⁵  \t l a ³/⁰ + ɬ a ⁵⁵    \t
 7  \t Baheng, west    \t 月亮    \t MOON    \t ʔa⁰³lha⁵⁵       \t ʔa⁰³lha⁵⁵  \t ʔ a ³/⁰ + ɬ a ⁵⁵    \t
 8  \t Qiandong, east  \t 月亮    \t MOON    \t la⁴⁴la⁴⁴        \t la⁴⁴la⁴⁴   \t l a ⁴⁴ + l a ⁴⁴     \t
 9  \t Qiandong, wesst \t 月亮    \t MOON    \t pau¹¹la³³       \t pau¹¹la³³  \t p ɔ ¹¹ + l a ³³     \t
 10 \t Baheng, east    \t 星星    \t STAR    \t la⁰³qang³⁵      \t la⁰³qang³⁵ \t l a ³/⁰ + q a ŋ ³⁵  \t
 11 \t Baheng, west    \t 星星    \t STAR    \t qa⁰³qang³⁵      \t qa⁰³qang³⁵ \t q a ³/⁰ + q a ŋ ³⁵  \t
 12 \t Qiandong, east  \t 星星    \t STAR    \t qei²⁴qei²⁴      \t qei²⁴qei²⁴ \t q ei ²⁴ + q ei  ²⁴  \t
 13 \t Qiandong, wesst \t 星星    \t STAR    \t tei⁴⁴qei⁴⁴      \t tei⁴⁴qei⁴⁴ \t t ei - ⁴⁴ + q ei ⁴⁴ \t
</div>

--
## @head:"CALC workflows"
### @subhead:"From segmented words to computer-inferred cognates"

<p style='text-align:center'>
<img src="img/machine-partial.svg" style="width:800px" alt="img"></img>
</p>

--
## @head:"CALC workflows"
### @subhead:"From segmented words to computer-inferred cognates"

<p style='text-align:center'>
<img src="img/partialcg.png" style="width:800px" alt="img"></img>
</p>


--
## @head:"CALC workflows"
### @subhead:"From segmented words to computer-inferred cognates"

<p align="middle"><img src="http://lingulist.de/documents/talks/img/calc-project/algo2.jpg" style="width:800px;align:middle;"></img></p>
<p style='text-align:center;font-size:60%;'>List et al. (2016). Using sequence similarity networks to identify partial cognates in multilingual wordlists. In Proceedings of the 54th Annual Meeting of the Association for Computational Linguistics (Vol. 2, pp. 599-605).</p>

--
## @head:"CALC workflows"
### @subhead:"From segmented words to computer-inferred cognates"

@class:scrollable
<div class="spreadsheet" data-delimiter="\t" data-width="100" fontsize="12">
ID  \t DOCULECT        \t CONCEPT \t ENGLISH \t VALUE           \t FORM         \t TOKENS              \t COGIDS
 1  \t Baheng, east    \t 七      \t SEVEN   \t tsja³¹,tsjung⁴⁴ \t tsja³¹      \t tɕ a ³¹             \t 3
 2  \t Baheng, east    \t 七      \t SEVEN   \t tsja³¹,tsjung⁴⁴ \t tsjung⁴⁴    \t tɕ u ŋ ⁴⁴           \t 3
 3  \t Baheng, west    \t 七      \t SEVEN   \t tsjang⁴⁴        \t tsjang⁴⁴    \t tɕ a ŋ ⁴⁴           \t 3
 4  \t Qiandong, east  \t 七      \t SEVEN   \t sjung⁵³         \t sjung⁵³     \t ɕ u ŋ ⁵³            \t 3
 5  \t Qiandong, wesst \t 七      \t SEVEN   \t sjung²²         \t sjung²²     \t ɕ u ŋ ²²            \t 3
 6  \t Baheng, east    \t 月亮    \t MOON    \t la⁰³lha⁵⁵       \t la⁰³lha⁵⁵   \t l a ³/⁰ + ɬ a ⁵⁵    \t 1908 1907
 7  \t Baheng, west    \t 月亮    \t MOON    \t ʔa⁰³lha⁵⁵       \t ʔa⁰³lha⁵⁵   \t ʔ a ³/⁰ + ɬ a ⁵⁵    \t 1909 1907
 8  \t Qiandong, east  \t 月亮    \t MOON    \t la⁴⁴la⁴⁴        \t la⁴⁴la⁴⁴    \t l a ⁴⁴ + l a ⁴⁴     \t 1908 1907
 9  \t Qiandong, wesst \t 月亮    \t MOON    \t pau¹¹la³³       \t pau¹¹la³³   \t p ɔ ¹¹ + l a ³³     \t 1910 1907
 10 \t Baheng, east    \t 星星    \t STAR    \t la⁰³qang³⁵      \t la⁰³qang³⁵  \t l a ³/⁰ + q a ŋ ³⁵  \t 1874 1870
 11 \t Baheng, west    \t 星星    \t STAR    \t qa⁰³qang³⁵      \t qa⁰³qang³⁵  \t q a ³/⁰ + q a ŋ ³⁵  \t 　1872 1870
 12 \t Qiandong, east  \t 星星    \t STAR    \t qei²⁴qei²⁴      \t qei²⁴qei²⁴  \t q ei ²⁴ + q ei  ²⁴  \t 　1872 1870
 13 \t Qiandong, wesst \t 星星    \t STAR    \t tei⁴⁴qei⁴⁴      \t tei⁴⁴qei⁴⁴  \t t ei - ⁴⁴ + q ei ⁴⁴ \t 　1871 1870
</div>

--
## @head:"CALC workflows"
### @subhead:"From cognates to alignments"

<p style='text-align:center'>
<img src="img/partial-alignment.svg" style="width:800px" alt="img"></img>
</p>
--
## @head:"CALC workflows"
### @subhead:"From cognates to alignments"

<p align="middle"><img src='img/alignment.png' style="width:400px;align:middle;"></img></p>

Phonetic alignment techniques are well-known in historical linguistics and have been applied for quite some time now.

--
## @head:"CALC workflows"
### @subhead:"From cognates to alignments"

We propose *Template-Based Alignments* as an alternative to semi-automatically computed alignments.

* Languages with a rather restricted syllable structure can usually be aligned in a very consistent way by simply using a template.
* A typical Chinese syllable, for example, consists of *initial*, *medial*, *nucleus*, *coda* and *tone* (Wang 1996). Once we know the individual template of a Chinese word, we can easily align it with any other word, as long as we know the template.

<!-- <font color="red"> add another slide (same title and subtitle) in order to illustrate templatte-based alignments, ideally with a table</font> -->
--
## @head:"CALC workflows"
### @subhead:"From cognates to alignments"



<p align="middle"><img src='img/templates.png' style="width:1000px;align:middle;"></img></p>

--
## @head:"CALC workflows"
### @subhead:"From cognates to alignments"



<p align="middle"><img src='img/orthotemplate.png' style="width:600px;align:middle;"></img></p>


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
### @subhead:"From alignments to strict, cross-semantic cognates"

<p style='text-align:center'>
<img src="img/alignment-strict.svg" style="width:800px" alt="img"></img>
</p>
--
## @head:"CALC workflows"
### @subhead:"From alignments to strict, cross-semantic cognates"

* For a realistic analysis, we need to identify cognates not only within the same meaning slot, but across different concepts.
* However, our algorithm for automatic congate detection designed to search words with the same meaning. 
* Therefore, we need to find *cross-semantic* partial (=normal) cognates in a second stage.


--
## @head:"CALC workflows"
### @subhead:"From alignments to strict, cross-semantic cognates"

* For this task, we employ a new algorithm to *merge* cognates in our data into larger groups.
* The basic idea is to check if two alignments are compatible with each other, and to fuse them to form a bigger alignment, if this is the case.
* As a side effect, all words we identify in this way are *strictly* cognate, since our procedure does not allow to identify a morpheme in the same language to be cognate if this does not show the exact same form.


--
## @head:"CALC workflows"
### @subhead:"From alignments to strict, cross-semantic cognates"

<!--<font color="red">add an illustrational graphic here, that shows how alignments that are compatible can be merged</font>-->

<p style='text-align:center'>
<img src="img/cross-semantic-picture.png" style="width:800px" alt="img"></img>
</p>
--
## @head:"CALC workflows"
### @subhead:"From alignments to strict, cross-semantic cognates"

<p style='text-align:center'>
<img src="img/cross-semantic-table.png" style="width:800px" alt="img"></img>
</p>

--
## @head:"CALC workflows"
### @subhead:"From alignments to strict, cross-semantic cognates"

@class:scrollable
<div class="spreadsheet" data-delimiter="\t" data-width="100" fontsize="12">
ID  \t DOCULECT        \t ENGLISH \t TOKENS             \t STRUCTURE \t ALIGNMENT \t CROSSIDS            \t COGIDS
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

--
<p style='text-align:center'>
<img src="img/strict-soundcorrespondence.svg" style="width:800px" alt="img"></img>
</p>


--
## @head:"CALC workflows"
### @subhead:"From strict, cross-semantic cognates to sound correspondence patterns"

<p style="text-align:center">
<img src="img/sound-correspondence-classic.png" alt="img" style="width:900px;text-align:center;"></img>
</p>

--
## @head:"CALC workflows"
### @subhead:"From strict, cross-semantic cognates to sound correspondence patterns"
<p style="text-align:center">
<img src="img/ratliff2010.png" alt="img" style="width:600px;text-align:center;"></img>
</p>
(Ratliff, 2010:57)
--
## @head:"CALC workflows"
### @subhead:"From strict, cross-semantic cognates to sound correspondence patterns"

<p style="text-align:center">
<img src="img/edictor-hn.png" alt="img" style="width:600px;text-align:center;"></img>
</p>

--
## @head:"Illustration of the Workflow"
### @subhead:"From Raw Data to Segmented Data"
<a style="color:#2d1f23;text-align:center" href='http://calc.digling.org/profile/'> http://calc.digling.org/profile/</a>
--
## @head:"Illustration of the Workflow"
### @subhead:"EDICTOR"
<p>EDICTOR: a web-based tool to edit, analyse, and publish etymological data.</p>
<p style="text-align:center">
<a style="color:#2d1f23" href='http://edictor.digling.org/' align='middle'><img src='img/edictor.png' width=300px></img></a>
</p>

---
## @head:"Conclusion and outlook"
<img src="img/outlook.jpg" alt="img" style="width:900px;text-align:center;"></img>

--
## @head:"Conclusion and outlook"
### @subhead:"Discussion"

Possible improvements:

<ul>
<li>Semi-automatic reconstruction (currently tested by Nathan Hill and Johann-Mattis List).</li>
<li>Clearer integration of automatic and semi-automatic methods in the workflow.</li>
<li>Enhancing the visualization of the results (Xun Gong is working on this for the Burmish Etymological Dictionary project).</li>
</ul>


--
## @head:"Conclusion and outlook"
### @subhead:"Discussion"

Challenges:

<ul>
<li>Lexical reconstruction: how can we reconstruct whole words?</li>
<li>Sound change: can we represent all changes from a proto-form along some phylogeny along with sound laws?</li>
</ul>

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
