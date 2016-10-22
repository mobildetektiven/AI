
from uninformed import SearchProblem
import time

def uniformCostSearch(SearchProblem, goal_state, initial_state):
	state = initial_state
	SearchProblem.fringeAddState(state)

	while True:
		newState = False
		while not newState:
			state = SearchProblem.fringeGetCheapestNextState() #returns the cheapest state, false if fringe is empty
			if state == False:
				return False
			if not SearchProblem.stateExplored(state):
				newState = True
		if SearchProblem.isGoalState(state, goal_state):
			return SearchProblem.solution(state)
		if(state.loaded):
			print("my current state", state.location,state.loaded, state.total_cost, state.cask.c_id)
		else:
			print("my current state", state.location,state.loaded, state.total_cost)
		SearchProblem.statesExploredAdd(state)
		children = SearchProblem.getStateChildren(state)
		for child in children:
			if not SearchProblem.stateExplored(child):
				#print("new state to add: ", child.location,child.total_cost)
				SearchProblem.fringeAddState(child)
		time.sleep(.1)
		#print(state.location,state.total_cost)




	