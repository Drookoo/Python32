"""
Whalecum to my English to Pig Latin Translator.
Input your desired English word."""
	
word = input("Input your desired word ")

Vowel = ['a', 'e', 'i', 'o', 'y', 'u', 'A', 'E', 'I', 'O', 'U', 'Y']
if [word[0]] not in Vowel:
	print(word[1:50] + word[0] +"ay")
elif [word[0]] in Vowel:
	print(word + "yay")

