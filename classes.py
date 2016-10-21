class Cask:
	def __init__(self, c_id, length, weight):
		self.c_id = c_id
		self.length = length
		self.weight = weight


class Stack:
	def __init__(self, s_id, size, stored_casks):
		self.s_id = s_id
		self.size = size
		self.stored_casks = stored_casks

	def addCaskToStack(self,arrived_cask):
		if self.occupiedStackSize() + arrived_cask.length <= self.size:
			self.stored_casks.append(arrived_cask) 
			return True
		else:
			print ("There is not enough room in this stack!")
			return False

	def removeCaskFromStack(self):
		if (len(self.stored_casks) > 0):
			loaded_cask = self.stored_casks.pop()
			print ("Picking up: ", loaded_cask)
			return loaded_cask
		else:
			print ("There are no casks to pick up in this stack!")
			return False

	def occupiedStackSize(self):
		occ_size = 0
		for cask in self.stored_casks:
			occ_size += cask.length
		return occ_size

class Node:
	def __init__(self, n_id, node_number, stack):
		self.n_id = n_id
		self.node_number = node_number
		self.stack = None

class Edge:
	def __init__(self, end_node_1, end_node_2, length):
		self.end_node_1 = end_node_1
		self.end_node_2 = end_node_2
		self.length = length

class State:
	def __init__(self, location, weight, total_cost, loaded, previous_state, action, goal_cask):
		self.location = location #node name
		self.weight = 1
		self.total_cost = 0
		self.loaded = False
		self.previous_state =  None
		self.action = None
		self.goal_cask = goal_cask


# class CTS:
# 	def __init__(self, location, goal_cask, state):
# 		self.location = location #In what node or stack is the CTS currently located
# 		self.loaded = None #Cask
# 		self.goalCask = goal_cask
# 		self.state = state

	#def nextActionList(self):
		#possible moves first
	#	for node in self.location
	
	# def moveCTS(self, edge):
	# 	if self.location == edge.end_node_1:
	# 		self.location = edge.end_node_2
	# 	elif self.location == end_node_2:
	# 		self.location = edge.end_node_1
	# 	else:
	# 		print ("The CTS is cannot move along this edge!")

	# def load(self,cask):
	# 	if (loaded != None):
	# 		Print("The CTS is already loaded - Only one at the time")
	# 	else: 
	# 		loaded = cask

	# def unload(self,cask):
	# 	if (loaded != None):
	# 		print ("There is nothing to unload - The CTS is empty")
	# 	else: 
	# 		loaded = None


	# def allowedActions(self, adjacency_list, mode, total_number_of_nodes):  #may find another way to find total_number_of_nodes
	# 	allowed_actions_list = []
	# 	row = self.location.n_id
	# 	for column in total_number_of_nodes:
	# 		if (adjacency_list[row][column] != 0): #gitt at vi setter inn 0 der det ikke ekstisterer edges
	# 			possible_action = move
	# 			possible_target = column

#Testing Code
# Cask1 = Cask(1,5,5)
# Cask2 = Cask(2,5,5)
# Cask3 = Cask(3,5,7)

# listOfCasks = [Cask1,Cask2]
# print (listOfCasks)
# Stack1 = Stack(1,15,listOfCasks)
# print (Stack1.stored_casks)
# Stack1.addCaskToStack(Cask3)
# print (Stack1.stored_casks)
# Stack1.removeCaskFromStack()
# print (Stack1.stored_casks)

# Node1 = Node(1,)
# Node2 = Node()
# Edge1 = Edge()