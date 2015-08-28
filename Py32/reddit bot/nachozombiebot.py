import time
import praw
r = praw.Reddit('PRAW test bot by /u/nachozombie v 1.0. ')
r.login()
already_done = []
prawWords = ['test']
#
while True:
	subreddit = r.get_subreddit('nachozombie')
	for submission in subreddit.get_hot(limit = 10):
		op_text = submission.selftext.lower()
		has_praw = any(string in op_text for string in prawWords)
		
		#r.send_message('redditor','msg title',body message)
		if submission.id not in already_done and has_praw:
			msg = 'SUCCESS'
			r.send_message('nachozombie','BLASTOFF',msg)
			already_done.append(submission.id)
	time.sleep(30)