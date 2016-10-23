#This is our uninformed search algorithm


from sys import argv
#from Classes import Cask, Stack 

#Global variables 
inputfile = argv[1]
goal_cask = argv[2]
casks = {}
stacks = {}
edges = []
goal_cask_loc = ""

#Collecting data from the input file
try:
	file = open(inputfile)
except IOError:
	print ("unable to open file")	
for line in file:
	#line = line.rstrip('\n')
	if len(line) > 1:
		key = line[0]
		print(key)
		line = line.split()
		if key == "C":
			#casks(key) = Cask(key,int(line[1]), float(line[2]))
			print(line)
		elif key == "S":
			temp_stack = Stack(line.pop(0), line.pop(0))
			for cask in line:
				temp_stack.addCaskToStack(casks.get(cask))
			stacks(temp_stack.s_id) = temp_stack 
		elif key == "E":
			edges.append(line)
			print(line)
		
		else:
			print("Unknown key in document")



# 1 first find the cheapest way to the stack that holds our goal cask
# 2 find the cheapest way to load the goal cask onto the CTS
# 3 return along the reversed path found in 1 


#We start at the exit node, should implement some sort of uniform cost algorithm
#to ensure finding the best way to the stack right away. 

#Our nodes are placed in a list, the include a list of edges they point to
#we must somehow store all explored nodes and the cost to reach them 

#build a min spanning tree using dijkstra? Also need to keep track of 
