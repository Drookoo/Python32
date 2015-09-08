#the following are notes to self:
#search if commented already 
#search if I have replied to this user in the past 12 hours
#storing data in file
import praw
r = praw.Reddit('/r/dogecoin tipping robo by /u/nachozombie v0.1')

#I don't mind if you use my throwaway 
r.login()
already_done = []
prawWords = ["a","i"]

while True:
	subreddit = r.get_subreddit('nachozombie')
	for submission in subreddit.get_new(limit = 5):
		if submission.id not in already_done:
			submission.add_comment("Have some doge. +/u/dogetipbot 30 doge ")
			already_done.append(submission.id)