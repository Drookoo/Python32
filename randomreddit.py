import webbrowser

url = 'https://reddit.com/r/random'

print("How many random subreddits would you like to visit?")
amount = input()

x = 1

while x <= int(amount): 
	webbrowser.open(url, new=0, autoraise=True)
	x = x + 1
	
	