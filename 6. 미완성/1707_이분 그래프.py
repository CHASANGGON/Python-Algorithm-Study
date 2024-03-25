def dfs(start, now_tag):
    stack = [start]
    while stack:
        next_tag = now_tag % 2 + 1
        now = stack.pop()
        for nxt in graph[now]:
            if tag[nxt]:
                tag[nxt] = next_tag
            elif tag[nxt] != :
            
    

t = int(input())
for _ in range(t):
    V, E = map(int, input().split()) # 정점(1~V) 개수, 간선 개수
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
        
    tag = [1] * (V+1)
    for i in range(1,V+1):
        if tag[i]:
            dfs(i, tag[i])
