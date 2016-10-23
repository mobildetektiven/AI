
#build problem debugs


for node_num in node_num_to_name:
	print(node_num, node_num_to_name[node_num])

i = 0
for row in adj_matrix:
	print(i,row)
	i += 1


for key, stack in stacks.items():
	print(key)
	for cask in stack.stored_casks:
		print(cask.c_id)
stack = stacks["S1"]

a = stack.removeCaskFromStack()
print(a.c_id)

for key, stack in stacks.items():
	i = True
	while i:
		print(stack.s_id)
		cask = stack.removeCaskFromStack()
		if cask == False:
			i = False
		else:
			print(cask.c_id)



#uninformed debugs





#Informed debugs


#classes debug

# class CTS:
# 	def __init__(self, location, goal_cask, state):
# 		self.location = location #In what node or stack is the CTS currently located
# 		self.loaded = None #Cask
# 		self.goalCask = goal_cask
# 		self.state = state

	#def nextActionList(self):
		#possible moves first
	#	for node in self.location
	
	# def moveCTS(self, edge):
	# 	if self.location == edge.end_node_1:
	# 		self.location = edge.end_node_2
	# 	elif self.location == end_node_2:
	# 		self.location = edge.end_node_1
	# 	else:
	# 		print ("The CTS is cannot move along this edge!")

	# def load(self,cask):
	# 	if (loaded != None):
	# 		Print("The CTS is already loaded - Only one at the time")
	# 	else: 
	# 		loaded = cask

	# def unload(self,cask):
	# 	if (loaded != None):
	# 		print ("There is nothing to unload - The CTS is empty")
	# 	else: 
	# 		loaded = None


	# def allowedActions(self, adjacency_list, mode, total_number_of_nodes):  #may find another way to find total_number_of_nodes
	# 	allowed_actions_list = []
	# 	row = self.location.n_id
	# 	for column in total_number_of_nodes:
	# 		if (adjacency_list[row][column] != 0): #gitt at vi setter inn 0 der det ikke ekstisterer edges
	# 			possible_action = move
	# 			possible_target = column

#Testing Code
# Cask1 = Cask(1,5,5)
# Cask2 = Cask(2,5,5)
# Cask3 = Cask(3,5,7)

# listOfCasks = [Cask1,Cask2]
# print (listOfCasks)
# Stack1 = Stack(1,15,listOfCasks)
# print (Stack1.stored_casks)
# Stack1.addCaskToStack(Cask3)
# print (Stack1.stored_casks)
# Stack1.removeCaskFromStack()
# print (Stack1.stored_casks)

# Node1 = Node(1,)
# Node2 = Node()
# Edge1 = Edge()


	
			if(state.loaded):
				if state.location == prev_state.location and prev_state.mission_number == state.mission_number:
					x = prev_state.casks_handled.get(state.cask.c_id)
					print("x = ", x)
					if x != None:
						print("hei",prev_state.location, prev_state.mission_number)
						return True
				if prev_state.loaded:
					if prev_state.cask.c_id == state.cask.c_id and prev_state.location and state.location:
						if prev_state.action == "load" and state.action == "unload":
							return True
						elif prev_state.action == "unload" and state.action == "load":
							return True
				elif:
					



class Mission:
	def __init__(self,mission_number,cask):
		self.mission_number = mission_number
		self.last_cask = cask

		#[action,cask]

	def appendAction(self,action):
		self.actions.append(action)

	def __eq__(self,other):
		if self.mission_number == other.mission_number and self.last_cask == other.last_cask:
			return True


