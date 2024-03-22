def dfs(now, distance):
    visited[now] = distance
    for nxt in graph[now]:
        if visited[nxt] == -1:
            dfs(nxt, distance+1)

import sys
input = sys.stdin.readline

n = int(input())

start, end = map(int, input().split())

m = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

visited = [-1] * (n + 1) # visited 겸 distance를 기록
dfs(start, 0)
print(visited[end])