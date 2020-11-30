from nltk.corpus import wordnet as wn
#print(wn.synsets('motorcar'))


from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
#words=['love','lovely','loves','loved','loving','lovingly']
#for i in words:
 #   print(lemmatizer.lemmatize(i))

from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

ps = PorterStemmer()
#example_words = ['love','lovely','loves','loved','loving','lovingly']
#example_words = ['trade', 'trading', 'trades', 'traded']
#example_words =['will',' ＇II', 'will', 'swo', 'willing', 'willed']
#for w in example_words:
#    print(ps.stem(w))




print(lemmatizer.lemmatize("love"))
print(lemmatizer.lemmatize("lovely", pos="a"))
print(lemmatizer.lemmatize("loves"))
print(lemmatizer.lemmatize("loved", pos="a"))
print(lemmatizer.lemmatize("loving", pos="a"))
print(lemmatizer.lemmatize("lovingly", pos="a"))
