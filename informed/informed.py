import os 
import classes
from classes import State
import heapq
import copy
from operator import attrgetter

#global variable exported to Build problem
inf = 99999

# Class SearchProblem, takes info from buildproblem, and follows commands from 
# our domainindependet uniform cost search algorithm
class SearchProblem:
	def __init__(self, adj_matrix, node_name_to_num, node_num_to_name,num_nodes, goal_cask_name, goal_node):
		self.adj_matrix = adj_matrix
		self.goal_cask_name = goal_cask_name
		self.goal_node = goal_node
		self.node_name_to_num = node_name_to_num
		self.node_num_to_name = node_num_to_name
		self.num_nodes = num_nodes

		self.fringe = [] #heapifyed using heapq
		self.states_explored = []
		self.number_of_explored_states = 0


	def fringeAddState(self, state):
		self.fringe.append(state)
		self.fringe.sort()
		self.fringe.reverse()
		
		#heapq.heappush(self.fringe,state)
		#heapq.heapify(self.fringe)
		
		#------------------------------remove later--------------------------
		print("")
		for el in self.fringe:
			print("fringe: ", el.total_cost,el.location, "loaded",el.loaded)		
		print("")
		#--------------------------------remove later -----------------------
		
	def fringeGetCheapestNextState(self):
		try:
			#state = heapq.heappop(self.fringe)
			state = self.fringe.pop()
			return state
		except IndexError:
			print("fringe is empty")
			return False
		
	def stateExplored(self, state):
		#------------------------------remove ------------------------------------	
		print("state to check", state.location, "mission number" , state.mission_num)
		#-------------------------------------------------------------------------		
		
		if state.previous_state != None:
			if state.previous_state.location == state.location:
				if state.action == "load" and state.previous_state.action == "unload":
					return True

				elif state.action == "unload" and state.previous_state.action == "load":
					return True	

		for prev_state in self.states_explored:
			if(prev_state.location == state.location and prev_state.mission_num == state.mission_num):
				same_list = True	
				if(len(state.cask_list) == len(prev_state.cask_list)):
					for num in range(len(state.cask_list)):
						if state.cask_list[num] != prev_state.cask_list[num]:
							same_list = False
							break
				if same_list == True:
					if not state.loaded:
						return True
					else:
						cask_name = prev_state.casks_handled.get(state.cask.c_id)
						if cask_name != None:
							return True
		return False




	def isGoalState(self, state, goal_state):
		if(state.cask != None):
			if state.location == self.goal_node and state.cask.c_id == self.goal_cask_name:
				return True
		else:
			return False 

	#Build list with all steps taken to get the solution return the list
	def solution(self,state):
		print("total number of explored states = ",self.number_of_explored_states)
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
		return steps

	def statesExploredAdd(self,state):
		self.number_of_explored_states += 1
		self.states_explored.append(state)





	def getStateChildren(self,state):
		children = []
		node_has_stack = state.stacks.get(state.location)
		
		#Handle actions load and unload:
		if node_has_stack != None:

			#copy stack for next branch level 
			stacks_copy = copy.deepcopy(state.stacks)
			stack_at_current_node = stacks_copy[state.location]
			
			#Check for casks in stack, and if load is possible
			if stack_at_current_node.stackSpaceOccupied() > 0 and not state.loaded:
				cask = stack_at_current_node.removeCaskFromStack()
				cost_of_action = cask.weight + 1
				new_total_cost = (state.total_cost + cost_of_action)
				stacks_copy[state.location] = stack_at_current_node

				#calculate the heuristic
			

				
				cask_list = copy.deepcopy(state.cask_list)
				cask_list.append(cask.c_id)
				temp_state = State(state.location,True,cost_of_action,new_total_cost,state,"load", cask, stacks_copy,cask_list, {}, state.mission_num + 1,0)
				temp_state.calculateHeuristic(cask,new_total_cost,self.goal_cask_name)
				if not self.stateExplored(temp_state):
					temp_state.casks_handled[cask.c_id] = True
					children.append(temp_state)

			#If CTS has cask unload if available space in stack
			elif state.loaded:	
				if stack_at_current_node.stackSpaceFree() >= state.cask.length:
					cost_of_action = state.cask.weight + 1
					new_total_cost = (state.total_cost + cost_of_action)
					state.cask.blocking_goal_cask = False
					stack_at_current_node.addCaskToStack(state.cask)
					stacks_copy[state.location] = stack_at_current_node
					temp_state = classes.State(state.location,False,cost_of_action,new_total_cost,state,"unload", None, stacks_copy, state.cask_list,{}, state.mission_num + 1,0)
					temp_state.calculateHeuristic(state.cask,new_total_cost,self.goal_cask_name)
					if not self.stateExplored(temp_state):
						children.append(temp_state)

		
		#Handle action move:
		node_num = self.node_name_to_num.get(state.location)
		if node_num == None:
			print("trying to access undefined Node_num aborting program")
			os._exit(0)

		for col_num in range(0,self.num_nodes):
			if self.adj_matrix[node_num][col_num] < inf:
				location = self.node_num_to_name.get(col_num)
				if location == None:
					print("tried to access unexisting node")
					os._exit(0)
				loaded = state.loaded
				new_total_cost = 0
				cost_of_action = 0
				
				#calculate cost of move
				if(loaded):
					cost_of_action = (state.cask.weight + 1)*self.adj_matrix[node_num][col_num]
					new_total_cost += cost_of_action + state.total_cost
				else:
					cost_of_action = self.adj_matrix[node_num][col_num]
					new_total_cost += cost_of_action + state.total_cost

				#create new state, check if it is not already explored before appending to list of children					
				temp_state = State(location,loaded,cost_of_action, new_total_cost, state,"move", state.cask, state.stacks,state.cask_list,state.casks_handled, state.mission_num,0)
				temp_state.calculateHeuristic(state.cask,new_total_cost,self.goal_cask_name)
				if not self.stateExplored(temp_state):
					children.append(temp_state)
		return children
