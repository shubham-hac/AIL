graph={
    'A':['B', 'C'],
    'B':['D', 'E'],
    'C':['F'],
    'D':['G'],
    'E':[],
    'F':['H','I'],
    'G':[],
    'H':[],
    'I':[]    
}
visited =set()
def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbor in graph[node]:
            dfs(visited,graph,neighbor)
print('Depth First Search')
dfs(visited,graph,'A')