import os 
import classes

from BuildProblem import inf

class SearchProblem:
	def __init__(self, adj_list, node_name_to_num, node_num_to_name,num_nodes, nodes, stack, casks, goal_cask, goal_node):
		self.adjacency_list = adj_list
		self.goal_cask = goal_cask
		self.goal_node = goal_node
		self.node_name_to_num = node_name_to_num
		self.node node_num_to_name = node_num_to_name
		self.num_nodes = num_nodes
		self.nodes = nodes
		self.stack = stack
		self.cask = cask

		self.fringe = [] #heapifyed using heapq
		self.states_explored = []
		self.loaded_at_last_visit_to_node = {} #To avoid having to check explored_states so that we can avoid expanding explored states


	def fringeAddState(self, state):
		#Add new state to sorted heap
		
	def fringeGetCheapestNextState(self):
		#Return cheapest stat - pop from heapq
		#if new state remains in the same node don't update dict
		#update cts dict for prev state and next state if location is changed
		# add new node to states_explored list

	def stateExplored(self, state):
		#Check if first visit to node, if not, check if state.loaded is in same state as
		#at previous visit if so the state is already explored
		loaded = loaded_at_last_visit_to_node.get(state.location, default=None)
		if(loaded == None):
			return False

		elif state.loaded != loaded:
				return False
		else:
			return True

	def isGoalState(self, state, goal_state):
		#Check if state state is goal state
		if state.location == self.goal_node and state.cask.c_id == self.goal_cask:
			return True
		else:
			return False 

	def solution(self,state):
		#Print steps to solution

	def statesExploredAdd(self,state):
		#Add the explored state and state.loaded to the dictionary
		states_explored[state.location] = state.loaded


	def getStateChildren(self,state):
		node_num = self.node_name_to_num.get(state.location, default = None)
		if node_num == None:
			print("trying to access undefined Node_num aborting program")
			os.exit(0)
		
		node = nodes.get(state.location, default=None)
		if node == None:
			print("trying to access undefined Node aborting program")
			os.exit(0)

		if node.stack != None:
			#load or unload action
			if node.stack.stackSpaceOccupied() > 0 and !state.loaded:
				cask = node.stack.removeCaskFromStack()
				cost_of_action = cask.weight
				new_total_cost = (state.total_cost + cost_of_action + 1)
				temp_state = classes.State(state.location,True,new_total_cost,state,"load", cask)
				if !stateExplored(temp_state):
					fringeAddState(temp_state)

			if state.loaded and (node.stack.stackSpaceFree() >= cask.lenght):
				cost_of_action = cask.weight
				new_total_cost = (state.total_cost + cost_of_action + 1)
				temp_state = classes.State(state.location,False,new_total_cost,state,"unload", None)
				if !stateExplored(temp_state):
					fringeAddState(temp_state)

			#possible moves


		for col in range self.num_nodes:
			if adjacency_list[node_num][col] < inf:
				node = node_num_to_name.get(col, default = None)
				if node == None:
					print("tried to access unexisting node")
					os.exit(0)
				loaded = state.loaded
				new_total_cost = state.total_cost
				if(loaded):
					new_total_cost += (state.cask.weigth + 1)*adj_list[node_num][col]
				else:
					new_total_cost += adj_list[node_num][col]


				temp_state = classes.State(node,loaded,new_total_cost,state,"load", cask)





		#check if state.location (the node we are in) has a stack
			#if so check if loaded = false and stack has cask
			#build new state, location is the same as prev state
			# loaded = true
			# previous state link to previous state in list
			# update weigth 
			# total_cost = state.total_cost + load
			# acton = load
			# add to state_list and fringe

			# if loaded = false and we have cask:
			# new state, location = state.location
			# update weigth
			# total cost update
			# action = unload 
			# prev_state = state 
			# add to fringe

		# find all nodes connect
		# create new state with new node as location
		# total_cost = state.total_cost += cost of move 
		# action = move 
		# add state to fringe



		



	def fringeInsertChild(self,state):
		#Add state to fringe