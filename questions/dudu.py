import time

def seconds():
	seconds = input("How many seconds do you want to sleep for?")

def loop():
	Number = 1 
	print(Number)
	while True: 
		Number = Number + 1 
		print(Number)
		time.sleep(1)

loop()