import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)
for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)
    
from collections import deque
dq = deque()
dq.append((1,1)) # node, order
visited[1] = 1
while dq:
    now, order =  dq.popleft()
    
    for nxt in graph[now]:
        if visited[nxt] == 0:
            visited[nxt] = order + 1
            dq.append((nxt, order+1))

dist = [0]
for i in range(1,n+1):
    if visited[i] > dist[0]:
        dist = [visited[i]]
        dist_idx = i
    elif visited[i] == dist[0]:
        dist.append(visited[i])

print(dist_idx, dist[0] - 1, len(dist))