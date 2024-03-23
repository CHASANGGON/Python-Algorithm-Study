def dfs(i, j):
    visited[i][j] = 0
    stack = [[i, j]]
    
    while stack:
        i, j = stack.pop()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] > water and visited[ni][nj]:
                visited[ni][nj] = 0
                stack.append([ni,nj])


import copy
import sys
input = sys.stdin.readline

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

di = [1,-1,0,0]
dj = [0,0,1,-1]
ans = 1
for water in range(min(map(min, arr)), max(map(max, arr)) + 1):
    visited = [[1] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] > water and visited[i][j]:
                dfs(i, j)
                cnt += 1
    
    ans = max(ans, cnt)
    
print(ans)