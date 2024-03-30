def bfs(i, j):
    dq = deque([[i,j]])
    arr[i][j] = 0
    cnt = 1

    while dq:
        i,j = dq.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < m and 0 <= nj < n and arr[ni][nj]:
                arr[ni][nj] = 0
                dq.append([ni,nj])
                cnt += 1
                
    return cnt


di = [1,-1,0,0]
dj = [0,0,1,-1]

from collections import deque
import sys
input = sys.stdin.readline

m, n, k = map(int, input().split())

arr = [[1] * (n) for _ in range(m)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    lst = [(x1, y1), (x2, y2)]
    lst.sort()
    for y in range(lst[0][1], lst[1][1]):
        for x in range(lst[0][0], lst[1][0]):
            arr[y][x] = 0


ans = []
for i in range(m):
    for j in range(n):
        if arr[i][j]:
            ans.append(bfs(i, j))
    
ans.sort()
print(len(ans))
print(*ans)