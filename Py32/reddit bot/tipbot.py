import praw
r = praw.Reddit('/r/dogecoin tipping robo by /u/nachozombie v0.1')

r.login()
already_done = []
prawWords = ["ball"]

while True:
	subreddit = r.get_subreddit('nachozombie')
	for submission in subreddit.get_hot(limit = 10):
		op_text = submission.selftext.lower()
		has_praw = any(string in op_text for string in prawWords)
		
		if submission.id not in already_done and has_praw:
			submission.add_comment("Have some doge.  " + "+/u/dogetipbot 30 doge verify")
			already_done.append(submission.id)
		elif submission.id not in already_done:
			submission.add_comment("Have some doge.  " + "+/u/dogetipbot 20 doge verify")
			already_done.append(submission.id)