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
		if self.occupiedStackSize() + arrived_cask.length <= self.size:
			self.stored_casks.append(arrived_cask.length)
		else:
			print ("There is not enough room in this stack!")

	def removeCaskFromStack(self):
		self.stored_casks.pop()

	def occupiedStackSize(self):
		occ_size = 0
		for cask_size in self.stored_casks:
			occ_size += cask_size
		return occ_size


class Edge:
	def __init__(self, e_id, start_node, end_node, length):
		self.e_id = e_id
		self.start_node = start_node
		self.end_node = end_node
		self.length

class Node:
	def __init__(self, n_id, connected_edges):
		




#Testing Code
Cask1 = Cask(1,4,5)
print(Cask1.length)

listOfCasks = [2, 3, 1, 4]
Stack1 = Stack(1,15,listOfCasks)
print (Stack1.stored_casks)
Stack1.addCaskToStack(Cask1)
print (Stack1.stored_casks)
Stack1.removeCaskFromStack()
print (Stack1.stored_casks)