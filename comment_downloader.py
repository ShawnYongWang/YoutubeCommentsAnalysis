import lxml
import requests
import time
import sys
import progress_bar as PB
import json

YOUTUBE_IN_LINK = 'https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&maxResults=100&order=relevance&pageToken={pageToken}&videoId={videoId}&key={key}'
YOUTUBE_LINK = 'https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&maxResults=100&order=relevance&videoId={videoId}&key={key}'
key = ''   #Change to your Google API

def commentExtract(videoId, count = -1,leastlikes=300):
	print ("\nComments downloading")
	#Close the HTTP connection and increase the number of reconnections



	page_info = requests.get(YOUTUBE_LINK.format(videoId = videoId, key = key))
	while page_info.status_code != 200:
		if page_info.status_code != 429:
			print ("Comments disabled")
			sys.exit()

		time.sleep(20)
		page_info = requests.get(YOUTUBE_LINK.format(videoId = videoId, key = key))

	page_info = page_info.json()
	#test
	# print(page_info)

	comments = []
	likes=[]
	co = 0
	for i in range(len(page_info['items'])):
		#The comments above like Leastlike are reserved, which can be changed as needed
		if page_info['items'][i]['snippet']['topLevelComment']['snippet']['likeCount']>=leastlikes:
			comments.append(page_info['items'][i]['snippet']['topLevelComment']['snippet']['textOriginal'])
			likes.append(page_info['items'][i]['snippet']['topLevelComment']['snippet']['likeCount'])
			co += 1
		if co == count:
			PB.progress(co, count, cond = True)
			return comments,likes

	PB.progress(co, count)
	# INFINTE SCROLLING
	while 'nextPageToken' in page_info:
		temp = page_info
		page_info = requests.get(YOUTUBE_IN_LINK.format(videoId = videoId, key = key, pageToken = page_info['nextPageToken']))

		while page_info.status_code != 200:
			time.sleep(20)
			page_info = requests.get(YOUTUBE_IN_LINK.format(videoId = videoId, key = key, pageToken = temp['nextPageToken']))
		page_info = page_info.json()

		for i in range(len(page_info['items'])):
			if page_info['items'][i]['snippet']['topLevelComment']['snippet']['likeCount']>=leastlikes:
				comments.append(page_info['items'][i]['snippet']['topLevelComment']['snippet']['textOriginal'])
				likes.append(page_info['items'][i]['snippet']['topLevelComment']['snippet']['likeCount'])
				co += 1
			if co == count:
				PB.progress(co, count, cond = True)
				return comments,likes
		PB.progress(co, count)
	PB.progress(count, count, cond = True)
	print ()

	return comments,likes

