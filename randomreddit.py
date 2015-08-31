"""
browse random subreddits.
don't input numbers over 90 if you have potato processor 
ie: not ivy bridge, not sandy bridge, not haswell?
I used bloomfield so I would know.
"""

import webbrowser

url = 'https://reddit.com/r/random'

amount = input("How many random subreddits would you like to visit? ")

x = 1

while x <= int(amount): 
	webbrowser.open(url, new=0, autoraise=True)
	x = x + 1
	
	
