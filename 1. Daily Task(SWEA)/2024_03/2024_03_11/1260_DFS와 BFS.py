def dfs(now_node):
    visited[now_node] = 0
    print(now_node,end=' ')

    for next_node in edge[now_node]:
        if visited[next_node]:
            dfs(next_node)

def bfs(start_node):
    bfs_queue = deque()
    bfs_queue.append(start_node)
    visited[start_node] = 0
    print(start_node,end=' ')
    while bfs_queue:
        now_node = bfs_queue.popleft()
        for next_node in edge[now_node]:
            if visited[next_node]:
                print(next_node,end=' ')
                visited[next_node] = 0
                bfs_queue.append(next_node)

from collections import deque
import sys
input = sys.stdin.readline

N, M, S = map(int,input().split())

edge = [[] for _ in range(N+1)]

for _ in range(M):
    s, e = map(int,input().split())
    edge[s].append(e)
    edge[e].append(s)

for i in range(1,N+1):
    edge[i].sort()


visited = [1]*(N+1)
dfs(S)

print()

visited = [1]*(N+1)
bfs(S)