coef=0.01
import pandas as pd
import re
import xlsxwriter
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize


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


counts={}
line_count=0

#Generates a combination that preserves only letters and Spaces    
cop=re.compile("[^\s^a-z]")

for sentence in text:
	words=sentence[0]
	# Convert all words to lowercase
	words=words.lower()
	# replace
	#for ch in '!@#$%:^&*()-.;,':
		#words=words.replace(ch," ")
	words = cop.sub("", words)
	words=words.split()
	for word in words:
		word=PorterStemmer().stem(word)
		if len(word)<4:
			continue
		if word in counts:
			counts[word] = counts[word]+coef*(likes[line_count][0])+1
		else:
			counts[word]=coef*(likes[line_count][0])+1
	line_count+=1

items=list(counts.items())
# Sort by second column
items.sort(key=lambda x:x[1],reverse=True)
# Words and times of output frequency
with open('freqency_Stem.txt','w',encoding ="utf-8") as f:
	for i in range (len(items)): 
		word,count=items[i]
		f.write("{0}：{1}".format(word,count)+'\n')

workbook = xlsxwriter.Workbook('frequency_Stem.xlsx')
worksheet = workbook.add_worksheet()
for i in range(len(items)):
	word,count=items[i]
	worksheet.write(i, 0, word)  # Row I, column 0
	worksheet.write(i, 1, count) # Row I, column 1
 
workbook.close()
