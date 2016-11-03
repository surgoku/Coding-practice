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




    
def floydWarshall(graph):
    # assuming the graph has INF or large number for disconnected nodes
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
    
    
    
    