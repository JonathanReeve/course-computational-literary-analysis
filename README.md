# Introduction to Computational Literary Analysis

 - Instructor: Jonathan Reeve
 - Room: D-Lab,
 - Office Hours: TBD
 - Email address: jonathan.reeve@columbia.edu

## Description

This course is an introduction to computational literary analysis, one which presumes no background in programming or computer science. We will cover many of the topics of an introductory course in natural language processing or computational linguistics, but center our inquiries around literary critical questions. We will attempt to answer questions such as: 

 - Did Shakespeare write the so-called Shakespeare apocrypha plays? 
 - What are the characteristic speech patterns of the narrators in Wilkie Collins's _The Moonstone_?
 - What words are most frequently used to describe Katherine Mansfield's female characters? 
 - Which novels of the nineteenth century are the most similar to each other? Which are the most different? 

The course will teach techniques of text analysis using the Python programming language. Special topics to be covered include authorship detection (stylometry), topic modeling, and word embeddings. Literary works to be read and analyzed will be Wilkie Collins's _The Moonstone_, Katherine Mansfield's _The Garden Party and Other Stories_, and James Joyce's _Dubliners_.

## Objectives

Although this course is focused on the analysis of literature, and British literature in particular, the skills you will learn may be used to computationally analyze any text. These are skills transferable to other areas of the digital humanities, as well as computational linguistics, computational social science, and the computer science field of natural language processing. There are also potential applications across the humanistic disciplines—history, philosophy, art history, and cinema studies, to name a few. Furthermore, text- and data-analysis skills are widely desired in today's world. Companies like Google and Facebook, for instance, need ways to teach computers to understand their users' search queries, documents, and sometimes books. The techniques taught in this course help computers and humans to understand language, culture, and human interactions. This deepens our understanding of literature, of our fellow humans, and the world around us.

## Prerequisites 

This course presumes no prior knowledge of programming, computer science, or quantitative disciplines. Those with programming experience, however, won't find this boring: the level of specialization is such that only the first week covers the basics.

## Resources

