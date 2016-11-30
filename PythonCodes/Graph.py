'''
Created on Oct 31, 2016

@author: root
'''
import path


def dfsIterative(graph, vertex):
    visited = set()
    stack = [vertex]
    while stack:
        curr = stack.pop()
        if curr not in visited:
            visited.add(curr)
            stack.extend(graph[curr] - visited)
    return visited

def bfsIterative(graph, vertex):
    visited = set()
    queue = [vertex]
    while queue:
        curr = queue.pop(0)
        if curr not in visited:
            visited.add(curr)
            queue.extend(graph[curr]-visited)
    return visited

def dfsPathIterative(graph, start, end):
    stack = [(start, [start])]
    while stack:
        curr, path = stack.pop()
        for neighbor in graph[curr] - set(path):
            if neighbor == end:
                yield path + [neighbor]
            else:
                stack.append((neighbor, path + [neighbor]))
    
def bfsPathIterative(graph, start, end):
    queue = [(start, [start])]
    while queue:
        curr, path = queue.pop(0)
        for neighbor in graph[curr] - set(path):
            if neighbor == end:
                yield path + [neighbor]
            else:
                queue.append((neighbor, path.append(neighbor)))
                
    
def dfsRecur(graph, vertex, visited):
    visited.add(vertex)
    for neigbour in graph[vertex] - visited:
        dfsRecur(graph, neigbour, visited)
    return visited


def Dijkstra():
    # minimum edge distance from one vertex to all vertex.
    nodes = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
    distances = {
        'B': {'A': 5, 'D': 1, 'G': 2},
        'A': {'B': 5, 'D': 3, 'E': 12, 'F' :5},
        'D': {'B': 1, 'G': 1, 'E': 1, 'A': 3},
        'G': {'B': 2, 'D': 1, 'C': 2},
        'C': {'G': 2, 'E': 1, 'F': 16},
        'E': {'A': 12, 'D': 1, 'C': 1, 'F': 2},
        'F': {'A': 5, 'E': 2, 'C': 16}}
    
    unvisited = {node: None for node in nodes} #using None as +inf
    visited = {}
    current = 'B'
    currentDistance = 0
    unvisited[current] = currentDistance
    
    while True:
        for neighbour, distance in distances[current].items():
            if neighbour not in unvisited: continue
            newDistance = currentDistance + distance
            if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
                unvisited[neighbour] = newDistance
        visited[current] = currentDistance
        del unvisited[current]
        if not unvisited: break
        candidates = [node for node in unvisited.items() if node[1]]
        current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]
    
    print(visited)
    
def PrimsMinimumSpanningTree(root):
    #minimum edge from each node to every node
    # start with any node and find the nearest node in terms of weight and do that for all the nodes.
     
    pass

    
    
def floydWarshall(graph):
    # assuming the graph has INF or large number for disconnected nodes
    # All pair shortest path
    nodes = graph.keys()
    updated_graph = {}
    
    for i in nodes:
        updated_graph[i] = {}
        for j in nodes:
            updated_graph[i][j] = graph[i][j]
            if i==j:
                updated_graph[i][j] = 0
            
    
    for k in nodes: # this loop or node required to find the path through alternative node apart from direct connection
        for i in nodes:
            for j in nodes:
                # i, j are the nodes that we really want to update. However, k is used for path through alternative node
                # if distance through alternative path is less expensive update
                if updated_graph[i][k] + updated_graph[k][j] < updated_graph[i][j]:
                    updated_graph[i][j] = updated_graph[i][k] + updated_graph[k][j]
                    
    return updated_graph


def aStarSearch(graph, start, end):
    # this is best first algorithm
    pass

def findNearestDoorMazeProblem():
    #bfs
    # floyd warshal
    pass





def run():
    graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}
    
    
    
    