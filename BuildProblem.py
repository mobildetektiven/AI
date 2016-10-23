

#imports
import os
from sys import argv
from classes import Cask, Stack, Node, Edge, State
from uninformed import SearchProblem, inf
from domainIndependent import uniformCostSearch, printToFile


#Global variables

#store input variables
inputfile = argv[1]
goal_cask_name = argv[2]

#store all nodes, casks and stacks in dictonary
casks = {}
stacks = {}
nodes = {}

#used to build adjacency matrix
edges = []

#dictionaries to convert between node name and node number, for use with
#print and adjacancy matrix
node_name_to_num = {} 
node_num_to_name = {} 
num_nodes = 0
goal_node = "EXIT"
goal_stack_name = ""


#Collecting data from the input file and building objects 
try:
	file = open(inputfile)
except IOError:
	print ("unable to open file")
	os._exit(0)

for line in file:
	if len(line) > 1:
		key = line[0]
		line = line.split()

		#build a cask object for each cask in the input file, store in a dictonary
		if key == "C":
			new_cask = Cask(line[0],int(line[1]), float(line[2]))
			casks[new_cask.c_id] = new_cask

		#Build a node and a stack object for each stack, store stack in node
		#Store list of cask names to enable storing of casks later
		elif key == "S":
			new_stack = Stack(line.pop(0), int(line.pop(0)), [])
			for cask in line:
				new_stack.stored_casks.append(cask)
			stacks[new_stack.s_id] = new_stack
			node_name = new_stack.s_id
			nodes[node_name] = Node(node_name,num_nodes,True)
	
			node_name_to_num[node_name] = num_nodes
			node_num_to_name[num_nodes] = node_name
			num_nodes += 1
		
		#For each edge, check if nodes exist, if not create and store in nodes dict
		elif key == "E":
			n1 = line[1]
			n2 = line[2]
			edges.append(Edge(n1,n2,float(line[3])))
			if n1 not in nodes:
				nodes[n1] = Node(n1,num_nodes,False)
				node_name_to_num[n1] = num_nodes
				node_num_to_name[num_nodes] = n1
				num_nodes += 1
			if n2 not in nodes:
				nodes[n2] = Node(n2,num_nodes,False)
				node_name_to_num[n2] = num_nodes
				node_num_to_name[num_nodes] = n2
				num_nodes += 1
		else:
			print("Unknown key in document")

#build adjacency matrix for all edges, set all values to Inf default
adj_matrix = [[inf for x in range(num_nodes)] for y in range(num_nodes)] 

#Update adj. Matrix with node edges costs
for edge in edges:
	n1 = node_name_to_num[edge.end_node_1]
	n2 = node_name_to_num[edge.end_node_2]
	adj_matrix[n1][n2] = edge.length
	adj_matrix[n2][n1] = edge.length

# Store all discovered casks in their stack
for stack_name, stack in stacks.items():
	new_stored_casks = []
	for cask in stack.stored_casks:
		if cask == goal_cask_name:
			goal_stack_name = stack_name
		new_stored_casks.append(casks[cask])
	stack.stored_casks = new_stored_casks
if goal_stack_name == "":
	print("Goal cask has no stack")
	printToFile(["Goal cask has no stack"], "error.txt")
	os._exit(0)


#Build goal and initial state
goal_state = State(goal_node,True,None,0,0,None,goal_cask_name, None, None, None, 0)
initial_state = State(goal_node,False,0,0,None,None,None,stacks,[],{}, 0)

#Build searchProblem object, and send to search algorithm
problem = SearchProblem(adj_matrix, node_name_to_num,node_num_to_name, num_nodes, goal_cask_name, goal_node)
solution_path = uniformCostSearch(problem,goal_state,initial_state)


# create file with input file name as argument
save_to_file_name = ""
for letter in inputfile:
	if letter != ".":
		save_to_file_name += letter

save_to_file_name += goal_cask_name + "Solution"

printToFile(solution_path,save_to_file_name)
#Write solution to file


