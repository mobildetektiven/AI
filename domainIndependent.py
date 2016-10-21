
from  import SearchProblem 


func uniformCostSearch(SearchProblem, goal_state, initial_state):
	state = initial_state
	SearchProblem.fringeAddstate(state)

	while True:
		newState = False
		while !newState:
			state = SearchProblem.fringeGetCheapestNextState() #returns the cheapest state, false if fringe is empty
			if state = False:
				return False
			if !SearchProblem.stateExplored(state):
				newstate = True
		if SearchProblem.isGoalState(state, goal_state):
			return SearchProblem.solution(state)
		SearchProblem.statesExploredAdd(state)
		for child in SearchProblem.getstateChildren(state):
			if !SearchProblem.stateExplored(child):
				SearchProblem.fringeInsertChild(child)





	