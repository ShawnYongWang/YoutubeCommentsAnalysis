coef=0.01
import pandas as pd
import re
import xlsxwriter

import nltk
import re
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
from nltk.stem import WordNetLemmatizer


def getText():
	# read txt file
	df = pd.read_excel('comments.xlsx',usecols=[0])
	txt=df.values
	return txt

text=getText()



def getlikes():
	# read txt file
	df = pd.read_excel('comments.xlsx',usecols=[1])
	likes=df.values
	#print(likes[1][0])
	return likes
likes=getlikes()


#Training in part-of-speech tagging through Bush's speeches
train_text = state_union.raw("2005-GWBush.txt")
#raw_comments=open("comments.txt","r",encoding ="utf-8")
#cop=re.compile("[^,^\s^.^a-z^A-Z]")
#save_file = open('English_comments.txt', 'w',encoding ="utf-8")
#for line in raw_comments.readlines():
    #string = cop.sub("", line)
    #save_file.write(string)
#save_file.flush()
#save_file.close()
#sample_text=open("English_comments.txt","r",encoding ="utf-8").read()
custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
#tokenized = custom_sent_tokenizer.tokenize(sample_text)

def process_content():
    try:
        tag=[]
        for i in tokenized[:]:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
        return tag
    except Exception as e: 
        print(str(e))

#tag=process_content()




counts={}
line_count=0

#Generates a combination that preserves only letters and Spaces   
cop=re.compile("[^\s^a-z]")
#Generating restorer
lemmatizer = WordNetLemmatizer()

for sentence in text:
	words=sentence[0]
	
	# Convert all words to lowercase
	words=words.lower()
	# replace
	#for ch in '!@#$%:^&*()-.;,':
		#words=words.replace(ch," ")
	words = cop.sub("", words)
	sample_words=nltk.word_tokenize(words)
	tokenized = custom_sent_tokenizer.tokenize(words)
	#tagged = nltk.pos_tag(sample_words)
	for i in tokenized[:]:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
	for i in range(len(tagged)):
		#print(tagged[i][1])
		if tagged[i][1].startswith('NN'):
			#print('n')
			origin_word=lemmatizer.lemmatize(tagged[i][0],pos='n')
		elif tagged[i][1].startswith('VB'):
			origin_word=lemmatizer.lemmatize(tagged[i][0],pos='v')
		elif tagged[i][1].startswith('JJ'):
			origin_word=lemmatizer.lemmatize(tagged[i][0],pos='a')
		elif tagged[i][1].startswith('R'):
			origin_word=lemmatizer.lemmatize(tagged[i][0],pos='r')
		else: origin_word=tagged[i][0]
		#print(origin_word)
		if len(origin_word)<4:
			continue
		if origin_word in counts:
			counts[origin_word] = counts[origin_word]+coef*(likes[line_count][0])+1
		else:
			counts[origin_word]=coef*(likes[line_count][0])+1
	line_count+=1

items=list(counts.items())
# Sort by second column
items.sort(key=lambda x:x[1],reverse=True)
# Words and times of output frequency
with open('freqency_Semantic.txt','w',encoding ="utf-8") as f:
	for i in range (len(items)): 
		word,count=items[i]
		f.write("{0}：{1}".format(word,count)+'\n')

workbook = xlsxwriter.Workbook('frequency_Semantic.xlsx')
worksheet = workbook.add_worksheet()
for i in range(len(items)):
	word,count=items[i]
	worksheet.write(i, 0, word)  # Row I, column 0
	worksheet.write(i, 1, count) # Row I, column 1
 
workbook.close()
