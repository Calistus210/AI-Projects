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

def bfs(graph, start, goal):
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        current_node, path = queue.popleft()
        if current_node in visited:
            continue
        visited.add(current_node)
        print("Visiting Node:", current_node)

        if current_node == goal:
            print("\nGoal Node Found!")
            return path

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    return None


start_node = 'A'
goal_node = 'H'

print("=========== BREADTH FIRST SEARCH ===========")
result = bfs(graph, start_node, goal_node)

if result:
    print("\nSearch Path:")
    print(" -> ".join(result))
else:
    print("Goal node not found.")