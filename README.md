# YoutubeCommentsAnalysis
A small Project about downloading Youtube comments and anaylsis them via frequency of each words
Before start, please apply for youtube comments V3 API and put your API ID into comment_downloader.py

Execute driver.py to start crawling YouTube comments, and save the comments and their corresponding thumb up in the comments.xlsx file as excel (you can also sort comments by thumb up number, which is also easy to implement, but not done yet)

Execute statistic.py reads the comments and their likes from the comments.xlsx file, cleans the comments briefly (removes punctuation marks, etc.), and outputs the cleaned results (not written yet, this is easy);

Then, according to the weighted calculation formula, as follows:

Word frequency f=∑ (number of times the word appears in the comment + coefficient × thumb up number)

Then sort the word frequency, and output as TXT file.

PS: statistic_Semantic_merge.py and statistic_Stem_merge.py 1 and 2 merge certain words based on Semantic and Stem analysis respectively, such as "love" and "lovely" into the same word


