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
visited=set()
queue=[]
def bfs(visited,graph,node):
    visited.add(node)
    queue.append(node)
    while queue:
        m=queue.pop(0)
        print(m,'\n',end="")
        for adjacent in graph:
            if adjacent not in visited:
                visited.add(adjacent)
                queue.append(adjacent)
print("Breadth-first Search")
bfs(visited,graph,'A')