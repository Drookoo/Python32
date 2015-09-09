import time

def seconds():
	seconds = input("How many seconds do you want to sleep for?")
	return seconds

def loop():
	Number = 0 
	length = seconds()
	print (Number)
	while True: 
		Number = Number + 1 
		print(Number)
		time.sleep(int(length))

loop()