from collections import defaultdict, deque

# Please dont use this code in production as debug is needed and optimaization is needed.
def heuristic(node, goal):
    x1, y1 = node
    x2, y2 = goal
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def a_star(graph, start, goal):
    open_set = deque()
    open_set.append((0, start))
    came_from = {}
    g_score = defaultdict(lambda: float('inf'))
    g_score[start] = 0
    f_score = defaultdict(lambda: float('inf'))
    f_score[start] = heuristic(start, goal)

    while open_set:
        current = open_set.popleft()[1]

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path

        for neighbor in graph[current]:
            temp_g_score = g_score[current] + graph[current][neighbor]

            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + heuristic(neighbor, goal)
                open_set.append((f_score[neighbor], neighbor))

    return None

# Example usage
graph = {
    'A': {'B': 5, 'C': 3},
    'B': {'D': 2, 'E': 4},
    'C': {'F': 6},
    'D': {'G': 1},
    'E': {},
    'F': {'H': 7, 'I': 8},
    'G': {},
    'H': {},
    'I': {}
}

start = 'A'
goal = 'I'

path = a_star(graph, start, goal)

if path:
    print("Path found:", path)
else:
    print("No path found from", start, "to", goal)
