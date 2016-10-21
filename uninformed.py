class SearchProblem:
	def __init__(self, adjacency_list):
		self.adjacency_list = adjacency_list
		self.CTS_state_last_visit_to_node = {} #To avoid having to check explored_states so that we can avoid expanding explored states
		self.fringe = [] #heapifyed using heapq
		self.states_explored = []
	def fringeAddState(self, state):
		#Add new state to sorted heap
		
	def fringeGetCheapestNextState(self):
		#Return cheapest stat - pop from heapq
	def stateExplored(self, state):
		#Check if state is explored
	def isGoalState(self, state):
		#Check if state state is goal state
	def solution(self,state):
		#Print steps to solution
	def statesExploredAdd(self,state):
		#Add the explored state to the dictionary
	def getStateChildren(self,state):
		#Check if state (node) has children and return as states
	def fringeInsertChild(self,state):
		#Add state to fringe