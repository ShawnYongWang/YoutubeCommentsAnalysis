import comment_downloader as CD
import xlsxwriter
import sentimentYouTube as SYT
import requests
import json
def main():
	# EXAMPLE videoID = 'tCXGJQYZ9JA'
	# videoId = input("Enter the videoID : ")
	videoId_all = ['FWMIPukvdsQ','LTejJnrzGPM','hR4DiU8wcVk','sbr-SAi6PHM','YSU9ZFd0lhc']
	#videoId_all = ['YSU9ZFd0lhc']
	#Put in the ID of the video of which comment you want to get
	# Fetch the number of comments   
	# if count = -1, fetch all comments
	# count = int(input("Enter the no. of comment to extract : "))
	count = 1000
	leastlikes=1
	comments = []
	#bufferI = []
	#bufferII = []
	likes = []
	with open('verified_proxies.json', encoding='utf-8') as f:
		# for line in f:
		a = json.load(f)
		#I put a proxy IP in it to prevent IP from being blocked. Every time I crawl a website, I change a proxy IP. Running IP.py can get the proxy IP
	# final[a['type']] = a['host']+':'+a['port']

	for videoId in videoId_all:
		requests.adapters.DEFAULT_RETRIES = 20
		s = requests.session()
		flag = 0
		# s.proxies = {"http": "27.152.8.152:9999", "https": "117.57.91.131:24978"}
		s.keep_alive = False
		s.proxies = {a[flag]['type']:str(a[flag]['host'])+':'+str(a[flag]['port'])}
		flag = flag+1
		#print(type(CD.commentExtract(videoId, count)[0]),type(CD.commentExtract(videoId, count)[1]))
		#print(CD.commentExtract(videoId, count)[1])
		(bufferI,bufferII)=CD.commentExtract(videoId, count,leastlikes)
		comments=comments+bufferI
		likes=likes+bufferII 
	
	with open('comments.txt','w',encoding='utf-8') as f:
		for i in comments:
			# Replaces newline characters with Spaces
			i=i.replace('\n','$')
			f.write(i+'\n')#Keep a record of crawled comments (which are filtered and exceed the set liking threshold)
	
	workbook = xlsxwriter.Workbook('comments.xlsx')
	worksheet = workbook.add_worksheet()
	for i in range(len(comments)):
		worksheet.write(i, 0, comments[i])  # Row I, column 0
		worksheet.write(i, 1, likes[i]) # Row I, column 1
 
	workbook.close()
	with open('likes.txt','w',encoding='utf-8') as f:
		for i in likes:
			f.write(str(i)+'\n')
	#SYT.sentiment(comments)
	#FS.fancySentiment(comments)



if __name__ == '__main__':
	main()
