def bfs(start, depth):
    dq = deque([[start, depth]])
    visited = [1] * (n+1)
    while dq:
        now, depth = dq.popleft()
        for nxt in graph[now]:
            if visited[nxt] and depth + 1 <= 2: # 친구의 친구까지만
                visited[nxt] = 0
                dq.append([nxt, depth + 1])
    
    print(visited[2:].count(0))

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
m = int(input())
for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

bfs(1,0)