
# Final Project Instructions

First, make sure you've read [the final project description in the syllabus](http://icla2021.jonreeve.com/#final-project). 

## Choosing a Corpus

 - You may choose any collection of text you like, so long as you make the case that it's *literary* in some way.
   - If it's not immediately obvious that you're working with a literary text, clear it with me beforehand (in #General on Zulip). 
 - Comparisons are good. It's a good idea to compare at least two texts, or many parts of a single text. 
   - E.g., it's not very meaningful to say that _The Moonstone_ contains 6% adverbs. But it could be very interesting to say that _The Moonstone_ has more adverbs than any other novel published that year!
 - If you're planning on doing some kind of statistical analysis, it's best to analyze texts containing a significant number of words. (It's not very meaningful to say that the word "plums" appears only once in William Carlos Williams's poem, "This is Just to Say.")
 - Choose only English texts. (Text analysis of other languages is very much possible, but it's beyond the scope of this course.)
   - Please don't choose texts that have been translated from other languages into English. The problem there is that word frequencies and other textual features won't reflect the choices of your chosen authors, but of the translator(s). 
   - One possible exception is that you're interested in comparing, say, twelve different English translations of the same ancient Greek text.
 - It's best to choose texts that you've read, or at least have passing familiarity with.
   - Texts that we've read in class are therefore good choices of corpora.
   - The more intimate you are with your text(s), the better your arguments will be. 
     - If you have time, read your text(s) closely. 
       - Obviously this is impossible if you're analyzing 1000 texts, but familiarize yourself with your corpus as much as you can.
   - Don't analyze anything completely blindly. 
     - Flip back and forth between reading your text and analyzing it computationally.

## Choosing Text Analysis Techniques

 - You may choose to apply one or more of the techniques we learned in class to your corpus, and/or write your own type of analysis.
 - **Go beyond your exploratory analysis.** An exploratory analysis, like we do in Homework 4, is great for discovering what you might want to look into further, but it isn't, and shouldn't be, your final project. Don't do everything you can and call it a day. Carefully choose your analytic method, and justify your choice.
 - One tactic is to model some textual phenomenon using some text analysis technique. 
   - Ex: model a text's "colorfulness" by quantifying its color words. 
   - Ex: model a text's "maleness" by counting the proportions of male to female pronouns, and other things you might consider masculine.
   - A common extension to this is to write a categorizer using your model: write a program that categorizes texts as either a detective novel or not a detective novel, using your model of what textual features you think a detective novel has. 
 - Another tactic is to test some critical theory using a computational method. 
   - Find an article that argues something testable about your text(s). Then write a program to test that argument. 
   - Ex: Edward Said has a book called _On Late Style_ in which he argues that a writer's last works are stylistically different from his earlier works. This can be tested using stylometry and a corpus of single-author collections of works.
 - You could also find some existing computational literary analysis, and reproduce it with Python. 
   - Ex: I once found a quantitative study of literature from 1885 (!) that just used pencil and paper, and recreated that study using Python.
 - Less is more. Final projects that try to run a dozen different analyses on a text are inevitably not as interesting as those that are more selective.

## Final Project Presentation Instructions

 - Create a four-minute video, (i.e., time > 3:59 and time < 5:00) and upload it to some video sharing platform before class begins on the due date. (I.e., before noon Berkeley time.)
   - You're not required to have finished your final project at this point, but you should have something to show.
 - Try for one slide per minute: thus, four slides. You may use a Jupyter notebook instead of slides, but presentations that use slides are usually better received, and easier to follow.
 - Post a link to your video in Zulip, in a new thread in the channel called #Final Project Presentations. The title of your thread should be your name and the title of your final project.
 - **Watch and respond to at least three other presentations.**
   - This is part of your presentation grade.
   - Write thoughtful responses. It's good to point out aspects of the project that are working well, and provide constructive criticism.

## Final Project Notebook Instructions

 - Final projects will be due by 11:59pm, Berkeley time, on August the 15th.
 - Like the homework, it should be a single Jupyter notebook (.ipynb), and nothing more. I'll provide a template.
 - Send it to me via email, to jonathan.reeve@columbia.edu.
 - Word count: 2,000–3,000 words of markdown prose.
   - I'll post a script that can help you count your prose.
   - Research is good. Try reading a few literary-critical articles that discuss your text(s).
     - The best final projects are usually in dialogue with some literary critical argument(s).
     - JSTOR and Google Scholar are good starting-points for finding literary critical articles that discuss your text(s). 
 - Treat it like writing an essay.
   - Give it a good title.
   - Start with a prose introduction. 
     - Say what your problem is. What questions are you trying to answer? 
   - End with a conclusion. 
 - You're limited to **a maximum of three figures/charts/visualizations**
   - This means, be selective about what you choose to visualize.
   - Subfigures are OK.
 - Write good markdown.
   - Ex: 'in the story "The Garden Party," by Katherine Mansfield' 
     - quotation marks for the titles of stories
   - Ex: 'in the book _The Garden Party and Other Stories_' 
     - italics for the titles of books
   - Don't use **emphasis formatting** if you can avoid it. Instead, emphasize things with your words.
   - It's better to write transition sentences to lead your reader to a new section, rather than subdivide your paper into too many sections using headings and subheadings. 
 - Use MLA format for citations.
   - Ex: "diamonds are forever" (Bond 132). 
   - Don't use parenthetical citations if it's obvious whom you're citing
   - Make a bibliography at the end called "Works Cited" listing all of the critical works you quote or reference. Make it the final cell in your notebook. 
   - Refer to [style.mla.org](https://style.mla.org/) for more details on MLA style. 
 - Write good code. 
   - Follow the DRY principle: don't repeat yourself. 
     - When you catch yourself writing (or copy-pasting) the same code snippet more than once, write a function that does that instead.
   - Document what you're doing with code comments and markdown cells. 
     - Code comments (lines beginning with `#` in Python) should usually reflect *why* you are writing what you're writing, rather than *what* you're writing. 
   - Functions are good! Use them everywhere.
   - Run all your cells to show your output.
   - Revise your code so that it's cleaner, nicer, and better documented. 
 - Failure can sometimes be interesting! 
   - Don't be afraid to show unexpected results, or analyses that didn't work the way you'd expected.
   
## Next Steps: **Optional**

 - You can get a small bonus of 5% on your final project, by making it public to the world. 
   - Make it a GitHub Gist or repository. 
   - Post the link to Zulip.
   - Add a link to your gist to the course repository.
 - Make a blog post about it? Tweet about it? 
 - Submit it to a conference? Like [DH2021](https://dh2021.adho.org/)
 - Submit it to a journal? Like [The Journal of Cultural Analytics](https://culturalanalytics.org/) 
   - Or [Digital Scholarship in the Humanities](https://academic.oup.com/dsh)
   - Respond to an existing paper? 
