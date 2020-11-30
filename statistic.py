coef=0.01
import pandas as pd

def getText():
    # read txt file
    df = pd.read_excel('comments.xlsx',usecols=[0])
    txt=df.values
    #txt=open("comments.txt","r",encoding ="utf-8").read()
    return txt

text=getText()

#with open('cleancomments.txt','w',encoding ="utf-8") as f:
    #f.write(text)


def getlikes():
    # read txt file
    df = pd.read_excel('comments.xlsx',usecols=[1])
    likes=df.values
    #print(likes[1][0])
    return likes
likes=getlikes()

# Defines an empty dictionary to hold words and their corresponding occurrences
counts={}
line_count=0
# Convert all words to lowercase

    

for sentence in text:
    words=sentence[0]
    # Convert all words to lowercase
    words=words.lower()
    # Replaces special characters with Spaces
    for ch in '!@#$%:^&*()-.;,':
        words=words.replace(ch," ")
    #print(type(words))
    words=words.split()
    #print(type(words))
    #print(words)
    for word in words:
        #print(type(word))
        if len(word)<4:
            continue
        if word in counts:
            #print(type(likes[line_count][0]))
            #print(likes[line_count][0])
            counts[word] = counts[word]+coef*(likes[line_count][0])+1
        else:
            counts[word]=coef*(likes[line_count][0])+1
    line_count+=1

#for word in words:
    # When Word is not in words, the return value is 0; when Word is in words, the return value is +1
    # counts[word]=counts.get(word,0)+1
    # Second method
    #if word in counts:
        #counts[word] = counts[word]+lambda*likes[i]
    #else:
        #counts[word]=1

# Converts the dictionary to a list of records
# Items () method: Returns an array of traversable (keys, values) tuples as a list.
items=list(counts.items())
# Sort by second column
items.sort(key=lambda x:x[1],reverse=True)
# Words and times of output frequency
with open('freqency.txt','w',encoding ="utf-8") as f:
    for i in range (len(items)): 
        word,count=items[i]
        f.write("{0}：{1}".format(word,count)+'\n')
