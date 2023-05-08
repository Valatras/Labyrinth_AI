class PriorityQueue:
	def __init__(self):
		self.data = []

	def enqueue(self, value, priority):
		# Could be better
		self.data.append({'value': value, 'priority': priority}) #priority == heuristic()
		self.data.sort(key=lambda elem: elem['priority'])

	def dequeue(self):
		return self.data.pop(0)['value']

	def isEmpty(self):
		return len(self.data) == 0

def BestFS(start, successors, goals, heuristic, state, free_tile):
	q = PriorityQueue()
	parent = {}
	parent[start] = None
	q.enqueue(start, heuristic(start)) #plus l'heuristic est petit meilleur est le move.
	while not q.isEmpty():
		node = q.dequeue()
		if node == find_target(state) or find_target(state) == False: #remplacer goals (le target) par sa position et faire attention si il se trouve dans notre main
			if find_target(state) == False:
				pass #devoir mettre la tuile a coter de nous => successor(node) avec tuile_orientation a choisir et prendre la gate a coter de nous
			break
		for successor in successors(node, free_tile, state):
			if successor not in parent:
				parent[successor] = node
				q.enqueue(successor, heuristic(successor)) 
		node = None

	#changer BFS pour qu'il renvoie le res avec la meilleur priorite.
	res = []
	while node is not None:
		res.append(node)
		node = parent[node]

	return node #node = new pos, 


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

def successors(node, free_tile,state):
	board = state["board"]

	directions = [-7, 1, 7, -1] # Nord, est, sud, ouest
	 
	res = [] #liste des moves possibles

	#ajouter la tuile libre avec toute ses orientations et toutes les portes sur lesquels la placer. Ne pas oublier de deplacer les tuiles 
	#dans party_state['board']
	
	#keys and vals of the free tile directions
	ft_keys = list((board[free_tile]-1).keys()) 
	ft_vals = list((board[free_tile]-1).values())

	#use the free tile in the four orientations
	for i in range(0,4):
		ft_vals.append(ft_vals[0])
		ft_vals.pop(0)
		for key,val in (ft_keys, ft_vals):
			board[free_tile][key] = val

	#use them in each gate
		for gate,gate_ind in {'A':1 ,'B':3 ,'C':4 ,'D':13 ,'E':27 ,'F':41 ,'G':47 ,'H':45 ,'I':43 ,'J':35 ,'K':21 ,'L':7 }:
			new_current = False
			changed_current = False # pour eviter que la position du pion est changer deux fois (example : 13->7->8)
			
			for i in reversed(range(7)): #(6,5,4,3,2,1,0)
				if gate in ['A','B','C']:
					step = 7
				if gate in ['D','E','F']:
					step = -1
				if gate in ['G','H','I']:
					step = -7
				if gate in ['J','K','L']:
					step = 1

				#verifier si on se trouve sur une tuile de la porte.
				if state['current'] == gate_ind + step*i:
					new_current == True

				if i != 0:
					board[gate_ind+step*i] = board[gate_ind+step*(i-1)]

				if new_current == True and changed_current == False:
					if i != 6:
						state['current'] += step
					else:
						state['current'] -= 6*step
					new_current == False
					changed_current == True 
						
					
			board[gate_ind] = board[free_tile] #la tuile de i = 0 est remplacer par free tile
					




			#now that the board is ready, search and add every move you can do
			search_path = zip(directions,(board[state['current']]-1).keys(),board[state['current']]-1) #-1 car pas besoin de "item"

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
					
					if board[new_node][direction_new_node]==True: #check if the new tile has no wall in our direction.
						res.append((board[free_tile],gate,new_node))

			board = state["board"] #reupload the basic board after each tried move 
				
	return res #[0] is the free tile in the good orientation, [1] is the gate, [2] is the final pos

def cord(tile):
	x = tile%7
	y = (tile-(tile%7))/7
	return [x,y]

#compare la nouvelle position avec la position du target
def heuristic(new_node, target):
	target_cord = cord(target)
	new_node_cord = cord(new_node)
	new_node_remaining = (sum((target_cord[i]-new_node_cord[i])**2 for i in range(0,2)))**0.5 #pythagore 
	return new_node_remaining 

print(BestFS(state[current], successors, state[target], heuristic, state, state[board][49])) #target == item id , current est faux on a besoin de party_state[positions][party_state[current]]