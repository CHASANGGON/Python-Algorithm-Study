def bfs(dq):
    
    while dq:
        i, j = dq.popleft()
        if i == ei and j == ej:
            print(arr[i][j])
            return
        for k in range(8):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < l and 0 <= nj < l and arr[ni][nj] == -1:
                arr[ni][nj] = arr[i][j] + 1
                dq.append([ni,nj])
                
                

from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

di = [2,1,-2,-1,2,1,-2,-1]
dj = [1,2,1,2,-1,-2,-1,-2]

for _ in range(t):
    l = int(input())
    arr = [[-1]*l for _ in range(l)]
    si, sj = map(int, input().split())
    ei, ej = map(int, input().split())
    dq = deque([[si, sj]])
    arr[si][sj] = 0 # visited
    bfs(dq)