import os 
import classes
from classes import State
import heapq

inf = 99999

class SearchProblem:
	def __init__(self, adj_matrix, node_name_to_num, node_num_to_name,num_nodes, nodes, goal_cask, goal_node):
		self.adj_matrix = adj_matrix
		self.goal_cask = goal_cask
		self.goal_node = goal_node
		self.node_name_to_num = node_name_to_num
		self.node_num_to_name = node_num_to_name
		self.num_nodes = num_nodes
		self.nodes = nodes


		self.fringe = [] #heapifyed using heapq
		self.states_explored = []
		self.loaded_at_last_visit_to_node = {} #To avoid having to check explored_states so that we can avoid expanding explored states


	def fringeAddState(self, state):
		heapq.heappush(self.fringe,state)
		for el in self.fringe:
			print("fringe: ", el.location,el.total_cost)
		#for elem in self.fringe:
		#	print("fringe",elem.location,elem.total_cost)
		#Add new state to sorted heap
		
	def fringeGetCheapestNextState(self):
		try:
			state = heapq.heappop(self.fringe)
			return state
		except IndexError:
			print("fringe is empty")
			return False
		#Return cheapest stat - pop from heapq
		#if new state remains in the same node don't update dict
		#update cts dict for prev state and next state if location is changed
		# add new node to states_explored list

	def stateExplored(self, state):
		#Check if first visit to node, if not, check if state.loaded is in same state as
		#at previous visit if so the state is already explored
		loaded = self.loaded_at_last_visit_to_node.get(state.location)
		#print("number of states explored = ", len(self.states_explored))
		#for i in self.loaded_at_last_visit_to_node:
		#	print("elements in explored dict", i, self.loaded_at_last_visit_to_node.get(i))
		if(loaded == None):
			return False

		elif state.loaded != loaded:
				return False
		else:
			print("state explored")
			return True

	def isGoalState(self, state, goal_state):
		#Check if state state is goal state
		if(state.cask != None):
			if state.location == self.goal_node and state.cask.c_id == self.goal_cask:
				return True
		else:
			return False 

	def solution(self,state):
		total_cost = state.total_cost
		steps = []
		looping = True
		while looping:
			if(state.action == "move"):
				steps.append(state.action +" "+ state.previous_state.location +" "+state.location +" "+ str(state.cost_of_action))
			elif(state.action == "unload"):
				steps.append(state.action +" "+ state.previous_state.cask.c_id +" "+ state.location + " " + str(state.cost_of_action))

			else:
				steps.append(state.action +" " + state.cask.c_id +" " + state.location + " " + str(state.cost_of_action) )
			if state.previous_state.previous_state == None:
				looping = False	
			else:
				state = state.previous_state
		steps.reverse()
		steps.append(str(total_cost))
		for element in steps:
			print(element)
		return True

	def statesExploredAdd(self,state):
		#Add the explored state and state.loaded to the dictionary
		if(state.previous_state != None):
			#print("previous state loc", state.previous_state.location)
			if(state.location != state.previous_state.location):
				self.loaded_at_last_visit_to_node[state.previous_state.location] = state.loaded
				self.loaded_at_last_visit_to_node[state.location] = state.loaded

		self.states_explored.append(state)





	def getStateChildren(self,state):
		node_num = self.node_name_to_num.get(state.location)
		children = []
		if node_num == None:
			print("trying to access undefined Node_num aborting program")
			os.exit(0)
		
		node = self.nodes.get(state.location)
		if node == None:
			print("trying to access undefined Node aborting program")
			os.exit(0)

		if node.stack != None:
			#print(node.stack)
			#load or unload action
			if node.stack.stackSpaceOccupied() > 0 and not state.loaded :
				cask = node.stack.removeCaskFromStack()
				cost_of_action = cask.weight
				new_total_cost = (state.total_cost + cost_of_action + 1)
				temp_state = classes.State(state.location,True,cost_of_action,new_total_cost,state,"load", cask)
				children.append(temp_state)

			if state.loaded and (node.stack.stackSpaceFree() >= state.cask.length):
				cost_of_action = state.cask.weight
				new_total_cost = (state.total_cost + cost_of_action + 1)
				temp_state = classes.State(state.location,False,cost_of_action,new_total_cost,state,"unload", None)
				children.append(temp_state)
				node.stack.addCaskToStack(state.cask)
			#possible moves


		for col in range(0,self.num_nodes):
			if self.adj_matrix[node_num][col] < inf:
				node = self.node_num_to_name.get(col)
				if node == None:
					print("tried to access unexisting node")
					os.exit(0)
				loaded = state.loaded #if loaded in previous state, it is still loaded
				new_total_cost = state.total_cost # add previous action costs to total cost
				cost_of_action = 0
				if(loaded):
					cost_of_action = (state.cask.weight + 1)*self.adj_matrix[node_num][col]
					new_total_cost += cost_of_action
				else:
					cost_of_action = self.adj_matrix[node_num][col]
					new_total_cost += cost_of_action

				temp_state = classes.State(node,loaded,cost_of_action, new_total_cost, state,"move", state.cask)
				children.append(temp_state)
		#print("el in children", len(children))
		#for el in children:
		#	print("child ", el.location,el.total_cost,el.action,el.cost_of_action)
		return children


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