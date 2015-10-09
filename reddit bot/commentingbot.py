# if bot restarts, posts are not saved locally and bot will reply again
import praw
import time
import os
from bot_config import *

# very very very small chance reddit banned this user agent :)
r = praw.Reddit('subreddit commenting robo by /u/nachozombie v1.0')

def startup():
	you_dun_goofed()
	r.login(R_USERNAME, R_PASSWORD)
	
def you_dun_goofed():
	if not os.path.isfile("bot_config.py"):
		print("Looks like you don't know what you're doing.")
		print("Make a config file for the bot. Name as bot_config.py")
		exit(1)
	
def target():
	x = 1
	prawWords = []
	words = input("How many keywords or phrases are you looking for? ")
	while x <= int(words):
		print("Enter the keyword or phrase that you want to look out for. Phrase/Word #", x)
		interests  = input()
		prawWords.append(interests)
		x = x + 1

def get_subreddit():
	sub = input("Subreddit: ")
	return sub
	
def get_comment():
	response = input("Comment: ")
	return response

def find_load_log():
	if not os.path.isfile("already_done.txt"):
		print("You thought you knew what you were doing.")
		print("Make a log for the bot. Name as already_done.txt")
	else:
		with open("already_done.txt", "r") as f:
			already_done = f.read()
			already_done = already_done.split("\n")
			already_done = filter(None, already_done)
			
def update_log():
	with open("already_done.txt", "w") as f:
		for post_id in already_done:
			f.write(post_id + "\n")
		
def loop():	
	find_load_log()
	already_done = []
	soob = get_subreddit()
	comment = get_comment()
	while True:
		subreddit = r.get_subreddit(soob)
		for submission in subreddit.get_new(limit = 5):
			if submission.id not in already_done:
				submission.add_comment(comment)
				already_done.append(submission.id)
	update_log()			

	time.sleep(15)			
	
def main():
	startup()
	target()
	loop()
	
main()