def bfs():
    while dq:
        i, j, cnt = dq.pop()
        print(cnt)
        # 탈출 조건
        if i == n-1 and j == m-1:
            print(cnt)
            return
        
        # 탐색
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == '1':
                arr[ni][nj] = 0
                dq.append([ni,nj,cnt+1])

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
arr = [list(input().rstrip()) for _ in range(n)]

di = [1,-1,0,0]
dj = [0,0,1,-1]
dq = deque()
dq.append([0,0,0])
arr[0][0] = 0
bfs()
