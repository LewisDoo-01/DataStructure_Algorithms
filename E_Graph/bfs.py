# a python dictionary for the adjacency 
# list of a graph
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = [] # list for visited nodes.
queue = []     # initialize a queue

# function for the bfs algorithm
def bfs(visited, graph, node): 
  visited.append(node)
  queue.append(node)

  # creating loop to visit each node
  while queue:          
    m = queue.pop(0) 
    print (m, end = " ") 

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

# driver code
print("the BFS traverse on Graph:")
bfs(visited, graph, '5')    