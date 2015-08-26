"""
When I'm bored, I like browsing new things on reddit. 
This tool helps you. Too bad that reddit's random is not very random.
You will see why if you use this tool in large quantities.
"""

import webbrowser

url = 'https://reddit.com/r/random'

amount = input("How many random subreddits would you like to visit? ")

x = 1

while x <= int(amount): 
	webbrowser.open(url, new=0, autoraise=True)
	x = x + 1
	
	
