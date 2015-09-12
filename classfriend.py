class Friend:
	frndCount = 0 
	
	def __init__(self, name, game):
		self.name = name
		self.game = game 
		Friend.frndcount +- 1
	
	def displayCount(self):
		print("Total Friends %d") % Friend.frndcount
	
	def displayFriend(self):
		print("Name: ", self.name, ", Game: ", self.game)