graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

def DFS(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop() # Get next node
        if vertex not in visited: # If it hasn't been seen before
            visited.add(vertex) # Add to seen
            stack.extend(graph[vertex] - visited) #Extend the stack by all the vertexes that haven't been seen yet
    return visited

def DFS_Path(graph, start, goal, path = None):
    if path is None:
        path = [start]
    if start == goal: 
        yield path
    for next in graph[start] - set(path):
        yield from DFS_Path(graph, next, goal, path + [next])
    
solution = list(DFS_Path(graph,'A','F'))
print(solution)