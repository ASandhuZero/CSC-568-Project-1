Class Node:
	def __init__(self,value,point)
		self.value = value
		self.point = point
		self.gcost = euclidean(starting node and neighbor node)
		self.hcost = manhattan(starting node and goal node)
	def move_cost(self,other):
		return 0 if self.value == '.' else 1

def succ(point,grid):
    x,y = point.point
    links = [grid[d[0]][d[1]] for d in [(x-1, y),(x,y - 1),(x,y + 1),(x+1,y)]]
return [link for link in links if link.value != '%']

def heuristic(point,point2):
return abs(point.point[0] - point2.point[0]) + abs(point.point[1]-point2.point[0])

def aStar(start, goal, graph)
	# Open and closed sets
	openNodes = set()
	closedNodes = set()
	# Current point is the the starting point
	current = start
	# Add starting point to open set
	openNodes.add(current)
	# While the open nodes set is not empty
	while openNodes:
		# Find the node in openNodes with minimal G + H
		current = min(openNodes, key=lambda, o:o.G + o.H)
		# If this is the correct node, backtrack and return
		if current == goal
			path = []
			while current.parent:
				path.append(current)
				current = current.parent
			path.append(current)
			return path[::-1]
		# Remove node from the open ndoes
		openNodes.remove(current)
		# Add current node to the closed nodes
		closedNodes.add(current)
        	#Iterate through the current node's successors
        	for node in succ(current,grid):
        		# If i already in the closed nodes then skip it   
        		if node in closedNodes:
                		continue
			# Else, it is already in openNodes
			if node in openNodes:
				#Check if we beat the G score 
				new_g = current.G + current.move_cost(node)
				if node.G > new_g:
			# then provide node with a new parent
					node.G = new_g
					node.parent = current
			else:
				#If it isn't in the open set, calculate the G and H score for the node
				node.G = current.G + current.move_cost(node)
				node.H = heuristic(node, goal)
				#Set the parent to our current item
				node.parent = current
				#Add it to the set
				openNodes.add(node)
	#Throw an exception if there is no path
	raise ValueError('No Path Found')
		
		
		
		
		
		if neighbor.walkable=True:
			add neighbors to open list
	order the OpenNodes by fcost
		Then n=first element
	if N=G:
		break, find out what the path is within this loop and return it
	else: n=n+1
		if n.fcost=n+1.fcost
			if n.hcost=n+1.cost:
			

			select min(n.hcost,n+1.hcost)


Priority queues Open and Closed begin empty. 
Put S into Open with priority f(s) = g(s) + h(s)
Is Open empty?
Yes? No solution. 
No. Remove node with lowest f(n). Call it n. 
If n is a goal, stop and report success (for pathfinding, return the path)
Otherwise, expand n. For each n’ in successors(n)
Let f’ = g(n’) + h(n’) = g(n) + cost (n, n’) + h(n’)
If n’ not seen before or n’ previously expanded with f(n’) > f’ or n’ currently in Open with f(n’) > f’ 
Then place or promote n’ on Open with priority f’
Else ignore n’
Place record for n in Closed
