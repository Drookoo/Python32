""" 
This is a tool for the game Mafia/ Werewolf/ or whatever you call yours.
The narrator uses this tool and discretely tells players on what thier
roles are. This tool assumes you have 2 bad guys, 1 cop and an angel. 
"""

import random

print("Hi, enter the number of players in your game")
players = input()

x = 1
playernames = []

while x <= int(players):
	print("Enter the name of player", x)
	name = input() 
	playernames.append(name)
	x = x + 1

print ("The following are the players:", playernames)
random.shuffle(playernames)	

print(playernames[0], "is the cop")
playernames.remove(playernames[0])
random.shuffle(playernames)	

print(playernames[0], "is a member of the mafia")
playernames.remove(playernames[0])
random.shuffle(playernames)	
print(playernames[0], "is a member of the mafia")
playernames.remove(playernames[0])

print(playernames, "are the citizens")