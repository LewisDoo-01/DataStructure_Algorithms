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

visited = []

# function for the dfs algorithm 
def dfs(visited, graph, node):  
    if node not in visited:
        print (node)
        visited.append(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# driver code
print("the DFS traverse on Graph:")
dfs(visited, graph, '5')