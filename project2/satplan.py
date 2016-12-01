#imports
import os
import itertools
from sys import argv
from func import findTerm, findNumOfInputsAndConstants, isNegated
#Global variables

#store input variables
inputfile = argv[1]

term_dict = {}
init_state_dict = {}
const_dict = {}
action_dict = {}
consts = []
num_of_terms = 0
num_of_actions = 0



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
			print()
		
		#Collect the initial state, find all terms and constants
		#Save all terms with their name as key in term_dict, on each
		#key store the number of input variables
		elif key == "I":
			print("initial state")
			for word in line:
				#print(word)
				term = findTerm(word)
				print("terms:" , term)
				num_of_inputs,constants = findNumOfInputsAndConstants(word)
				term_dict[term] = num_of_inputs
				if(isNegated(word)):
					init_state_dict[word[1:]] = False
				else:
					init_state_dict[word] = True
				for constant in constants:
					const_dict[constant] = True
		#Collect all possible actions
		#store in dict with action name as key, at each key store a list, index 0 is num
		#of input arguments, i1 is all terms that have to be fullfilled at given timestep
		#index 2 is a list with terms to be fullfilled at next timestep
		#
		elif key == "A":
			word = line.pop(0)
			action = findTerm(word)
			num_of_inputs,_ = findNumOfInputsAndConstants(word)
			action_dict[action] = [num_of_inputs]
			
			current_timestep = True
			current_terms = {}
			next_terms = {}		
			
			for word in line:
				if(current_timestep):
					if(word == "−>"):
						current_timestep = False
					elif(word != ":"):
						if(isNegated(word)):
							current_terms[word[1:]] = False
						else:
							current_terms[word] = True

				else:
					if(word != ":"):
						if(isNegated(word)):
							next_terms[word[1:]] = False
						else:
							next_terms[word] = True
			action_dict[action].append(current_terms)
			action_dict[action].append(next_terms)

		else:
			print("Unknown key in document")

#print(consts)
# for term in term_dict:
# 	inputs = term_dict[term]
# 	print(term, " ", inputs)
# 	i = 0
# 	list_of_constants = []
# 	temp_list = []
# 	for a in range(0,inputs):
# 		temp_list.append(consts[i+a])
# 		i += 1
# 		list_of_constants.append(temp_list)
# 	for l in list_of_constants:
# 		print(l)
#for x in const_dict:
#	print(x)

print("TERMS")
for term in term_dict:
	print(term, term_dict[term])


print("Initial State")
for x in init_state_dict:
	print(x, init_state_dict[x])


print("Constants")
for x in const_dict:
	print(x)

print("Actions")
for action in action_dict:
	print(action, action_dict[action])


#print((list(itertools.permutations(["a", "b", "c"]))))

