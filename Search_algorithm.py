import copy

def showBoard(board):
    mat = []
    for i in range(28):
        mat.append([])
        for j in range(28):
            mat[i].append(" ")
    for index, value in enumerate(board):
        i = (index // 7) * 4
        j = (index % 7) * 4
        mat[i][j] = "#"
        mat[i][j + 1] = "#" if not value["N"] else " "
        mat[i][j + 2] = "#"
        mat[i][j + 3] = "|"
        mat[i + 1][j] = "#" if not value["W"] else " "
        mat[i + 1][j + 1] = (
            " " if value["item"] is None else chr(ord("A") + value["item"])
        )
        mat[i + 1][j + 2] = "#" if not value["E"] else " "
        mat[i + 1][j + 3] = "|"
        mat[i + 2][j] = "#"
        mat[i + 2][j + 1] = "#" if not value["S"] else " "
        mat[i + 2][j + 2] = "#"
        mat[i + 2][j + 3] = "|"
        mat[i + 3][j] = "-"
        mat[i + 3][j + 1] = "-"
        mat[i + 3][j + 2] = "-"
        mat[i + 3][j + 3] = "-"

    print("\n".join(["".join(line) for line in mat]))

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

def BestFS(start, successors, heuristic, state, free_tile):
	q = PriorityQueue()
	parent = {}
	parent[start[2]] = None
	target_pos = find_target(state)
	q.enqueue(start, heuristic(start[2], target_pos)) #plus l'heuristic est petit meilleur est le move.
	while not q.isEmpty():
		target_pos = find_target(state)
		node = q.dequeue() #node = [ft_oriented, gate, pos]
		if node[2] == target_pos or target_pos == True: #remplacer goals (le target) par sa position et faire attention si il se trouve dans notre main
			
			node = [free_tile, 'K', node[2]] #devoir mettre la tuile a coter de nous => successor(node) avec tuile_orientation a choisir et prendre la gate a coter de nous
			print('terminer')
			return node
		for successor in successors(node[2], free_tile, state): #modifier node ou res pour envoyer correctement un move
			
			if successor not in list(parent.keys()):
				parent[successor[2]] = node[2]
				q.enqueue(successor, heuristic(successor[2], target_pos))
		answer = q.dequeue()
		print(answer)
		return(answer)
		
		

	#changer BFS pour qu'il renvoie le res avec la meilleur priorite.
	#print(node)
	 #node  


def find_target(state):
	board = copy.copy(state["board"][:-1])
	target = copy.copy(state["target"])
	for tiles in board:
		if tiles["item"] == target:
			print('le tresor se trouve sur la tuile ' + str(board.index(tiles)))
			return board.index(tiles)
	
	print("il est dans ta main") 
	print(state['board'])
	return False




def successors(node, free_tile, state):
	board = copy.copy(state["board"])

	directions = [-7, 1, 7, -1] # Nord, est, sud, ouest
	 
	res = [] #liste des moves possibles

	#ajouter la tuile libre avec toute ses orientations et toutes les portes sur lesquels la placer. Ne pas oublier de deplacer les tuiles 
	#dans party_state['board']
	
	#keys and vals of the free tile directions
	free_tile_dir = copy.copy(free_tile)
	free_tile_dir.popitem()
	ft_keys = list((free_tile_dir).keys()) 
	ft_vals = list((free_tile_dir).values())

	#use the free tile in the four orientations
	for i in range(0,4):
		ft_vals.append(ft_vals[0])
		ft_vals.pop(0)
		for key,val in zip(ft_keys, ft_vals):
			free_tile[key] = val

		#use them in each gate
		gates = {'A':1 ,'B':3 ,'C':4 ,'D':13 ,'E':27 ,'F':41 ,'G':47 ,'H':45 ,'I':43 ,'J':35 ,'K':21 ,'L':7 }
		for gate,gate_ind in zip(gates.keys(), gates.values()):
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
						
					
			board[gate_ind] = free_tile #la tuile de i = 0 est remplacer par free tile
					




			#now that the board is ready, search and add every move you can do
			current = state['current']
			current_dir = copy.copy(board[current])
			current_dir.popitem()
			search_path = zip(directions, current_dir.keys(), current_dir.values()) #-1 car pas besoin de "item"

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
						res.append((free_tile,gate,new_node))

			board = copy.copy(state["board"]) #reupload the basic board after each tried move 
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

##print(BestFS((None, None ,state['current']), successors, heuristic, state, state['board'][49])) #target == item id , current est faux on a besoin de party_state[positions][party_state[current]]