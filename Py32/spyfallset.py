"""
Tool for the game Spyfall. The Moderator inputs the names of the 
players into the tool and the tool outputs the location and the roles.
"""
import random

list1 = ['Airplane', 'Bank', 'Beach', 'Cathedral', 'Circus Tent',
		'Corporate Party', 'Crusader Army', 'Casino', 'Day Spa', 
		'Embassy', 'Hospital', 'Hotel', 'Military Base', 'Movie Studio',
		'Ocean Liner', 'Passenger Train', 'Pirate Ship', 'Polar Station',
		'Police Station', 'Restaurant', 'School', 'Service Station',
		'Submarine', 'Supermarket', 'Theater', 'University', 'War Zone']
 
print("Hi, enter the number of players in your game.")
players = input()

x = 1
playernames = []

while x <= int(players):
	print("Enter the name of player", x)
	name = input() 
	playernames.append(name)
	x = x + 1
	
random.shuffle(playernames)	
random.shuffle(list1)
print(playernames[0], "is the spy. And", list1[0], "is the location")






