##Step1 part of speech labeling
#step2 and word segmentation
#step3 speech merge

import nltk
import re
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
import pandas as pd
from nltk.stem import WordNetLemmatizer



##Start tagging the words of comments, and then categorize them

lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize('Americans',pos='n'))

from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
print(PorterStemmer().stem('loves'))
