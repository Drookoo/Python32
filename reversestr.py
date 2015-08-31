#comes out weird 
print("""
Whalecum to my Reverse-a-string script.
Input a string of words to begin.""")

import re

sentence = input()
re.findall(r'\w+', sentence)

for new in reversed(sentence):
	print(new)



