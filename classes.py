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
		if self.stackSpaceOccupied() + arrived_cask.length <= self.size:
			self.stored_casks.append(arrived_cask)
			for cask in self.stored_casks:
				print("cask in stack", cask.c_id) 
			return True
		else:
			print ("There is not enough room in this stack!")
			return False

	def removeCaskFromStack(self):
		if (len(self.stored_casks) > 0):
			loaded_cask = self.stored_casks.pop()
			#print ("Picking up: ", loaded_cask.c_id)
			return loaded_cask
		else:
			print ("There are no casks to pick up in this stack!")
			return False

	def stackSpaceOccupied(self):
		occ_size = 0
		for cask in self.stored_casks:
			occ_size += cask.length
		print("space occupied ", occ_size)
		return occ_size

	def stackSpaceFree(self):
		occ_size = 0
		for cask in self.stored_casks:
			occ_size += cask.length
		return self.size - occ_size		

class Node:
	def __init__(self, n_id, node_number, stack):
		self.n_id = n_id
		self.node_number = node_number
		self.has_stack = None

class Edge:
	def __init__(self, end_node_1, end_node_2, length):
		self.end_node_1 = end_node_1
		self.end_node_2 = end_node_2
		self.length = length

class State:
	def __init__(self, node,loaded, cost_of_action,total_cost, previous_state, action, cask, stacks, cask_list, casks_handled, mission):
		self.location = node
		self.loaded = loaded
		self.cost_of_action = cost_of_action
		self.total_cost = total_cost
		self.cask = cask

		#variables to simplify outputting solution
		self.previous_state =  previous_state
		self.action = action
		self.stacks = stacks #dict holding all stacks and casks for this branch 
		self.casks_handled = casks_handled
		self.cask_list = cask_list
		self.mission = mission

	#function to enable use of heapq

	def __lt__(self, other):
		return self.total_cost < other.total_cost

	#def __cmp__(self,other):
	#	return cmp(self.total_cost,other)
