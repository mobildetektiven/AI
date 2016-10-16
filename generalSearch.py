#This is our uninformed search algorithm

#Collecting and processing data from inputfile
from sys import argv
inputfile = argv[1]
goalCask = argv[2]
casks = []
stacks = []
edges = []
try:
	file = open(inputfile)
	for string in file:
		line = string.rstrip('\n')
		if len(line) > 0:
			key = line[0]
			if key == "C":
				casks.append(line)
			elif key == "S":
				stacks.append(line)
			elif key == "E":
				edges.append(line)
			else:
				print("Unknown key in document")
except IOError:
	print ("unable to open file")

