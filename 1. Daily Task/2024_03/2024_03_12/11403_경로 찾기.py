def dfs(start_v, next_v):
    for next_v in edge[next_v]:
        if visited[next_v]:
            ans[start_v][next_v] = 1
            visited[next_v] = 0
            dfs(start_v, next_v)

import sys
input = sys.stdin.readline

n = int(input())

arr = [list(map(int,input().split())) for _ in range(n)]

edge = [[] for _ in range(n)]

# edge 정보 완성
for i in range(n):
    for j in range(n):
        if arr[i][j]:
            edge[i].append(j)
            
ans = [[0]*n for _ in range(n)]

for start_v in range(n):
    visited = [1]*n
    dfs(start_v,start_v)
    
for i in range(n):
    print(*ans[i])