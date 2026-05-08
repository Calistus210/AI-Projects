from collections import deque
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': ['H'],
    'F': [],
    'G': [],
    'H': []
}

def dfs(graph, start, goal, visited=None, path=None):

    if visited is None:
        visited = set()

    if path is None:
        path = []

    visited.add(start)

    path.append(start)

    print("Visiting Node:", start)

    if start == goal:
        print("\nGoal Node Found!")
        return path
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            result = dfs(graph, neighbor, goal, visited, path.copy())

            if result:
                return result

    return None

start_node = 'A'
goal_node = 'H'

print("=========== DEPTH FIRST SEARCH ===========")
result = dfs(graph, start_node, goal_node)

if result:
    print("\nSearch Path:")
    print(" -> ".join(result))
else:
    print("Goal node not found.")