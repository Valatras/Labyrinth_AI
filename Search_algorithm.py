class PriorityQueue:
	def __init__(self):
		self.data = []

	def enqueue(self, value, priority):
		# Could be better
		self.data.append({'value': value, 'priority': priority})
		self.data.sort(key=lambda elem: elem['priority'])

	def dequeue(self):
		return self.data.pop(0)['value']

	def isEmpty(self):
		return len(self.data) == 0

def BestFS(start, successors, goals, heuristic):
	q = PriorityQueue()
	parent = {}
	parent[start] = None
	q.enqueue(start, heuristic(start))
	while not q.isEmpty():
		node = q.dequeue()
		if node in goals and find_target == True: #remplacer goals (le target) par sa position et faire attention si il se trouve dans notre main
			break
		for successor in successors(node):
			if successor not in parent:
				parent[successor] = node
				q.enqueue(successor, heuristic(successor)) 
		node = None

	res = []
	while node is not None:
		res.append(node)
		node = parent[node]

	return node

def find_target(state):
	board = state["board"]
	target = state["target"]
	for tiles in board:
		if tiles["item"] == target:
			return board.index(tiles)
		else:
			print("il est dans ta main") 
			return False


# comparer sa distance avec la distance du target et lui demander de se rapprocher (colonne,rangee) . A FAIRE

def successors(node):
	laby = party_state["board"]

	directions = [-7, 1, 7, -1] # Nord, est, sud, ouest
	search_path = zip(directions,(laby[current]-1).keys(),laby[current]-1) #pas besoin de "item" 

	res = [] #liste des moves possibles
	for d, direction_current, no_walls_current in search_path: #(-7,north, true)
		new_node = node + d
		if no_walls_current == True:
			if new_node > 48 :
				new_node -= 48
			elif new_node < 0:
				new_node += 48
			
			direction_new_node = ""
			if direction_current == "N":
				direction_new_node = "S"
			elif direction_current == "E":
				direction_new_node = "W"
			elif direction_current == "S":
				direction_new_node = "N"
			elif direction_current == "W":
				direction_new_node = "E"
			
			if laby[new_node][direction_new_node]==True: #check if the new tile has no wall in our direction.
				res.append((new_node))
			
	return res

def heuristic(node):
	return (node - remaining)**2 #prendre les coord de target a la place de (1,9)

print(BestFS(current, successors, target, heuristic)) #target == item id , current est faux on a besoin de party_state[positions][party_state[current]]