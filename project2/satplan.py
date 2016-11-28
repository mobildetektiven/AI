#imports
import os
import itertools
from sys import argv

#Global variables

#store input variables
inputfile = argv[1]

term_dict = {}
const_dict = {}
try:
	file = open(inputfile)
except IOError:
	print ("unable to open file")
	os._exit(0)

for line in file:
	if len(line) > 1:
		line = line.split()
		key = line.pop(0)

		#Collect the goal state
		if key == "G":
			print(line)

		
		#Collect the initial state, find all terms and constants
		#and save them in dictonaries 
		
		elif key == "I":
			for word in line:
				term = ""
				termFound = False
				for letter in word:
					if(not termFound):
						if(letter == "("):
							termFound = True
						else:
							term = term + letter
					if letter.isalnum() and letter.isupper():
						const_dict[letter] = True

				term_dict[term] = True
		#Collect all possible actions
		
		elif key == "A":
			for word in line:
				action = ""
				actionFound = False
				for letter in word: 
					if(not actionFound):
						if(letter == "("):
							actionFound = True
						else:
							action = action + letter
		else:
			print("Unknown key in document")

for x in term_dict:
	print(x)
for x in const_dict:
	print(x)

print(list(itertools.permutations(["a", "b", "c"])))