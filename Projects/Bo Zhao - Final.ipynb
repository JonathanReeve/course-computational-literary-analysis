{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Digital Humanities and Text and Language Analysis\n",
    "## Zhao, Bo\n",
    "# Commonalities of Detective Novels, from _The Moonstone_ to _Sherlock Holmes_\n",
    "Instructions: \n",
    "\n",
    "1. Replace \"yourname\" in the title of this notebook, and \"your name here\" in the markdown above, with your name.\n",
    "2. Create a title for your final project. Preferably, this should indicate what your argument is. Replace \"your title here\" in the markdown above with your title.\n",
    "3. Write your paper, and include everything (your prose in Markdown, your code, and your figures) in this notebook. Don't include the texts you're analyzing. If you generated your corpus programmatically (i.e. using corpus-db.org or some fancy Python), maybe you'll want to include that in the code somewhere here. Your notebook file (`.ipynb`) will be the only thing you turn in.  \n",
    "3. Annotate your code using markdown cells, and/or comment lines (lines beginning with `#`), explaining why you're doing what you're doing. If one of your functions takes certain parameters, for instance, why did you choose those parameters? \n",
    "3. Prune your notebook of unnecessary or redundant code. Run all your code again, to show that it works as-is. Each code cell should have a number in it, and an output, if applicable. \n",
    "4. Proofread well! If English is not your first language, you might consider making an appointment with [the Writing Center](https://slc.berkeley.edu/appointment-service) to get help polishing the language of your paper. At the minimum, you'll want to use a spell checker and maybe even an automatic grammar-checking service like [Grammerly](https://www.grammarly.com/). (Of course, you now have the tools to analyze your own writing, if you want. You can get your markdown text into Python by adapting the word count function below, and use it to analyze your most frequent n-grams!) You might also consider organizing a mutual editing session with classmates.\n",
    "4. Ensure that you have no more than three plots (figures). One figure with several subplots is OK, and counts as one figure.\n",
    "4. If you quote from or reference literary works, or works of criticirm, provide in-text parenthetical citations. Then create a bibliographic entry for each work you cite, and include them at the end. Unless your discipline requires a different format, use [MLA Style](https://style.mla.org/) as the format for your bibliography, and title it \"works cited.\" \n",
    "4. Replace the value of the `filename` variable in the wordcount cell below to the name your file. (E.g., `Jonathan-Final.ipynb`.) Then run the wordcount cell. Ensure that your paper is between 1000 and 2000 words, so it doesn't give you any errors or warnings.  \n",
    "5. Optionally, and for a 5% bonus, add your notebook to the `/Projects` directory of the course repository, and submit it as a pull request. Your project will then become public. \n",
    "6. Email me your `.ipynb` file: jonathan.reeve@columbia.edu. Please email me only your `.ipynb` file, alone and uncompressed. Please don't respond to an existing email, but create a new email, with the subject: `Yourname: Final Project`, replacing `yourname` with your name. Do this regardless of whether you also submit a pull request. \n",
    "7. Celebrate! You've finished your final project, and gloriously completed _Introduction to Computational Literary Analysis_!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import all your libraries here, and only here, please.\n",
    "\n",
    "# Don't remove this line. It's necessary for the wordcount function \n",
    "# below to work. \n",
    "from IPython.nbformat import current\n",
    "from nltk.corpus import brown\n",
    "from nltk.text import Text\n",
    "from collections import Counter\n",
    "from textblob import TextBlob\n",
    "import pandas as pd\n",
    "from nltk import word_tokenize, sent_tokenize, pos_tag, ngrams, pos_tag_sents\n",
    "from sklearn.feature_extraction.text import TfidfVectorizer\n",
    "from sklearn.decomposition import PCA\n",
    "import requests\n",
    "import json\n",
    "\n",
    "\n",
    "\n",
    "# This is to make your plots a little bigger.\n",
    "# You may adjust this, but be careful of making your plots too big or too small.\n",
    "import matplotlib.pyplot as plt\n",
    "%matplotlib inline\n",
    "plt.rcParams['figure.figsize'] = [10, 5]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Introduction\n",
    "In the history of the United Kingdom, while Romantic poetry had been the dominant genre, it was the novel that was most important in the Victorian period, from 1837 to 1901. It is known to all that Charles Dickens dominated the first part of Victoria's reign; William Thackeray's Vanity Fair appeared in 1848, and the three Brontë sisters, Charlotte, Emily and Anne, also published significant works in the 1840s. At the same period of time, Wilkie Collins published The Moonstone, known as the first detective novel. About two decades later, still in the Victorian era, Arthur Conan Doyle published the corpora of _Sherlock Holmes_, which is also the name of a famous detective with super-human characteristics in the UK. However, the sensibility of Doyle's writing is often regarded as Edwardian despite his works came out in the Victorian period. There might be some underlying associations and common features between the two famous detective novels since it is believed Arthur Conan Doyle was influenced by Wilkie Collins."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Firstly, open all the texts I will analyze and split some of them."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "response = requests.get('http://corpus-db.org/api/author/Doyle, Arthur Conan')\n",
    "response.ok\n",
    "parsed = json.loads(response.text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[('108.0', 'The Return of Sherlock Holmes'),\n",
       " ('126.0', 'The Poison Belt'),\n",
       " ('139.0', 'The Lost World'),\n",
       " ('221.0', 'The Return of Sherlock Holmes'),\n",
       " ('244.0', 'A Study in Scarlet'),\n",
       " ('290.0',\n",
       "  'The Stark Munro Letters: Being series of twelve letters written by J. Stark Munro, M.B., to his friend and former fellow-student, Herbert Swanborough, of Lowell, Massachusetts, during the years 1881-1884'),\n",
       " ('294.0', 'The Captain of the Polestar, and Other Tales'),\n",
       " ('355.0', 'The Parasite: A Story'),\n",
       " ('356.0', 'Beyond the City'),\n",
       " ('423.0', 'Round the Red Lamp: Being Facts and Fancies of Medical Life'),\n",
       " ('439.0', 'The Vital Message'),\n",
       " ('537.0', 'Tales of Terror and Mystery'),\n",
       " ('834.0', 'The Memoirs of Sherlock Holmes'),\n",
       " ('903.0', 'The White Company'),\n",
       " ('1638.0', 'The New Revelation'),\n",
       " ('1644.0', 'The Adventures of Gerard'),\n",
       " ('1661.0', 'The Adventures of Sherlock Holmes'),\n",
       " ('2097.0', 'The Sign of the Four'),\n",
       " ('2343.0', 'The Adventure of Wisteria Lodge'),\n",
       " ('2344.0', 'The Adventure of the Cardboard Box'),\n",
       " ('2345.0', 'The Adventure of the Red Circle'),\n",
       " ('2346.0', 'The Adventure of the Bruce-Partington Plans'),\n",
       " ('2347.0', 'The Adventure of the Dying Detective'),\n",
       " ('2348.0', 'The Disappearance of Lady Frances Carfax'),\n",
       " ('2349.0', \"The Adventure of the Devil's Foot\"),\n",
       " ('2350.0', 'His Last Bow: An Epilogue of Sherlock Holmes'),\n",
       " ('2845.0', 'Sir Nigel'),\n",
       " ('2852.0', 'The Hound of the Baskervilles'),\n",
       " ('3069.0', 'The Great Boer War'),\n",
       " ('3070.0', 'The Hound of the Baskervilles'),\n",
       " ('3289.0', 'The Valley of Fear'),\n",
       " ('3776.0', 'The Valley of Fear'),\n",
       " ('4295.0', 'Songs of Action'),\n",
       " ('5148.0', 'Rodney Stone'),\n",
       " ('5260.0', 'A Duet, with an Occasional Chorus'),\n",
       " ('5317.0', 'Through the Magic Door'),\n",
       " ('7964.0', 'The Mystery of Cloomber'),\n",
       " ('8394.0', 'The Doings of Raffles Haw'),\n",
       " ('8727.0', 'The Last Galley; Impressions and Tales'),\n",
       " ('9504.0',\n",
       "  'Micah Clarke: His Statement as made to his three grandchildren Joseph,; Gervas and Reuben During the Hard Winter of 1734'),\n",
       " ('9874.0', 'A Visit to Three Fronts: June 1916'),\n",
       " ('10446.0', 'The Green Flag, and Other Stories of War and Sport'),\n",
       " ('10581.0', 'Uncle Bernac: A Memory of the Empire'),\n",
       " ('11247.0', 'The Exploits of Brigadier Gerard'),\n",
       " ('11413.0', 'The Refugees: A Tale of Two Continents'),\n",
       " ('11656.0', 'The Great Shadow and Other Napoleonic Tales'),\n",
       " ('12555.0', 'The Tragedy of the Korosko'),\n",
       " ('13152.0', 'The Firm of Girdlestone'),\n",
       " ('13734.0', 'Jim Harrison, boxeur'),\n",
       " ('13735.0', 'La grande ombre'),\n",
       " ('13795.0', 'Nouveaux mystères et aventures'),\n",
       " ('14254.0', 'Enoni: muistoja Napoleonin ajoilta'),\n",
       " ('15949.0', 'Le Horror Altissime = The Horror of the Heights'),\n",
       " ('17398.0', \"The Cabman's Story: The Mysteries of a London 'Growler'\"),\n",
       " ('18716.0', 'Micah Clarke - Tome I: Les recrues de Monmouth'),\n",
       " ('18717.0', 'Micah Clarke - Tome II: Le Capitaine Micah Clarke'),\n",
       " ('18718.0', 'Micah Clarke - Tome III: La Bataille de Sedgemoor'),\n",
       " ('21768.0', 'A Desert Drama: Being The Tragedy Of The \"Korosko\"'),\n",
       " ('21769.0', 'Songs Of The Road'),\n",
       " ('22357.0', 'Danger! and Other Stories'),\n",
       " ('23059.0', 'My Friend The Murderer'),\n",
       " ('24951.0', 'The War in South Africa, Its Cause and Conduct'),\n",
       " ('26153.0', 'The Last of the Legions and Other Tales of Long Ago'),\n",
       " ('29392.0', 'Etienne Gerards Bedrifter'),\n",
       " ('29490.0', 'De dood van Sherlock Holmes — De terugkeer van Sherlock Holmes'),\n",
       " ('30933.0', 'Sherlock Holmes: De Agra-Schat'),\n",
       " ('32536.0', 'Baskervillen koira'),\n",
       " ('32777.0',\n",
       "  'The Great Keinplatz Experiment and Other Tales of Twilight and the Unseen'),\n",
       " ('34079.0', \"Tajemnica Baskerville'ów: dziwne przygody Sherlocka Holmes\"),\n",
       " ('34627.0', 'The Dealings of Captain Sharkey, and Other Tales of Pirates'),\n",
       " ('34797.0', 'The Man from Archangel, and Other Tales of Adventure'),\n",
       " ('36050.0', 'Rodney Stone'),\n",
       " ('36453.0', 'La guardia blanca: novela histórica escrita en inglés'),\n",
       " ('37712.0', 'The Crime of the Congo'),\n",
       " ('38071.0', 'The Guards Came Through, and Other Poems'),\n",
       " ('38443.0', 'The Croxley Master: A Great Tale Of The Prize Ring'),\n",
       " ('39718.0', 'The Wanderings of a Spiritualist'),\n",
       " ('40848.0', 'The Gully of Bluemansdyke, and Other stories'),\n",
       " ('42127.0', 'The German War'),\n",
       " ('45335.0', \"Toisen tahran tarina: Ym. Sherlock Holmes'in seikkailuja\"),\n",
       " ('47506.0', 'The Coming of the Fairies'),\n",
       " ('48320.0', 'Adventures of Sherlock Holmes: Illustrated'),\n",
       " ('49584.0', 'Napoleonin sotilaan seikkailut'),\n",
       " ('49702.0', 'Uusi katakombi ja muita kertoelmia'),\n",
       " ('51818.0', 'Kadonnut maailma'),\n",
       " ('52099.0', 'Neljän merkit'),\n",
       " ('52253.0', 'Vainottu: Romaani'),\n",
       " ('52677.0', 'Kauhun laakso 1: Murhenäytelmä Birlstonen kartanossa'),\n",
       " ('52678.0', 'Kauhun laakso 2: Salaseuralaiset'),\n",
       " ('54109.0', 'Round the Fire Stories'),\n",
       " ('54158.0', 'Myrkkyvyöhyke')]"
      ]
     },
     "execution_count": 98,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "[(item['id'],item['title']) for item in parsed]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def getFullText(bookID): \n",
    "    response = requests.get('http://corpus-db.org/api/id/' + bookID + '/fulltext')\n",
    "    if response.ok: \n",
    "        print('Got full text for ' + bookID)\n",
    "        parsed = json.loads(response.text)\n",
    "        if len(parsed)>0 and 'text' in parsed[0]: \n",
    "            return parsed[0]['text']\n",
    "    else: \n",
    "        print('Response came back bad: ' + response.status)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Got full text for 3070.0\n",
      "Got full text for 1661.0\n"
     ]
    }
   ],
   "source": [
    "Hound = getFullText('3070.0')# The Hound of the Baskervilles, one of the most famous novella of Sherlock Holmes\n",
    "AdvtuHolmes = getFullText('1661.0')#The Adventures of Sherlock Holmes, story collection related by Watson"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "moonstone = open('moonstone.md', encoding = \"UTF-8\").read()\n",
    "moonstoneParts = moonstone.split('%%%%%')\n",
    "clack = moonstoneParts[2]\n",
    "bruff = moonstoneParts[4]\n",
    "dubliners = open('dubliners.md', encoding = \"UTF-8\").read()\n",
    "gardenparty = open('garden-party.md', encoding =\"UTF-8\").read()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Uncertainty of A Text "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "There are many features of a text. Uncertainty is a feature which is easy to analyze by computer."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Hypothesis 1: \n",
    "It is highly possible that the uncertainty of detective novels is higher than that of other genres."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "In order to know the uncertainty of a text, I will measure it by calculating the frequency of 'may'. Here is a function to calculate the frequency of 'may' in a text."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def mayFrequency(text):\n",
    "    textTokens= word_tokenize(text)\n",
    "    textTokensLower = [token.lower() for token in textTokens]\n",
    "    CountMay = Counter(textTokensLower)['may']\n",
    "    return CountMay/len(textTokens)*100"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "Corpus = [gardenparty, dubliners, moonstone, Hound, AdvtuHolmes]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 104,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "TextmayFrequency = [mayFrequency(text) for text in Corpus]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "frequencies = pd.DataFrame(TextmayFrequency, columns = [\"Frequency of 'may'\"],\n",
    "                          index = ['The Garden Party', 'Dubliners', 'The Moonstone', 'The Hound Of The Baskervilles', 'The Adventures Of Sherlock Holmes'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Frequency of 'may'</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>The Garden Party</th>\n",
       "      <td>0.012108</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Dubliners</th>\n",
       "      <td>0.032230</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>The Moonstone</th>\n",
       "      <td>0.111124</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>The Hound Of The Baskervilles</th>\n",
       "      <td>0.145351</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>The Adventures Of Sherlock Holmes</th>\n",
       "      <td>0.155153</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                   Frequency of 'may'\n",
       "The Garden Party                             0.012108\n",
       "Dubliners                                    0.032230\n",
       "The Moonstone                                0.111124\n",
       "The Hound Of The Baskervilles                0.145351\n",
       "The Adventures Of Sherlock Holmes            0.155153"
      ]
     },
     "execution_count": 106,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "frequencies"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x24060eb8d68>"
      ]
     },
     "execution_count": 107,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAl0AAAHcCAYAAADshh/LAAAABHNCSVQICAgIfAhkiAAAAAlwSFlz\nAAALEgAACxIB0t1+/AAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDIuMi4yLCBo\ndHRwOi8vbWF0cGxvdGxpYi5vcmcvhp/UCwAAIABJREFUeJzt3Xm8XVV9///Xm4QZQYixRaYEZAoS\nGZI4UBFBEX5VcACBUgcqRb8WbfGrLbYOFIevs6jla8ECCmqBatWotCAqomg1YSiQMkVEE9GvYRAD\nMgU+vz/OSbhcbpJzk3v3Pif39Xw88sjZa+9zzudywr3vu9baa6WqkCRJ0vhar+0CJEmSJgJDlyRJ\nUgMMXZIkSQ0wdEmSJDXA0CVJktQAQ5ckSVIDDF2SJEkNMHRJkiQ1wNAlSZLUgMltFzDcU57ylJo2\nbVrbZUiSJK3WlVdeeUdVTe3l2r4LXdOmTWP+/PltlyFJkrRaSX7R67U9DS8mOSTJTUkWJjl5hPP7\nJ7kqybIkRww7t32SS5LckOR/kkzrtThJkqR1xWpDV5JJwOnAocAM4JgkM4Zd9kvgdcCXRniJc4GP\nVNXuwBzgt2tTsCRJ0iDqZXhxDrCwqm4FSHI+cDjwP8svqKrbuuceHfrEbjibXFXf7l5379iULUmS\nNFh6CV3bAIuGHC8GntXj6+8C/C7JvwPTgUuBk6vqkaEXJTkBOAFg++23f8KLPPzwwyxevJgHHnig\nx7fVumqjjTZi2223Zf3112+7FEmSRqWX0JUR2moUr/88YG86Q5AX0BmGPOtxL1Z1JnAmwKxZs57w\n2osXL+ZJT3oS06ZNIxmpHE0EVcWdd97J4sWLmT59etvlSJI0Kr1MpF8MbDfkeFvg9h5ffzFwdVXd\nWlXLgK8B+4yuRHjggQeYMmWKgWuCS8KUKVPs8ZQkDaReQtc8YOck05NsABwNzO3x9ecBWyZZvn7F\ngQyZCzYaBi6B/w4kSYNrtaGr20N1InAxcANwYVUtSHJqksMAksxOshg4EjgjyYLucx8B3gZ8J8l1\ndIYqPzs+X4okSVL/6mlx1Kq6CLhoWNu7hzyeR2fYcaTnfhuYuRY1PsG0k781li/HbR/809VeM2nS\nJPbcc88Vx1/72teYCCvnH3PMMSxYsIDjjjuOk046aUX7KaecwrRp03jd6143bu89bdo0brvttnF7\nfUmSmtR3K9L3q4033phrrrlmpeeXLVvG5Mnr1n/O3/zmN/zoRz/iF7/oebFdSZK0Em54vRY+97nP\nceSRR/LSl76Ugw8+GICPfOQjzJ49m5kzZ/Ke97xnxbXvf//72XXXXXnhC1/IMcccw0c/+lEADjjg\ngBXbHt1xxx0res8eeeQR3v72t694rTPOOAOAyy67jAMOOIAjjjiC3XbbjWOPPZaqzg2f8+bN47nP\nfS7PfOYzmTNnDkuXLuV5z3ve48Lifvvtx7XXXvu4r+OBBx7guOOOY88992Tvvffme9/7HgAHH3ww\nv/3tb9lrr734wQ9+8LjnbLbZZmy88cYrvoaTTjqJ/fffn91335158+bxile8gp133pl3vvOdK57z\nspe9jH333Zc99tiDM888E4CzzjrrcT1on/3sZ3nrW98KwNSpPW1lJUnSQFi3umbG0f33389ee+0F\nwPTp0/nqV78KwI9//GOuvfZattpqKy655BJuueUWfvrTn1JVHHbYYVx++eVsuummnH/++Vx99dUs\nW7aMffbZh3333XeV73fWWWexxRZbMG/ePB588EH222+/FcHu6quvZsGCBTztaU9jv/3244orrmDO\nnDkcddRRXHDBBcyePZvf//73bLzxxhx//PF87nOf47TTTuPmm2/mwQcfZObMx4/2nn766QBcd911\n3HjjjRx88MHcfPPNzJ07l5e85CUj9vC97W1ve9zxBhtswOWXX84nP/lJDj/8cK688kq22mordtpp\nJ0466SSmTJnC2WefzVZbbcX999/P7NmzeeUrX8nRRx/NzJkz+fCHP8z666/POeecsyJgzps3bw0+\nKUnS6oz1NJ1+08u0oTYYunq0suHFF73oRWy11VYAXHLJJVxyySXsvffeANx7773ccsstLF26lJe/\n/OVssskmABx22GGrfb9LLrmEa6+9li9/+csA3HPPPdxyyy1ssMEGzJkzh2237Uyh22uvvbjtttvY\nYost2HrrrZk9ezYAm2++OQBHHnkk733ve/nIRz7C2WefPeIcrB/+8Ie8+c1vBmC33XZjhx124Oab\nb17xGr1Y/jXtueee7LHHHmy99dYA7LjjjixatIgpU6bwqU99akVYXbRoEbfccgvPfvazOfDAA/nm\nN7/J7rvvzsMPP/y4uXOSJK0rDF1radNNN13xuKp4xzvewRve8IbHXXPaaaetdKmDyZMn8+ijnd2T\n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\n",
      "text/plain": [
       "<Figure size 720x360 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "frequencies.plot(kind=\"bar\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Conclusion 1:\n",
    "According to the plot of the result above, the frequency of 'may' in _The Moonstone_ and _Sherlock Holmes_ is much higher than that in _Dubliners_ and _The Garden Party_, which is about 10 times of other types of stories. _The Moonstone_ and _Sherlock Holmes_ both belong to detective genre while _Dubliners_ and _The Garden Party_ are not. According to the frequency of 'may', I can draw the conclusion that the uncertainty of detective novels or story collections is much higher than that of other genres, which conforms to the hypothesis we made before. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## A Comparative Stylometry of _The Moonstone_, _Sherlock Holmes_ and Other Genres of Literature"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Uncertainty is one of the features of a text. And the technique of 'TfidfVectorize' can capture a large number of features of a text, not necessarily including uncertainty, to compare the stylometry of texts."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The function of the codes below is to measure how similar _The Moonstone_, by Wilkie Collins, and _The Hound of the Baskervilles_, one of the most famous novellas of _Sherlock Holmes_ corpus, and _The Adventures of Sherlock Holmes_, a story collection, and _Dubliners_ and _The Garden Party_, which are as references."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Hypothesis 2：\n",
    "_The Hound of the Baskervilles_ and _The Adventures of Sherlock Holmes_ should be the most similar because they both belong to the same corpus. And _The Moonstone_ should be more similar to _Sherlock Holmes_ than the other two novels because _The Moonstone_ and _Sherlock Holmes_ are both detective novels."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "tfidf = TfidfVectorizer(use_idf=False, max_features=500)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "I put labels on all the points I am going to create in the plot."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "CorpusLabel = ['The Garden Party', 'Dubliners', 'The Moonstone', 'The Hound of the Baskervilles', 'The Adventures of Sherlock Holmes']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "allTf = tfidf.fit_transform(Corpus).todense()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(5, 500)"
      ]
     },
     "execution_count": 111,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "allTf.shape"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now reduce the number of dimensions in that matrix from 500 to 2, so that we can plot it easier and see the relationships easier: "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 112,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "pca = PCA(2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 113,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "matrix([[ 0.00179581,  0.        ,  0.01755906, ...,  0.0091786 ,\n",
       "          0.01935487,  0.00239442],\n",
       "        [ 0.00091842,  0.        ,  0.0197461 , ...,  0.01699083,\n",
       "          0.0078066 ,  0.00168378],\n",
       "        [ 0.00156746,  0.00820305,  0.01818257, ...,  0.00663559,\n",
       "          0.03699212,  0.00376191],\n",
       "        [ 0.00495292,  0.        ,  0.01926136, ...,  0.00385227,\n",
       "          0.03283604,  0.00366883],\n",
       "        [ 0.00329194,  0.        ,  0.01784021, ...,  0.00860153,\n",
       "          0.04205193,  0.00446005]])"
      ]
     },
     "execution_count": 113,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "allTf"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 114,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "pcaOut = pca.fit_transform(allTf)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 115,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAApkAAAEyCAYAAACxnMviAAAABHNCSVQICAgIfAhkiAAAAAlwSFlz\nAAALEgAACxIB0t1+/AAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDIuMi4yLCBo\ndHRwOi8vbWF0cGxvdGxpYi5vcmcvhp/UCwAAIABJREFUeJzt3Xl4VeW59/HfTRBIQUEFFUEl9FAR\nMmxImIqMwQAvk0UpUKqgVURBfOFUxaMoR2v1HLnqgLbWocBxgBRQwaOvIAqCEyVARFGQQZRJmZEp\nSJL7/SObbQKZICsTfD/Xta+917OeZ6372Su1P9baa29zdwEAAABBqlLeBQAAAOD0Q8gEAABA4AiZ\nAAAACBwhEwAAAIEjZAIAACBwhEwAAAAEjpAJAACAwBEyAQAAEDhCJgAAAAJXtbwLOBV169b1Ro0a\nlXcZAAAARVq2bNlOd69X3nWUtUoZMhs1aqS0tLTyLgMAAKBIZvZteddQHrhcDgAAgMARMgEAABA4\nQiYAAAACR8gEAABA4AiZAAAACBwhEwAAAIEjZCJQu3btUigUUigU0kUXXaQGDRooFAqpTp06atas\n2Slvd8qUKTIzvffee5G2119/XWammTNnBlF6oTZu3KhXX3211PcDAMDpgpCJQJ1//vlKT09Xenq6\nRowYoTFjxkSWq1Qp2Z9bXFycpk2bFlmePn26EhISSlpysRAyAQA4OYRMlJmsrCzdfPPNat68uVJS\nUnT48GFJ0vr169WjRw8lJiaqQ4cOWr16db7jO3TooH/96186evSoDhw4oHXr1ikUCkXWv/fee2rR\nooXi4uJ044036siRI4W2N2rUSA888IBatmypuLi4yH4/+OCDyNnYFi1aaP/+/Ro3bpwWL16sUCik\nxx9/XBkZGbrhhhsUFxenFi1aaMGCBZJyzrj2799fPXr0UJMmTXTXXXdF6ps3b57atWunli1basCA\nATpw4EDwbzIAABUEIRNlZu3atRo5cqRWrVqlOnXqaNasWZKk4cOHa9KkSVq2bJkmTpyo2267Ld/x\nZqZu3bpp7ty5mj17tvr27RtZl5GRoWHDhik1NVWff/65MjMz9be//a3A9mPq1q2r5cuX69Zbb9XE\niRMlSRMnTtQzzzyj9PR0LV68WNHR0Xr00UfVoUMHpaena8yYMXrmmWckSZ9//rmmTZumoUOHKiMj\nQ5KUnp4e2V9qaqo2bdqknTt36k9/+pPmz5+v5cuXKykpSX/5y19K5X0GAKAiIGQiEG9teEspM1MU\nPzVeKTNT9NaGt07oExMTEznzmJiYqI0bN+rAgQP6+OOPNWDAAIVCId1yyy3atm1bgfsZNGiQpk+f\nrunTp2vw4MGR9jVr1igmJka/+tWvJElDhw7VokWLCmw/pn///nnqkaT27dtr7Nixeuqpp7R3715V\nrXrir69++OGHuu666yRJTZs21WWXXaavv/5akpScnKzatWurRo0aatasmb799lt9+umn+vLLL9W+\nfXuFQiFNnTpV3357Rv7KGADgDFEpf7scFctbG97ShI8nKCMr50zetoPbNOHjCWqyp4la1moZ6Ve9\nevXI66ioKB0+fFjZ2dmqU6eO0tPTi7Wv1q1b64svvlB0dHQkOEqSu+fbv6D242uKiopSZmamJGnc\nuHHq1auX3n77bbVt21bz588/qe0eP8/MzEy5u6666qo8nykFAOB0xplMlNiTy5+MBMxjMrIytGTb\nkiLHnnPOOYqJidGMGTMk5YS3zz77rNAxjzzyiP785z/naWvatKk2btyodevWSZJeeuklderUqcD2\nwqxfv15xcXG6++67lZSUpNWrV+vss8/W/v37I306duyoV155RZL09ddf67vvvtPll19e4Dbbtm2r\njz76KFLHoUOHImc+AQA4HREyUWLfH/w+3/YDPxXvxpZXXnlFL774ohISEtS8eXPNnj270P49e/ZU\nly5d8rTVqFFDkydP1oABAxQXF6cqVapoxIgRBbYX5oknnlBsbKwSEhIUHR2tnj17Kj4+XlWrVlVC\nQoIef/xx3XbbbcrKylJcXJwGDhyoKVOm5DmDebx69eppypQpGjx4sOLj49W2bdsCb3ACAOB0YEVd\nTqyIkpKSPC0trbzLQFjKzBRtO3ji5yjr16yvedfOK4eKAACoOMxsmbsnlXcdZY0zmSixO1reoRpR\nNfK01YiqoTta3lFOFQEAgPLGjT8osV6Ne0nK+Wzm9we/10U1L9IdLe+ItAMAgDMPIROB6NW4F6ES\nAABEcLkcAAAAgSNkAgAAIHCETABAqYmKilIoFFLz5s2VkJCgv/zlL8rOzi5yXK1atfJtHzZsmGbO\nnClJuummm/Tll18GWi+A4PCZTABAqYmOjo78otf27dv1u9/9Tvv27dN//ud/lnjbL7zwQom3IUmZ\n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\nsrJ05513qlWrVoqPj9ff//53STln6zp37qxrr71WTZs21ZAhQ+Tueuqpp7R161Z16dIlcvYw95m3\nmTNnatiwYZF9jB07Vl26dNHdd9+tgwcP6sYbb1SrVq3UokULzZ6d8zsBq1atUuvWrRUKhRQfH6+1\na9eeMN9p06YpLi5OsbGxuvvuuyVJDz74oD788EONGDFCd955Z57+27ZtU/369SNhvmHDhjr33HMj\n6++9914lJCSobdu2+uGHHyRJO3bs0DXXXKNWrVqpVatW+uijjyTlnCUcPny4UlJSdP311+fZz+7d\nu3X11VcrPj5ebdu21cqVKyVJBw4c0A033KC4uDjFx8dr1qxZecbt3LlT7dq101tvvZXP0S3Yt99+\nq+TkZMXHxys5OVnffffdCX06d+6sMWPGqGPHjrriiiu0dOlS9e/fX02aNNF9990X6ffyyy9H3vdb\nbrlFWVlZysrK0rBhwyJngB9//PGTqg8AUMG5e6V7JCYmOgr2wAMP+GOPPebu7t98841HRUX5ihUr\n3N19wIAB/tJLL7m7e9euXf3rr792d/dPP/3Uu3Tpku/2kpOTfdGiRb5mzRqPi4uLtPfp08enTp3q\n7u5PP/2016xZ093dX3vtNb/++uvd3f3IkSPesGFDP3TokP/973/3hx56yN3dMzIyPDEx0Tds2OAL\nFizwc845xzdt2uRZWVnetm1bX7x4sbu7X3bZZb5jx47IPo/tw919xowZPnToUHd3Hzp0qPfq1csz\nMzPd3f2ee+6JzHPPnj3epEkTP3DggI8aNcpffvnlSG2HDh3KM9ctW7b4JZdc4tu3b/ejR496ly5d\n/PXXX3d3906dOvnSpUtPeH82bdrkl112mSckJPjYsWN9+fLlkXWSfM6cOe7ufuedd0bmP3jw4Mgc\nv/32W2/atGnk2LVs2TJS14IFC7xXr17u7j5q1CifMGGCu7u/9957npCQ4O7ud911l99xxx2Rfe7e\nvTvyXn3//ffeunVrnzdv3gl1u7tXqVLFExISIo9LLrnER44c6e7uvXv39ilTpri7+4svvuj9+vWL\n1Hjs76tTp05+1113ubv7E0884fXr1/etW7d6RkaGN2jQwHfu3Olffvml9+7d23/66Sd3d7/11lt9\n6tSpnpaW5t26dYvUsmfPnnxrBIDKTlKaV4D8VNaPIn+7HJVfTEyMQqGQJCkxMVEbN27UgQMH9PHH\nH2vAgAGRfkeOHDlh7A8//KB169bpyiuvlJmpatWq+uKLLxQbG6uPPvooctbsuuuui5z169mzp0aP\nHq0jR47onXfeUceOHRUdHa158+Zp5cqVmjlzpiRp3759Wrt2rapVq6bWrVurYcOGkqRQKKSNGzfq\nyiuvPKl5DhgwQFFRUZKkefPmac6cOZHPDmZkZOi7775Tu3bt9PDDD2vz5s2RM265LV26VJ07d1a9\nevUkSUOGDNGiRYt09dVXF7jfhg0bas2aNXr//ff1/vvvKzk5WTNmzFBycrKqVasW+UxlYmKi3n33\nXUnS/Pnz9eWXX0a28eOPP2r//v2SpL59+yo6OvqE/Xz44YeR97tr167atWuX9u3bp/nz5+c5w3zs\nLOrRo0eVnJysZ555Rp06dcq39ujoaKWnp0eWp0yZomM/dPDJJ5/otddek5RzfO+66658t9G3b19J\nUlxcnJo3b6769etLkho3bqxNmzbpww8/1LJly9SqVStJ0uHDh3XBBReoT58+2rBhg26//Xb16tVL\nKSkpBb7HAIDKh5BZyX295Ht9Mnu9Duw+olrnVVe7fr88oU/16tUjr6OionT48GFlZ2erTp06eQJG\nflJTU7Vnzx7FxMRIyglD06dP15/+9CdJkpmdMKZGjRrq3Lmz5s6dq9TUVA0ePFhSzlnzSZMmqXv3\n7nn6L1y48IQaC/o8Yu79ZWRk5FlXs2bNyGt316xZs3T55Zfn6XPFFVeoTZs2euutt9S9e3e98MIL\n6tq1a55xp6J69erq2bOnevbsqQsvvFBvvPGGkpOTddZZZ0Vqzj2v7OxsffLJJ/mGydzzyC2/2sxM\n7p7vcahataoSExM1d+7cAkPmychvH9LPf19VqlTJcxyrVKmizMxMubuGDh2qRx555ISxn332mebO\nnatnnnlG//znP/WPf/yjxHUCACoGPpNZiX295HsteGW1DuzOOQN5YPcRLXhltXZtPlDk2HPOOUcx\nMTGaMWOGpJwA89lnn53Qb9q0aXrnnXe0ceNGbdy4UcuWLYucNWvfvn3k9SuvvJJn3KBBgzR58mQt\nXrw4Eiq7d++uv/3tbzp69GhO/V9/rYMHDxZa59lnnx05wydJF154ob766itlZ2fr9ddfL3Bc9+7d\nNWnSpEgwW7FihSRpw4YNaty4sUaPHq2+fftGPtd4TJs2bfTBBx9o586dysrK0rRp04oMaMuXL9fW\n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\n5syJfH4yIyND3333nSTpqquu0nnnnSdJ6tmzp0aPHq0jR47onXfeUceOHRUdHV3k3AubZ/v27TVs\n2DD99re/Vf/+/Yv/hgIAUEkRMguw7803tW38/fKMDElS5tat2jb+fmVc0VS1EhMj/apXrx55HRUV\npcOHDys7O1t16tRRenr6Ke8/5x8++TOzyOuMcH351ZN7G7nHlKag3g8zU58+fTRp0iSNGzdOt99+\nu8aOHau+fftq4cKFmjBhgqScS/a9evXS22+/rbZt22r+/PmSpPr16ysjI0MrVqyIhEx316xZs3T5\n5Zfn2deSJUtUs2bNyHKNGjXUuXNnzZ07V6mpqRo8eHCxai5sns8++6yWLFmit956S6FQSOnp6Tr/\n/POL/X4AAFDZ8JnMAmx//IlIwDzGMzJ08NNPixx7zjnnKCYmRjNmzMgZ567PPvvspPbfpk0bffDB\nB9q5c6eysrI0bdq0yFnGCy+8UF999ZWys7P1+uuvF7mtjh07avr06crKytK2bdu0YMGCE/rUrl1b\n5557rhYvXixJeumllyL7K8xZZ52lo0ePFtrnVN+PDz/8MHKj0b59+9SgQQNJ0tSpUyN91q9fr7i4\nON19991KSkqKfAayTp06euutt/Qf//EfWrhwoSSpe/fumjRpUiR8r1ixosB9Dxo0SJMnT9bixYvV\nvXv3Imstap7r169XmzZt9OCDD6pu3bratGlTsbYJACiZ0vqGGEl655131Lp1azVt2lShUEgDBw6M\nXCE7VWa20czqlmgjOdsZZmY7zCzdzL40s5tPcnwjM/tdSWogZBYgc9u2fNuz9x8o1vhXXnlFL774\nohISEtS8efPITSbFVb9+fT3yyCPq0qWLEhIS1LJlS/Xr10+S9Oijj6p3797q2rWr6tevX+S2fvOb\n36hJkyaKi4vTrbfeWmB4nDp1qu68807Fx8crPT1d999/f5HbHj58uOLj4yM3/hSkuO9HamqqQqGQ\n4uPjtWLFCo0fP15SztcEDRgwQB06dFDduj//b++JJ56I3FATHR2tnj17RtZdeOGFevPNNzVy5Egt\nWbJE48eP19GjRxUfH6/Y2NjItvOTkpKiRYsWqVu3bqpWrVqR70NR87zzzjsjN3F17NhRCQkJxd4m\nAODUldY3xHzxxRe6/fbbNXXqVK1evVrp6ekaMmSINm7cWOxtmFlpX1FOdfeQpM6S/mxmFxZnULiu\n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\n",
      "text/plain": [
       "<Figure size 720x360 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "xs, ys = pcaOut[:,0], pcaOut[:,1]\n",
    "for i in range(len(xs)): \n",
    "    plt.scatter(xs[i], ys[i])\n",
    "    plt.annotate(CorpusLabel[i], (xs[i], ys[i]))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Conclusion 2:\n",
    "According to the plot above, the two books belonging to the corpus of _Sherlock Holmes_ are the most similar. As expected, _Sherlock Holmes_ is more similar to _The Moonstone_ than _Dubliners_ and _The Garden Party_, which are as references. The result conforms to the hypothesis."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## William Wilkie Collins's influence on _Sherlock Holmes_"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "_The Moonstone_ is known as the first detective novel. Sergeant Cuff, who appears in _The Moonstone_, is known as one of the best detectives in Britain and so is Sherlock Homles created by Conan Doyle.\n",
    "The two detectives, Cuff and Holmes, have similarities and differences. They both have some special hobbies. Cuff likes roses and Holmes uses drugs. Cuff is a great detective with great patience and resistance rather than superhuman gifts, while Sherlock Holmes reveals his knowledge of the criminal underworld of London, portraited as a genius."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Hypothesis 3: \n",
    "The probability is high that Arthur Conan Doyle was influenced by Wilkie Collins and borrowed some traits from the detectives Collins made in his books."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Since the data and plot showed above proves their works are more similar compared to other books, I will print out the context of some motifs to validate the hypothesis."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 116,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "moonstoneTokens = word_tokenize(moonstone)\n",
    "moonstoneText = Text(moonstoneTokens)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Wilkie Collins is an addict of opium because of it is a euphoria though it was viewed as a symbol of corruption and licentiousness in the UK at that time. So I display the context of 'opium' in his book using the technique of concordance, _The Moonstone_. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 117,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Displaying 25 of 45 matches:\n",
      " time . Sometimes they said he was given up to smoking opium and collecting old books ; sometimes he was reported t\n",
      "uable papers he possessed was by accepting a matter of opium as a matter of fact , my father was quite willing to t\n",
      "rs from my sentence of death . But even the virtues of opium have their limit . The progress of the disease has gra\n",
      "of the disease has gradually forced me from the use of opium to the abuse of it . I am feeling the penalty at last \n",
      " suppose . Have you ever been accustomed to the use of opium ? ” “ I never tasted it in my life. ” “ Were your nerv\n",
      " said , “ that you have never–to your knowledge–tasted opium in your life. ” “ To my knowledge , ” I repeated . “ Y\n",
      " Let us go on . You are not aware of ever having taken opium . At this time , last year , you were suffering from n\n",
      " took the Diamond , in a state of trance , produced by opium . Secondly , that the opium was given to you by Mr. Ca\n",
      "te of trance , produced by opium . Secondly , that the opium was given to you by Mr. Candy–without your own knowled\n",
      " the course of his practice . The ignorant distrust of opium ( in England ) is by no means confined to the lower an\n",
      " same position , physically and morally , in which the opium found you last year . In that case we may fairly hope \n",
      "se are active proceedings . I thought the influence of opium was first to stupefy you , and then to send you to sle\n",
      " then to send you to sleep. ” “ The common error about opium , Mr. Blake ! I am , at this moment , exerting my inte\n",
      "e said , “ are the far-famed CONFESSIONS OF AN ENGLISH OPIUM EATER ! Take the book away with you , and read it . At\n",
      " De Quincey had committed what he calls ‘ a debauch of opium , ’ he either went to the gallery at the Opera to enjo\n",
      "I am not answered yet as to the effect produced by the opium on myself. ” “ I will try to answer you in a few words\n",
      "n a few words , ” said Ezra Jennings . “ The action of opium is comprised , in the majority of cases , in two influ\n",
      " held the stone . In the spiritualised intoxication of opium , you would do all that . Later , as the sedative acti\n",
      " sleep . When the morning came , and the effect of the opium had been all slept off , you would wake as absolutely \n",
      "y remember , under the influence of the second dose of opium , the place in which you hid the Diamond under the inf\n",
      "the present , let us return to our experiment with the opium . We have decided that you leave off the habit of smok\n",
      "tten . Let Ezra Jennings tell how the venture with the opium was tried , and how it ended . # # Fourth Narrative Ex\n",
      "fter a dreadful night ; the vengeance of yesterday ’ s opium , pursuing me through a series of frightful dreams . A\n",
      "ed to think , yesterday , that our experiment with the opium was not likely to be viewed very favourably by some of\n",
      " present as one of the witnesses on the night when the opium is tried for the second time . Here , again , there is\n"
     ]
    }
   ],
   "source": [
    "moonstoneText.concordance('opium', width=115)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "From the context of 'opium', it is learned that Colonel used opium, so did Frankin Blake. And the effect of opium is harmful, some of them resulting in adverse consequences."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Sergeant Cuff seems to like roses. Let's see the context that surrounds 'roses'."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 118,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Displaying 22 of 22 matches:\n",
      " these . Grass , Mr. Gardener–grass walks between your roses ; gravel ’ s too hard for them . That ’ s a sweet pret\n",
      "o hard for them . That ’ s a sweet pretty bed of white roses and blush roses . They always mix well together , don \n",
      ". That ’ s a sweet pretty bed of white roses and blush roses . They always mix well together , don ’ t they ? Here \n",
      " out the thief who stole it ! “ You seem to be fond of roses , Sergeant ? ” I remarked . “ I haven ’ t much time to\n",
      "fondness to bestow , most times , Mr. Betteredge , the roses get it . I began my life among them in my father ’ s n\n",
      "ire from catching thieves , and try my hand at growing roses . There will be grass walks , Mr. Gardener , between m\n",
      "aracter . It reminded him , you see , of his favourite roses , and , as HE whistled it , it was the most melancholy\n",
      "is weekly account . The Sergeant got on the subject of roses and the merits of grass walks and gravel walks immedia\n",
      "them , head over ears in an argument on the growing of roses . The Sergeant was so deeply interested that he held u\n",
      "f boys . Knowing nothing whatever about the growing of roses , I steered a middle course–just as her Majesty ’ s ju\n",
      ", ” he said . “ And mind , if you ever take to growing roses , the white moss rose is all the better for not being \n",
      "rently meaning me ) , “ only understood the growing of roses he would be the most completely perfect character on t\n",
      " the Sergeant and the gardener were wrangling over the roses ) we two spent the interval before the news came back \n",
      ". Away they went together , fighting the battle of the roses without asking or giving quarter on either side . The \n",
      "I left , to surprise my aunt , among the geraniums and roses . The happy thought followed , “ Why not do the same f\n",
      " Dorking ; and he ’ s up to his eyes in the growing of roses . I have it in his own handwriting , Mr. Franklin . He\n",
      "r , before you knew it yourself . She used to give you roses to wear in your button-hole . Ah , Mr. Franklin , you \n",
      " in your button-hole . Ah , Mr. Franklin , you wore my roses oftener than either you or she thought ! The only comf\n",
      "as jealous of Rachel , confessing that she changed the roses , confessing that she saw a glimpse of hope for hersel\n",
      "out the last Sybarite years of his life , smothered in roses ! A decent elderly woman opened the gate to me , and a\n",
      "y one business now , sir , ” she said ; “ and that ’ s roses . Some great man ’ s gardener in Ireland has found out\n",
      "t have got from this , to the subject of his favourite roses , if my servant had not interrupted us by announcing t\n"
     ]
    }
   ],
   "source": [
    "moonstoneText.concordance('roses', width=115)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Seeing sentences or phrases like “You seem to be fond of roses, Sergeant ?”, \"the subject of his favourite roses\", we can conclude it is true that Cuff loves roses."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's see the context of 'opium' in _Sherlock Holmes_ and see what Sherlock Holmes loves."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 119,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "ScarletTokenText = Text(word_tokenize(Scarlet))\n",
    "AdvtuHolmesTokenText = Text(word_tokenize(AdvtuHolmes))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 120,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Displaying 11 of 11 matches:\n",
      " TWISTED LIP Isa Whitney , brother of the late Elias Whitney , D.D. , Principal of the Theological College of St. George 's , was much addicted to opium . The habit grew upon him , as I understand , from some foolish freak when he was at college ; for having read De Quincey 's description of his dr\n",
      "could bring him back to her ? It seems that it was . She had the surest information that of late he had , when the fit was on him , made use of an opium den in the farthest east of the City . Hitherto his orgies had always been confined to one day , and he had come back , twitching and shattered , \n",
      "and by the light of a flickering oil-lamp above the door I found the latch and made my way into a long , low room , thick and heavy with the brown opium smoke , and terraced with wooden berths , like the forecastle of an emigrant ship . Through the gloom one could dimly catch a glimpse of bodies ly\n",
      " . They could only have come from the old man at my side , and yet he sat now as absorbed as ever , very thin , very wrinkled , bent with age , an opium pipe dangling down from between his knees , as though it had dropped in sheer lassitude from his fingers . I took two steps forward and looked bac\n",
      " Whitney 's bill , led him out to the cab , and seen him driven through the darkness . In a very short time a decrepit figure had emerged from the opium den , and I was walking down the street with Sherlock Holmes . For two streets he shuffled along with a bent back and an uncertain foot . Then , g\n",
      "n neither collar nor necktie . `` Convinced that something was amiss with him , she rushed down the steps -- for the house was none other than the opium den in which you found me to-night -- and running through the front room she attempted to ascend the stairs which led to the first floor . At the \n",
      "ence of the missing gentleman 's clothes . `` So much for the Lascar manager . Now for the sinister cripple who lives upon the second floor of the opium den , and who was certainly the last human being whose eyes rested upon Neville St. Clair . His name is Hugh Boone , and his hideous face is one w\n",
      "with a reply to any piece of chaff which may be thrown at him by the passers-by . This is the man whom we now learn to have been the lodger at the opium den , and to have been the last man to see the gentleman of whom we are in quest . '' `` But a cripple ! '' said I . `` What could he have done si\n",
      "quiet and innocent one . There the matter stands at present , and the questions which have to be solved -- what Neville St. Clair was doing in the opium den , what happened to him when there , where is he now , and what Hugh Boone had to do with his disappearance -- are all as far from a solution a\n",
      "e . I distinctly saw his bare throat . '' `` Had he ever spoken of Swandam Lane ? '' `` Never . '' `` Had he ever showed any signs of having taken opium ? '' `` Never . '' `` Thank you , Mrs. St. Clair . Those are the principal points about which I wished to be absolutely clear . We shall now have \n",
      "wife knew that I had business in the City . She little knew what . `` Last Monday I had finished for the day and was dressing in my room above the opium den when I looked out of my window and saw , to my horror and astonishment , that my wife was standing in the street , with her eyes fixed full up\n"
     ]
    }
   ],
   "source": [
    "AdvtuHolmesTokenText.concordance('opium', width=300)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "It is interesting that the phrase, \"opium den\", appears frequently. As far as I know, it appears in _The Man with the Twisted Lip_ collected in _The Adventures of Sherlock Holmes_. Although whether Conan Doyle himself took up the \"pipe\" has remained undisclosed, he must have visited the opium den."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 121,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Displaying 3 of 3 matches:\n",
      " with his whole Bohemian soul , remained in our lodgings in Baker Street , buried among his old books , and alternating from week to week between cocaine and ambition , the drowsiness of the drug , and the fierce energy of his own keen nature . He was still , as ever , deeply attracted by the study\n",
      "tric , anatomy unsystematic , sensational literature and crime records unique , violin-player , boxer , swordsman , lawyer , and self-poisoner by cocaine and tobacco . Those , I think , were the main points of my analysis . '' Holmes grinned at the last item . `` Well , '' he said , `` I say now , \n",
      "himself out and burst into a hearty fit of laughter . `` I suppose , Watson , '' said he , `` that you imagine that I have added opium-smoking to cocaine injections , and all the other little weaknesses on which you have favoured me with your medical views . '' `` I was certainly surprised to find \n"
     ]
    }
   ],
   "source": [
    "AdvtuHolmesTokenText.concordance('cocaine', width=300)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 122,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Displaying 5 of 5 matches:\n",
      " Do you include violin-playing in your category of rows ? '' he asked , anxiously . `` It depends on the player , '' I answered . `` A well-played violin is a treat for the gods -- a badly-played one -- -- '' '' Oh , that 's all right , '' he cried , with a merry laugh . `` I think we may consider t\n",
      "nsystematic . 9 . Sensational Literature. -- Immense . He appears to know every detail of every horror perpetrated in the century . 10 . Plays the violin well . 11 . Is an expert singlestick player , boxer , and swordsman . 12 . Has a good practical knowledge of British law . When I had got so far i\n",
      "ch needs them all , '' I said to myself , `` I may as well give up the attempt at once . '' I see that I have alluded above to his powers upon the violin . These were very remarkable , but as eccentric as all his other accomplishments . That he could play pieces , and difficult pieces , I knew well \n",
      " his advice . When I returned with the pistol the table had been cleared , and Holmes was engaged in his favourite occupation of scraping upon his violin . `` The plot thickens , '' he said , as I entered ; `` I have just had an answer to my American telegram . My view of the case is the correct one\n",
      "tion . I left Holmes seated in front of the smouldering fire , and long into the watches of the night I heard the low , melancholy wailings of his violin , and knew that he was still pondering over the strange problem which he had set himself to unravel . CHAPTER VI . TOBIAS GREGSON SHOWS WHAT HE CA\n"
     ]
    }
   ],
   "source": [
    "ScarletTokenText.concordance('violin', width=300)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "From the context above, it is certain that Sherlock Holmes loves playing the violin a lot and sometimes he injects cocaine and smokes tobacco."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Conclusion 3:\n",
    "All these pieces of evidence increase the belief that there are some influences on Arthur Conan Doyle from Wilkie Collins."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##  Sentiment Analysis of Women Characters \n",
    "Sentiment analysis bases on TextBlob library for processing textual data."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "During the era of Victoria, women did not have the right to vote, sue, or own property. At the same time, the number of women participated in the paid workforce increased. In the last years of the Victorian era, feminist ideas spread among the educated middle classes and discriminatory laws were repealed. It is interesting to compare the sentiment of texts containing female to those without in detective novels written in that time."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Hypothesis 4：\n",
    "Female characters may be portrayed weaker than the male in detective novels during the period of Victoria. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 123,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "moonstoneSents = sent_tokenize(moonstone)\n",
    "clackSents = sent_tokenize(clack)\n",
    "AdvtuHolmesSents = sent_tokenize(AdvtuHolmes)\n",
    "dublinersSents = sent_tokenize(dubliners)\n",
    "HoundSents = sent_tokenize(Hound)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "This is a program to pick up sentences containing female ('she', 'her', 'hers', 'woman', 'women') from the whole text."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 124,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "Women = []\n",
    "noWomen = []\n",
    "for sent in moonstoneSents: \n",
    "    if ' she ' in sent or ' her ' in sent or ' hers ' in sent or ' woman ' in sent or ' women ' in sent: \n",
    "        Women.append(sent)\n",
    "    else: \n",
    "        noWomen.append(sent)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 125,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "Women0 = []\n",
    "for sent in clackSents: \n",
    "    if ' she ' in sent or ' her ' in sent or ' hers ' in sent or ' woman ' in sent or ' women ' in sent: \n",
    "        Women0.append(sent)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 126,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "clackWomen = ' '.join(Women0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 127,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "MoonstoneWomen = ' '.join(Women)\n",
    "MoonstoneNoWomen = ' '.join(noWomen)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 128,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "Women1 = []\n",
    "noWomen1 = []\n",
    "for sent in AdvtuHolmesSents: \n",
    "    if ' she ' in sent or ' her ' in sent or ' hers ' in sent or ' woman ' in sent or ' women ' in sent:\n",
    "        Women1.append(sent)\n",
    "    else: \n",
    "        noWomen1.append(sent)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 129,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "AdvtuHolmesWomen = ' '.join(Women1)\n",
    "AdvtuHolmesNoWomen = ' '.join(noWomen1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 130,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "Women2 = []\n",
    "noWomen2 = []\n",
    "for sent in dublinersSents: \n",
    "    if ' she ' in sent or ' her ' in sent or ' hers ' in sent or ' woman ' in sent or ' women ' in sent:\n",
    "        Women2.append(sent)\n",
    "    else: \n",
    "        noWomen2.append(sent)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 131,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "dublinersWomen = ' '.join(Women2)\n",
    "dublinersNoWomen = ' '.join(noWomen2)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The polarity score is a float within the range [-1.0, 1.0], from negative to positive.\n",
    "Let's test it by three interesting sentences first!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 132,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Sentiment(polarity=0.5, subjectivity=1.0)"
      ]
     },
     "execution_count": 132,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "testimonial0 = TextBlob(\"My final project is extremely awesome that everyone loves it.\")\n",
    "testimonial0.sentiment"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 133,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Sentiment(polarity=0.0, subjectivity=0.0)"
      ]
     },
     "execution_count": 133,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "testimonial1 = TextBlob(\"Mike Wallace is here!\")\n",
    "testimonial1.sentiment"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 134,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Sentiment(polarity=0.033333333333333326, subjectivity=0.6)"
      ]
     },
     "execution_count": 134,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "testimonial2 = TextBlob(\"I love California so much expecially cold Berkeley, but I have to leave tomorrow morning.\")\n",
    "testimonial2.sentiment"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "TextBlob cannot be always correct, for instance, it does not know Mike Wallace, but we can use it if the length of the text is big enough. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 135,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "SeveralTexts = [clackWomen, MoonstoneWomen, MoonstoneNoWomen, AdvtuHolmesWomen, AdvtuHolmesNoWomen, dublinersWomen, dublinersNoWomen]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 136,
   "metadata": {},
   "outputs": [],
   "source": [
    "SeveralBlobs = [TextBlob(text).sentiment\n",
    "            for text in SeveralTexts]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 137,
   "metadata": {},
   "outputs": [],
   "source": [
    "SeveralSentiments = [item.polarity\n",
    "                 for item in SeveralBlobs]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 138,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x2406101eba8>"
      ]
     },
     "execution_count": 138,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n0CVJktSB/wcu6WY8OKZBRAAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 720x360 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "pd.Series(SeveralSentiments, index=[\"clackWomen\", \"MoonstoneWomen\", \"MoonstoneNoWomen\", \"AdvtuHolmesWomen\", \"AdvtuHolmesNoWomen\", \"dublinersWomen\", \"dublinersNoWomen\"]).plot(kind='bar')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "### Conclusion 4:\n",
    "In _The Moonstone_, When Cuff was investigating the case, it is more often that Cuff talked to Betteredge, the house-steward rather than Mrs.Verinder. Mrs. Ablewhite, Rachel's aunt, was so upset that Rachel went back on the engagement. Rosanna Spearman, the poor servant, committed suicide silently. All these pieces of evidence implicate female status was lower than male in that era."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "In _Sherlock Holmes_, there are several female characters in different stories. Sherlock Holmes seems to have little interest in women in most times though he deals with women with gentleness and courtesy. There is one exception, Irene Adler, a character in _A Scandal in Bohemia_, collected in _The Adventures of Sherlock Holmes_ because she is the only woman who beat Sherlock in the battle of wits."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "It is known that there were both resistance and obedience of women during the Victorian era. Irene Adler in _Adventure of Sherlock Holmes_ could be an example that the social position of the female has been increasing."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "From the plot above, in _The Moonstone_, sentences containing women (\"she\", \"her\", \"hers\", \"woman\", \"women\") are less positive than those without, and that of the part of Miss Clack's narrative is even more negative compared with the whole text.\n",
    "The same thing happens in _The Adventures of Sherlock Holmes_. This might be another influence on Conan Doyle by Wilkie Collins. The result of _Dubliners_ is the opposite. Although the relative difference of the height of bars is not so big, it still shows that female characters are portrayed weaker in these two detective novels more and less."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Epilogue\n",
    "The method and the focus diversifies when a text is analyzed by human and computer. The result of the analysis cannot be always the same. However, it becomes more and more important to combine brain and computer when reading works of literature for synergy effect. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "In my project, hypotheses are based on reading by the human. Since computers are better to deal with long texts in a much shorter time, I calculated the frequency of 'may', plotted a comparative stylometry, displayed the context of some certain words and analyzed the sentiment using TextBlob, a library for processing textual data, by computer. With the help of computational literary analysis, people can develop a more profound understanding of literary works."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Work Cited"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Wordcount Function\n",
    "\n",
    "Please replace `Yourname-Final.ipynb` with the filename of this notebook. For instance, if my name is Jonathan, and I've renamed this notebook to `Jonathan-Final.ipynb`, I'd change `filename = 'Yourname-Final.ipynb'` below to `filename = 'Jonathan-Final.ipynb`. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 142,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total words: 1508\n"
     ]
    }
   ],
   "source": [
    "filename = 'Bo Zhao-Final.ipynb'\n",
    "\n",
    "if filename == 'Yourname-Final.ipynb': \n",
    "    raise ValueError(\"You forgot to change the filename above!\")\n",
    "\n",
    "with open('Bo Zhao-Final.ipynb', encoding='utf-8') as f:\n",
    "    nb = current.read(f, 'json')\n",
    "\n",
    "wordCount = 0\n",
    "\n",
    "for cell in nb.worksheets[0].cells:\n",
    "    if cell.cell_type == \"markdown\":\n",
    "        wordCount += len(cell['source'].replace('#', '').lstrip().split(' '))\n",
    "\n",
    "# This is the word count of my instructions. \n",
    "# My instructions obviously don't count toward the final word count, \n",
    "tare = 533\n",
    "\n",
    "wordCount = wordCount - tare\n",
    "\n",
    "print(\"Total words: {}\".format(wordCount))\n",
    "\n",
    "if wordCount < 1000: \n",
    "    raise Warning('Your paper has not yet met the minimum required length.')\n",
    "if wordCount > 2000: \n",
    "    raise Warning('Your paper has exceeded the maximum allowed length. Please edit for concision.')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
