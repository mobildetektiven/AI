#This is our uninformed search algorithm

from sys import argv
from classes import Cask, Stack, Node, Edge, State
from uninformed import SearchProblem, inf
from domainIndependent import uniformCostSearch


#Global variables 
inputfile = argv[1]
goal_cask = argv[2]
casks = {}
stacks = {}
nodes = {}
edges = []
node_name_to_num = {} 
node_num_to_name = {} 
goal_cask_loc = ""
num_nodes = 0
goal_node = "EXIT"



#Collecting data from the input file build 

try:
	file = open(inputfile)
except IOError:
	print ("unable to open file")

for line in file:
	#line = line.rstrip('\n')
	if len(line) > 1:
		key = line[0]
		line = line.split()
		print(line)

		#build a cask object for each cask in the input file, store in a dictonary
		if key == "C":
			temp_cask = Cask(line[0],int(line[1]), float(line[2]))
			casks[temp_cask.c_id] = temp_cask

		#build a stack object for each stack in the input file
		#Check if stack contains a cask, if so put cask in stack
		#Build a node with the stack name, and store the stack in the node
		#Give all nodes a uniqe number ID for use in adjacancy matrix
		#store all nodes in a dictonary, using the number_id as key
		#Store name connected to number in two different dictonaries for references	
		elif key == "S":
			temp_stack = Stack(line.pop(0), int(line.pop(0)), [])
			for cask in line:
				temp_stack.addCaskToStack(casks.get(cask))

			stacks[temp_stack.s_id] = temp_stack
			
			node_name = temp_stack.s_id
			nodes[node_name] = Node(node_name,num_nodes,True)
	
			node_name_to_num[node_name] = num_nodes
			node_num_to_name[num_nodes] = node_name
			num_nodes += 1
		
		#Create an edge object for each edge, store it in a list. If new nodes are
		#discovered, create a node object for them, and store in the node dictonary
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

print(num_nodes)
#build goal_state



goal_state = State(goal_node,True,None,0,0,None,goal_cask, None, None, None, 0)
initial_state = State(goal_node,False,0,0,None,None,None,stacks,[],{}, 0)

#build adjacency matrix, set all values to inf
adj_matrix = [[inf for x in range(num_nodes)] for y in range(num_nodes)] 

print(adj_matrix)
#do we need to set distance to ourselves = 0? 

#Update adj. Matrix with node edges
for edge in edges:
	n1 = node_name_to_num[edge.end_node_1]
	n2 = node_name_to_num[edge.end_node_2]
	adj_matrix[n1][n2] = edge.length
	adj_matrix[n2][n1] = edge.length


problem = SearchProblem(adj_matrix, node_name_to_num,node_num_to_name, num_nodes, goal_cask, goal_node)

success = uniformCostSearch(problem,goal_state,initial_state)
if success:
	print("you have found the solution")
else:
	print("you didn't find the solution")



# 1 first find the cheapest way to the stack that holds our goal cask
# 2 find the cheapest way to load the goal cask onto the CTS
# 3 return along the reversed path found in 1 

#func build adjacencyList()

#func find_next_states(current_state, allowed_actions, adjacency_list
	#


#Graph_Search(initial_state, goal_state, allowed actions, adjacency list)

#	closed_states = None
#	fringe = None
#	state = initial_state
	
 
#	while state != goal_state
#	find next possible states based on current state and allowed actions 
#	check if they are in the closed states list
#	if not add to fringe and sort
#	retreive next state from fringe
#	update state variable, add new chain to action chained list 







#We start at the exit node, should implement some sort of uniform cost algorithm
#to ensure finding the best way to the stack right away. 

#Our nodes are placed in a list, the include a list of edges they point to
#we must somehow store all explored nodes and the cost to reach them 

