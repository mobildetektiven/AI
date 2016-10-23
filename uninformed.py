import os 
import classes
from classes import State
import heapq
import copy
from operator import attrgetter

#ut.sort(key = attrgetter('count'), reverse = True)



inf = 99999

class SearchProblem:
	def __init__(self, adj_matrix, node_name_to_num, node_num_to_name,num_nodes, goal_cask, goal_node):
		self.adj_matrix = adj_matrix
		self.goal_cask = goal_cask
		self.goal_node = goal_node
		self.node_name_to_num = node_name_to_num
		self.node_num_to_name = node_num_to_name
		self.num_nodes = num_nodes

		self.fringe = [] #heapifyed using heapq
		self.states_explored = []
		#self.loaded_at_last_visit_to_node = {} #To avoid having to check explored_states so that we can avoid expanding explored states


	def fringeAddState(self, state):
		self.fringe.append(state)
		#f = self.fringe
		#self.fringe = self.sorter(f)
		#self.fringe.reverse()
		self.fringe.sort()
		
		#heapq.heappush(self.fringe,state)
		#heapq.heapify(self.fringe)
		#for el in self.fringe:
		#	print("fringe: ", el.total_cost,el.location)

		self.fringe.reverse()
		#print ("reversing")
		print("")
		for el in self.fringe:
			print("fringe: ", el.total_cost,el.location, "loaded",el.loaded)		
		print("")
		
	def fringeGetCheapestNextState(self):
		try:
			#state = heapq.heappop(self.fringe)
			state = self.fringe.pop()
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
		#loaded = state.loaded_at_last_visit_to_node.get(state.location)
		#print("number of states explored = ", len(self.states_explored))
		#for i in state.loaded_at_last_visit_to_node:
		#	print("elements in explored dict", i, state.loaded_at_last_visit_to_node.get(i))
		#if(loaded == None):
		#	return False

		#elif state.loaded != loaded:
		#		return False
		#else:
		#	print("state explored")
		#	return True
		print("state to check", state.location, "mission number" , state.mission)
		
		if state.previous_state != None:
			if state.previous_state.location == state.location:
				print("happens 1?")
				if state.action == "load" and state.previous_state.action == "unload":
					print("happens 4?")

					return True
				elif state.action == "unload" and state.previous_state.action == "load":
					print("happens 5?")
					return True	

		for prev_state in self.states_explored:
			if(prev_state.location == state.location and prev_state.mission == state.mission):
				same_list = True	
				if(len(state.cask_list) == len(prev_state.cask_list)):
					for num in range(len(state.cask_list)):
						if state.cask_list[num] != prev_state.cask_list[num]:
							same_list = False
							break
				if same_list == True:
					if not state.loaded:
						print("happens 2?")
						return True
					else:
						print("happens 3?")
						cask_name = prev_state.casks_handled.get(state.cask.c_id)
						print("cask name ", state.cask.c_id, "handled",cask_name)
						if cask_name != None:
							return True

							
		return False




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
		#if(state.previous_state != None):
			#print("previous state loc", state.previous_state.location)
			#if(state.location != state.previous_state.location):
		#	state.loaded_at_last_visit_to_node[state.previous_state.location] = state.loaded
		#	state.loaded_at_last_visit_to_node[state.location] = state.loaded
		#print("new state", state.location, state.loaded)
		self.states_explored.append(state)





	def getStateChildren(self,state):
		children = []

		node_has_stack = state.stacks.get(state.location)
		
		#Handle actions load and unload
		if node_has_stack != None:
			#print(node.stack)
			
			#copy stack for next branch level 
			stacks_copy = copy.deepcopy(state.stacks)
			stack_at_current_node = stacks_copy[state.location]
			
			#Check for casks in stack, and if load is possible
			if stack_at_current_node.stackSpaceOccupied() > 0 and not state.loaded:

				print("casks before cask pop")
				for c in stacks_copy[state.location].stored_casks:
					print("cask name", c.c_id)
				cask = stack_at_current_node.removeCaskFromStack()
				cost_of_action = cask.weight + 1
				new_total_cost = (state.total_cost + cost_of_action)
				stacks_copy[state.location] = stack_at_current_node
				print("casks after cask pop")
				#for c in stacks_copy[state.location].stored_casks:
				#	print("cask name", c.c_id)
				
				cask_list = copy.deepcopy(state.cask_list)
				cask_list.append(cask.c_id)
				temp_state = State(state.location,True,cost_of_action,new_total_cost,state,"load", cask, stacks_copy,cask_list, {}, state.mission + 1)
				#temp_state.mission.mission += 1
				print("mission number", temp_state.mission, temp_state.casks_handled)
				if not self.stateExplored(temp_state):
					temp_state.casks_handled[cask.c_id] = True
					children.append(temp_state)
				print("mission number", temp_state.mission, temp_state.casks_handled)

			#If CTS has cask unload if available space in stack
			elif state.loaded:	
				if stack_at_current_node.stackSpaceFree() >= state.cask.length:
					cost_of_action = state.cask.weight + 1
					new_total_cost = (state.total_cost + cost_of_action)

					stack_at_current_node.addCaskToStack(state.cask)
					stacks_copy[state.location] = stack_at_current_node
					temp_state = classes.State(state.location,False,cost_of_action,new_total_cost,state,"unload", None, stacks_copy, state.cask_list,{}, state.mission + 1)
					#temp_state.mission.mission += 1
					if not self.stateExplored(temp_state):
						children.append(temp_state)

		
		#Handle action move
		node_num = self.node_name_to_num.get(state.location)
		if node_num == None:
			print("trying to access undefined Node_num aborting program")
			os.exit(0)

		for col_num in range(0,self.num_nodes):
			if self.adj_matrix[node_num][col_num] < inf:
				location = self.node_num_to_name.get(col_num)
				if location == None:
					print("tried to access unexisting node")
					os.exit(0)
				loaded = state.loaded #if loaded in previous state, it is still loaded after a move
				new_total_cost = state.total_cost # add previous action costs to total cost
				cost_of_action = 0
				
				#calculate cost of move
				if(loaded):
					cost_of_action = (state.cask.weight + 1)*self.adj_matrix[node_num][col_num]
					new_total_cost += cost_of_action
				else:
					cost_of_action = self.adj_matrix[node_num][col_num]
					new_total_cost += cost_of_action

				#create new state, check if it is not already explored					
				temp_state = State(location,loaded,cost_of_action, new_total_cost, state,"move", state.cask, state.stacks,state.cask_list,state.casks_handled, state.mission)
				if not self.stateExplored(temp_state):
					children.append(temp_state)

		#print("el in children", len(children))
		for el in children:
			print("child ", el.location,el.total_cost,el.action,el.cost_of_action)
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

	def sorter(self,fringe):
		for j in range(1, len(fringe)):
			k = fringe[j]
			i = j-1
			while i >= 0 and fringe[i].total_cost > k.total_cost:
				fringe[i+1] = fringe[i]
				i = i - 1
				fringe[i+1] = k
		return fringe