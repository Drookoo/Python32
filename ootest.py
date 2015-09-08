"""
Object Orienting 101
"""
def what_to_play():
	def do_local():
		game = "Dota 2"
	def do_nonlocal():
		nonlocal game
		game = "Payday 2"
	def do_global():
		global game 
		game = "Half Life 2"
	game = "Path of Exile"
	do_local()
	print ("Let's locally play", game)
	do_nonlocal()
	print ("Let's non-locally play", game)
	do_global()
	print("Let's globally play", game)

what_to_play()
print("Let's play", game)