The best resource for this course is [the course GitHub repository](https://github.com/JonathanReeve/course-computational-literary-analysis). We will also have a [Gitter chatroom]() for any questions you might have along the way, especially those that you think might be able to be answered by other students. Check out what's happening on Gitter as often as you can, and ask any questions you have there, first. 

If you want a second opinion, or have questions that we can't answer in the chatroom, a good website for getting help with programming is [StackOverflow](https://stackoverflow.com). 

Also, the Internet is full of Python learning resources. One of my favorites is [CodeCademy](https://codecademy.com), which has a game-like interactive interface, badges, and more. If you like a good puzzle, and like being challenged, there's also the older [Python Challenge](http://pythonchallenge.com). 

## Requirements

Coursework falls into three categories:

 - Annotations (30% of final grade)
 - Homework (30% of final grade)
 - Final project (40% of final grade)

Additionally, there are three course readings: one novel and two short story collections. Reading these closely will help you to contextualize the quantitative analyses, and will prepare you for the close reading tasks of the final paper. 

## Readings

All readings will be provided in digital form on the course GitHub repository, but if you prefer to read on paper, or to supplement your reading with background information and critical articles, I highly recommend the Broadview and Norton Critical Editions: 

 - Wilkie Collins, _The Moonstone_, Broadview Edition
   - [Available as paperback, pdf, or epub at Broadview Press](https://broadviewpress.com/product/the-moonstone/#tab-description)
 - Katherine Mansfield, _The Garden Party and Other Stories_, in _Katherine Mansfield's Selected Stories_, Norton Critical Edition
   - [Available as _Katherine Mansfield's Selected Stories_, in paperback from Norton Critical Editions](http://books.wwnorton.com/books/webad.aspx?id=11871)
 - James Joyce, _Dubliners_, Norton Critical Edition
   - [Available as paperback from Norton Critical Editions](http://books.wwnorton.com/books/webad.aspx?id=10295)

## Annotations

For each reading assignment, please write at least two annotations to our editions of the text, using [hypothes.is](http://hypothes.is). Links are provided below. You may write about anything you want, but it will help your final project to think about ways in which computational analysis might help you to better understand what you observe in the text. Good annotations are: 

 - Concise (think: a long tweet)
 - Well-written (although not too formal)
 - Observant (rather than evaluative)

You may respond to another student's annotation for one of your two, if you want.

## Homework 

Four short homework assignments, of 3-10 questions each, will be assigned weekly, and are due on Monday the following week. Jupyter notebook templates for each will be provided. Since we'll review the homework answers at the beginning of each week, late work cannot be accepted. There will be no homework due on the Monday of the last week, to give you more time to work on your final projects. 

Submit homework to BCourses, the course management system. If the system is not yet available, please email me your notebook. 

## Final Project / Paper

The final project will be a literary argument, presented in the form of a short academic paper, created from the application of one or more of the text analysis techniques we have learned toward the analysis of a text or corpus of your choosing. Should you choose to work with a text or corpus other than the ones we've discussed in class, please clear it with me beforehand. Your paper should be a Jupyter notebook, including prose in Markdown, code in Python, in-text citations, and a bibliography. A template will be provided. The length should be about the equivalent of an 6- to 8-page printed paper. You're allowed a maximum of three figures, so produce plots selectively. A word count function will be provided in the Jupyter notebook template. 

During the final week of class, we'll have final project presentations. Your paper isn't required to be complete by then, but you'll be expected to speak about your project for about 10 minutes. Consider it a conference presentation. 

Final papers will be evaluated according to the:

 - Quality of the literary critical argument presented
 - Quality of the close readings of the text or corpus
 - Quality of the Python text analysis
 - Literary interpretation of the results
 - Integration of the computational analysis with the literary argument

As with homework, please submit your final project to BCourses.

## Attendance 

Attendance is crucial. Although most course materials will be published in the course GitHub repository, they cannot replace hands-on experience with the techniques this course teaches. This is doubly true of in-class discussions of our readings. If you can't make it to a class for some reason, please let me know in advance, and arrange to get notes from a classmate.

# Schedule

## Week 1: Introduction to Python for Text Analysis
Text: [Wilkie Collins, _The Moonstone_](/readings/texts/moonstone)
Tools: Python (Anaconda)

 - Unit 1.1: Course intro. Motivation: what is possible with computational literary analysis? 
 - Unit 1.2: Installing Python. Python 2 v. 3. Jupyter. Jupyter toolchain, module installation, package importing. Strings. 
   - Text: [_The Moonstone_, First Period, Through Chapter IX](https://course-computational-literary-analysis.github.io/readings/texts/moonstone)
 - Unit 1.3: **No Class: Independence Day Holiday**
 - Unit 1.4: Working with strings. Splitting, concatenating, slicing, indexing. Working with lists and dictionaries. Slicing, indexing, appending. 
   - Text: [First Period, Through Chapter XV](https://course-computational-literary-analysis.github.io/readings/texts/moonstone/#chapter-x)
 
## Week 2 (7/9-7/13): Basic Text Analysis
Text: _The Moonstone_, Continued
Tools: Natural Language ToolKit (NLTK)

 - Unit 2.1: Review of Week 1 and Homework 1. Loading and manipulating plain text files.
   - Text: [First Period, Complete.](https://course-computational-literary-analysis.github.io/readings/texts/moonstone/#chapter-xv)
   - **Homework 1 due**
 - Unit 2.2: Working with words. Tokenization techniques. Lemmatizers.
   - Text: [Second Period, First Narrative](/readings/texts/moonstone/#second-period)
 - Unit 2.3: Basic text statistics with the NLTK. Type / token ratios. Loops, functions, and other control structures. 
   - Text: [Second Period, Second Narrative ](/readings/texts/moonstone/#second-narrative)
 - Unit 2.4: More text statistics. Concordances, collocations, dispersion plots. 
   - Text: [Second Period, Third Narrative](/readings/texts/moonstone/#third-narrative)

## Week 3 (7/16-7/19): Word Frequency Analyses
Text: _The Moonstone_ and Katherine Mansfield, _The Garden Party and Other Stories_ 
Tools: Scikit-Learn, Pandas

 - Unit 3.1: Review of Week 2 and Homework 2. Working with corpora and partitioned texts. Chapterization.
   - **Homework 2 due**
   - Text: [Second Period, Fourth and Fifth Narratives](/readings/texts/moonstone/#fourth-narrative)
 - Unit 3.2: Word frequency analyses. Document-term matrices. Principal Component Analysis and Latent Semantic Analysis.
   - Text: [_The Moonstone_, Complete](/readings/texts/moonstone/#sixth-narrative)
 - Unit 3.3: Data visualization using Pandas and Matplotlib.
   - Texts: ["The Garden Party"](/readings/texts/garden-party/#the-garden-party)
 - Unit 3.4: Stylometry: character voice and authorship attribution. 
   - Texts: ["The Daughters of the Late Colonel,"](/readings/texts/garden-party/#the-daughters-of-the-late-colonel) ["Mr. and Mrs. Dove"](/readings/texts/garden-party/#mr-and-mrs-dove)

## Week 4 (7/23-7/26): Linguistic Techniques I
Text: [Katherine Mansfield, _The Garden Party and Other Stories_](/readings/texts/garden-party)
Tools: NLTK, SpaCy

 - Unit 4.1: Review of Week 3 and Homework 3. 
   - **Homework 3 due**
   - Texts: ["The Young Girl,"](/readings/texts/garden-party/#the-young-girl) ["Life of Ma Parker"](/readings/texts/garden-party/#life-of-ma-parker)
 - Unit 4.2: Words: lexical tools. WordNet. Navigating hyponym trees. 
   - Texts: ["Marriage à la Mode,"](/readings/texts/garden-party/#marriage-a-la-mode) ["The Voyage"](/readings/texts/garden-party/#the-voyage)
 - Unit 4.4: Word probabilities. Identifying improbable words and ngrams. 
   - Texts: ["Her First Ball,"](/readings/texts/garden-party/#her-first-ball) ["The Stranger"](/readings/texts/garden-party/#the-stranger)
 - Unit 4.5: Quantifying parts-of-speech. Using Penn Treebank tags. Verb tense analyses. 
   - Texts: ["An Ideal Family,"](/readings/texts/garden-party/#an-ideal-family) ["The Lady's Maid"](/readings/texts/garden-party/#the-ladys-maid)

## Week 5 (7/30-8/2): Linguistic Techniques II
Text: James Joyce, _Dubliners_
Tools: SpaCy

 - Unit 5.1: Review of Week 4 and Homework 4. 
   - **Homework 4 due**
   - Texts: ["The Sisters,"](/readings/texts/dubliners/#the-sisters) ["An Encounter"](/readings/texts/dubliners/#an-encounter)
 - Unit 5.2: Intro to final project. 
   - Texts: ["Araby"](/readings/texts/dubliners/#araby), ["Eveline"](/readings/texts/dubliners/#eveline)
 - Unit 5.3: TF/IDF and distinguishing words. Macro-etymological textual analysis. 
   - Texts: ["After the Race,"](/readings/texts/dubliners/#after-the-race) ["Two Gallants"](/readings/texts/dubliners/#two-gallants)
 - Unit 5.4: Sentences: dependency parsing. Literary character attribute detection with dependency trees.
   - Texts: ["The Boarding House,"](/readings/texts/dubliners/#the-boarding-house) ["Clay"](/readings/texts/dubliners/#clay)

## Week 6 (8/6-8/9): Advanced Topics
Text: James Joyce, _Dubliners_
Tools: Scikit-Learn, SpaCy

 - Unit 6.1: Review of Week 5. 
   - Text: ["The Dead"](/readings/texts/dubliners/#the-dead)
 - Unit 6.2: Word embeddings. Document vectors. Semantic document similarity. 
 - Unit 6.3: Final project presentations. 
 - Unit 6.4: Final project presentations continued. Wrap-up. 
   - **Final project due** 
