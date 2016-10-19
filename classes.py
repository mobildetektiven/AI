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
			self.stored_casks.append(arrived_cask) #LEGG TIL HELE CASKEN...
		else:
			print ("There is not enough room in this stack!")

	def removeCaskFromStack(self):
		if (self.stored_casks != None):
			self.stored_casks.pop()
		else:
			print ("There are no casks to pick up in this stack!")

			#HER SKAL DU RETURNERE HVA SOM TAES UT AV STACKEN

	def occupiedStackSize(self):
		occ_size = 0
		for cask_size in self.stored_casks:
			occ_size += cask_size
		return occ_size

class Node:
	def __init__(self, n_id, node_number, stack):
		self.n_id = n_id
		self.node_number = node_number
		self.stack = None

# class Edge:
# 	def __init__(self, e_id, end_node_1, end_node_2, length):
# 		self.e_id = e_id
# 		self.end_node_1 = end_node_1
# 		self.end_node_2 = end_node_2
# 		self.length

class State:
	def __init__(self, weight, total_cost, loaded, previous_state, action):
		self.weight = 1
		self.total_cost = 0
		self.loaded = False
		self.previous_state =  None
		self.action = None

class CTS:
	def __init__(self, location, goal_cask):
		self.location = location #In what node or stack is the CTS currently located
		self.loaded = None #Cask
		self.goalCask = goal_cask

	def nextActionList(self):
		#possible moves first
		for node in self.location.
	
	def moveCTS(self, edge):
		if self.location == edge.end_node_1:
			self.location = edge.end_node_2
		elif self.location == end_node_2:
			self.location = edge.end_node_1
		else:
			print ("The CTS is cannot move along this edge!")

	def load(self,cask):
		if (loaded != None):
			Print("The CTS is already loaded - Only one at the time")
		else: 
			loaded = cask

	def unload(self,cask):
		if (loaded == !None):
			print ("There is nothing to unload - The CTS is empty")
		else: 
			loaded = None


#Testing Code
Cask1 = Cask(1,4,5)
print(Cask1.length)

listOfCasks = [Cask1]
print (listOfCasks)
# Stack1 = Stack(1,15,listOfCasks)
# print (Stack1.stored_casks)
# Stack1.addCaskToStack(Cask1)
# print (Stack1.stored_casks)
# Stack1.removeCaskFromStack()
# print (Stack1.stored_casks)

# Node1 = Node(1,)
# Node2 = Node()
# Edge1 = Edge()