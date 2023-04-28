graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': [],
    'F': ['H', 'I'],
    'G': [],
    'H': [],
    'I': []
}

def dls(start, goal, path, level, maxD):
    print('\nCurrent level', level)
    print('Goal node testing for', start)
    path.append(start)
    
    if start == str(goal):
        print('\nGoal test successful')
        return path

    print('\nGoal test failed')
    if level == maxD:
        return False

    print('\nExpanding the current node', start)
    for child in graph[start]:
        if dls(child, goal, path, level + 1, maxD):
            return path
    path.pop()
    return False

start = 'A'
goal = input('Enter the goal node: ')
maxD = int(input('Enter the maximum depth limit: '))
print()
path = []
res = dls(start, goal, path, 0, maxD)

if res:
    print('Path to goal node available')
    print('Path:', path)
else:
    print('No path available for the goal node in the given depth limit')  