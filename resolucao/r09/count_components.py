# Python3 program to find unique count of 
# connected components 
graph = [[] for i in range(100 + 1)] 
visited = [False] * (100 + 1) 
ans = 0

# Function to add edge in the garph 
def add_edge(u, v): 
	
	graph[u].append(v) 
	graph[v].append(u) 

# Function to traverse the undirected graph 
# using DFS algorithm and keep a track of 
# individual lengths of connected chains 
def depthFirst(v): 
	
	global ans 
	
	# Marking the visited vertex as true 
	visited[v] = True
	print(v, end = " ") 
	#print(ans,end="-") 

	# Incrementing the count of 
	# connected chain length 
	ans += 1

	for i in graph[v]: 
		if (visited[i] == False): 
			
			# Recursive call to the 
			# DFS algorithm 
			depthFirst(i) 

# Function to initialize the graph 
# and display the result 
def UniqueConnectedComponent(n): 
	
	global ans 

	# Initializing boolean visited array 
	# to mark visited vertices 

	# Initializing a Set container 
	result = {} 

	# Following loop invokes DFS algorithm 
	for i in range(1, n + 1): 
		if (visited[i] == False): 
			
			# ans variable stores the 
			# individual counts 
			# ans = 0 

			# DFS algorithm 
			depthFirst(i) 

			# Inserting the counts of connected 
			# components in set 
			result[ans] = 1
			print("Count = ", ans) 
			ans = 0

	print("Unique Counts of connected "
		"components: ", end = "") 

	# The size of the Set container 
	# gives the desired result 
	print(len(result)) 

# Driver code 
if __name__ == '__main__': 
	
	# Number of nodes 
	n = 7

	# Create graph 

	# Constructing the undirected graph 
	add_edge(1, 2) 
	add_edge(3, 4) 
	add_edge(3, 5) 
	add_edge(6, 7) 

	# Function call 
	UniqueConnectedComponent(n) 

# This code is contributed by mohit kumar 29 

