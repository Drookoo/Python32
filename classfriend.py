class Friend:
	frndCount = 0 
	
	def __init__(self, name, game):
		self.name = name
		self.game = game 
	
	def displayFriend(self):
		print("Name:", self.name, ", Game:", self.game)

buddy1 = Friend("Dog", "Payday 2")
buddy1.displayFriend()
