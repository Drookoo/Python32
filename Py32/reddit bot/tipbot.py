import praw 
import time
r = praw.Reddit('/r/dogecoin tipping bot by /u/nachozombie')

r.login()
already_done = []
prawWords = ['help']

while True:
	subreddit = r.get_subreddit('nachozombie')
	for submission in subreddit.get_hot(limit = 10):
		op_text = submission.selftext.lower()
		has_praw = any(string in op_text for string in prawWords)
		
		if submission.id not in already_done and has_praw:
			submission.add_comment('+/u/dogetipbot 20 doge')
			already_done.append(submission.id)
	time.sleep(30)

