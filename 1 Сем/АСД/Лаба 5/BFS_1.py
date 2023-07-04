import collections
def bfs(graph, root): 
    visited, q = set(), collections.deque([root])
    visited.add(root)
    while q: 
        vertex = q.popleft()
        for neighbour in graph[vertex]: 
            if neighbour not in visited: 
                visited.add(neighbour) 
                q.append(neighbour)
                print(visited)

adj = [    
    [1,3],      # 0
    [0,3,4,5],  # 1
    [4,5],      # 2
    [0,1,5],    # 3
    [1,2],      # 4
    [1,2,3]     # 5
]
bfs(adj, 0)
