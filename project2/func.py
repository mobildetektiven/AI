def findTerm(word):
	term = ""
	termFound = False
	for letter in word:
		if(not termFound):
			if(letter == "("):
				return term
			else:
				term = term + letter
	

def findNumOfInputsAndConstants(word):
	num_of_inputs = 0
	constants = []
	for letter in word:
		if letter.isalnum() and letter.isupper():
			num_of_inputs += 1
			constants.append(letter)
	return num_of_inputs, constants

def isNegated(word):
	if(word[:1] == "−"):
		return True
	return False	