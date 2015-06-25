import random, pygame  

my_number = random.randrange(51)

print "Guess a number from 1-50"
guess = raw_input() 
print "Is %r your number? Answer with Yes or No" % (
	guess)
answer = raw_input()

if my_number == guess:
	print "You have guessed correctly!"
elif my_number != guess:
	print "You have guess incorrectly."
