def bfs():
    while dq:
        i, j = dq.popleft()
        
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == '1':
                arr[ni][nj] = arr[i][j] + 1
                dq.append([ni, nj])

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(n)]

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

dq = deque()
dq.append([0, 0])
arr[0][0] = 1 # 방문 표시
bfs()
print(arr[n-1][m-1])