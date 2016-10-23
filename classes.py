
#All classes used to solve the Search problem 

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
			return True
		else:
			return False

	def removeCaskFromStack(self):
		if (len(self.stored_casks) > 0):
			loaded_cask = self.stored_casks.pop()
			return loaded_cask
		else:
			return False

	def stackSpaceOccupied(self):
		occ_size = 0
		for cask in self.stored_casks:
			occ_size += cask.length
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


# Class used to represent the state of the CTS and to ensure no repeated states
class State:
	def __init__(self, location,loaded, cost_of_action,total_cost, previous_state, action, cask, stacks, cask_list, casks_handled, mission_num):
		self.location = location
		self.loaded = loaded
		self.cost_of_action = cost_of_action
		self.total_cost = total_cost
		self.cask = cask
		self.previous_state =  previous_state
		self.action = action
		self.stacks = stacks

	#variables only used to avoid repeated states 
		#Used to ensure a cask is not rehandled in the same mission 
		self.casks_handled = casks_handled
		#list of all casks that has been onboard the CTS, sorted
		self.cask_list = cask_list
		#For each time a cask is either loaded or unloaded, the misson num is increased
		self.mission_num = mission_num

	#To enable comparison of two states 
	def __lt__(self, other):
		return self.total_cost < other.total_cost