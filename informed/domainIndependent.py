
from uninformed import SearchProblem

# The domain independent searcalgorithm, based on the uniform cost search model 
# All domain specific parts are hidden in the SearchProblem object 
def uniformCostSearch(SearchProblem, goal_state, initial_state):
	state = initial_state
	SearchProblem.fringeAddState(state)
	i = 0
	while True:
		newState = True
		while newState:
			state = SearchProblem.fringeGetCheapestNextState() 
			if state == False:
				return []

			#Check that state returned from fringe is a new state
			if not SearchProblem.stateExplored(state):
				newState = False
		if SearchProblem.isGoalState(state, goal_state):
			return SearchProblem.solution(state)
		
		SearchProblem.statesExploredAdd(state)
		children = SearchProblem.getStateChildren(state)
		for child in children:
			SearchProblem.fringeAddState(child)




def printToFile(list_of_actions, filename):
	try:
		file = open(filename,'wt')
		for line in list_of_actions:
			line += '\n'
			file.write(line)

	except IOError:
		print ("unable to open file")
		os._exit(0)
	file.close()