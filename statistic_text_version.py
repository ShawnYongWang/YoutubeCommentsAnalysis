coef=1.0
def getText():
    # Read the TXT file
    txt=open("comments.txt","r",encoding ="utf-8").read()
    # Convert all words to lowercase
    txt=txt.lower()
    # Replaces special characters with Spaces
    for ch in '!@#$%:^&*()-.;':
        txt=txt.replace(ch," ")
    return txt

text=getText()

with open('cleancomments.txt','w',encoding ="utf-8") as f:
    f.write(text)


def getlikes():
    #   Read the TXT file
    likes=[]
    with open("likes.txt","r") as f:
        for line in f:#Iterate through each row
            wordlist=line.split()#Separate the Numbers in the list for each line
            likes.append(int(wordlist[0]))
        #print("the sum is",likes)
        return likes
    f.close()
likes=getlikes()
#print(len(likes))
# The string is split by Spaces
sentences=text.split('\n')
#print(len(sentences))
# Defines an empty dictionary to hold words and their corresponding occurrences
counts={}
line_count=0
for sentence in sentences:
    words=sentence.split()
    #print(words)
    for word in words:
        #print(type(word))
        if word in counts:
            counts[word] = counts[word]+coef*int(likes[line_count])
        else:
            counts[word]=coef*int(likes[line_count])
    line_count+=1

#for word in words:
    # When Word is not in words, the return value is 0; when Word is in words, the return value is +1
    # counts[word]=counts.get(word,0)+1
    # The second method
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
