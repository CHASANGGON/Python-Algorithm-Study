from collections import deque
from pprint import pprint
import sys
input = sys.stdin.readline

n, m, p = map(int, input().split())
s_lst = list(map(int, input().split()))
arr = [list(input().rstrip()) for _ in range(n)]
dq_lst = [deque() for _ in range(p)]
# 1. 플레이어들의 위치를 dq에 push
dq = deque()
for i in range(n):
    for j in range(m):
        if arr[i][j].isdigit():
            arr[i][j] = int(arr[i][j])
            dq.append((i, j ,s_lst[arr[i][j]-1], s_lst[arr[i][j]-1])) # 좌표, Sp

# 2. bfs
while dq:
    i, j, Sp, left =  dq.popleft()
    
    for ni, nj in (i+1,j), (i-1,j), (i,j+1), (i,j-1):
        if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == '.':
            arr[ni][nj] = arr[i][j]
            if left - 1 > 0:
                dq.append((ni,nj,Sp, left-1))
            else:
                dq.append((ni,nj,Sp, Sp))

ans = [0] * len(s_lst)
for i in range(n):
    print(arr[i])
for i in range(n):
    for j in range(m):
        ans[arr[i][j]-1] += 1
print(*ans)