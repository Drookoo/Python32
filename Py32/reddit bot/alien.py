import praw

user_angent = ("PyEng Bot 0.1")

r = praw.reddit(user_agent = user_agent)

subreddit = r.get_subreddit("nachozombie")

for submission in subreddit.get_new(limit = 5):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("---------------------------------\n")