import praw
import pdb
import re
import os
import time
from bot_config import *

user_agent = ("nachozombie robo")
r = praw.Reddit(user_agent=user_agent)
r.login(R_USERNAME, R_PASSWORD)
if not os.path.isfile("already_done.txt"):
    posts_replied_to = []
# If we have run the code before, load the list of posts we have replied to
else:
    # Read the file into a list and remove any empty values
    with open("already_done.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = filter(None, posts_replied_to)

# Get the top 5 values from our subreddit
subreddit = r.get_subreddit('nachozombie')
for submission in subreddit.get_hot(limit=5):
    # print submission.title

    # If we haven't replied to this post before
    if submission.id not in posts_replied_to:

        # Do a case insensitive search
        if re.search("waldo", submission.title, re.IGNORECASE):
            # Reply to the post
            submission.add_comment("Nigerian scammer bot says: It's all about the Bass (and Python)")
            print("Bot replying to : "), submission.title

            # Store the current id into our list
            posts_replied_to.append(submission.id)
    time.sleep(9999)

# Write our updated list back to the file
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")