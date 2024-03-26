def bfs():
    global area
    cnt = 1
    while q:
        i,j = q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < m:
                if arr[ni][nj]:
                    cnt += 1
                    arr[ni][nj] = 0
                    q.append([ni,nj])
            
    area = max(area, cnt)
            
            
from collections import deque
import sys
input = sys.stdin.readline
di = [1,-1,0,0]
dj = [0,0,1,-1]
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
picture = 0
area = 0
for i in range(n):
    for j in range(m):
        if arr[i][j]:
            picture += 1
            q = deque()
            q.append([i,j])
            arr[i][j] = 0
            bfs()
          
print(picture)  
print(area)