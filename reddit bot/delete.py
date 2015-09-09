# if bot restarts, posts are not saved locally and bot will reply again
import praw
import time
r = praw.Reddit('subreddit commenting robo by /u/nachozombie v0.1')

def startup():
	r.login()
	
def target():
	x = 1
	prawWords = []
	words = input("How many keywords or phrases are you looking for? ")
	while x <= int(words):
		print("Enter the keyword or phrase that you want to look out for. Phrase/Word #", x)
		interests  = input()
		prawWords.append(interests)
		x = x + 1

def loop():	
	already_done = []
	while True:
		subreddit = r.get_subreddit('nachozombie')
		for submission in subreddit.get_new(limit = 5):
			if submission.id not in already_done:
				submission.add_comment('tacoking')
				already_done.append(submission.id)			
	# sleep is for the weak	
def main():
	startup()
	target()
	loop()
	
main()