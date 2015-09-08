import praw
r = praw.Reddit('subreddit commenting robo by /u/nachozombie v0.1')

def startup():
	r.login()
	already_done = []
	target()
	
def target():
	prawWords = []
	if 
	interests  = input("Enter the keywords or phrases that you want to look out for")