def bfs():

    visited = [[1]*m for _ in range(n)]
    visited[0][0] = 0
    di = [1,-1,0,0]
    dj = [0,0,1,-1]
    dq = deque()
    dq.append([0,0,1,False]) # i, j, is_wall_break
    
    while dq:
        i, j, time, is_break_wall = dq.popleft()
        if i == n-1 and j == m-1:
            print(time)
            return
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < m and visited[ni][nj]: # 방문한 적 없고
                if arr[ni][nj] == '0': # 길이면
                    visited[ni][nj] = 0 # 방문 체크
                    if is_break_wall: # 벽을 부순 적 있다면
                        dq.append([ni,nj, True]) # True를 append
                    else: # 벽을 부순 적 없다면
                        dq.append([ni,nj, False]) # False를 append
                        
                    
                elif not is_break_wall: # 벽인데, 아직 부순 적 없다면
                    dq.append([ni,nj, True]) # visited 증가시켜서 append
                    visited[ni][nj] = 0
    
    print(-1)
    
from collections import deque
import copy
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [list(input().rstrip()) for _ in range(n)]

bfs()