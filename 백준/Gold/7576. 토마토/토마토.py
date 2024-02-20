from collections import deque


def bfs(q):
    di = [1,-1,0,0]
    dj = [0,0,1,-1]
    day = 0
    
    while q:
        new_q = deque()
        while q:
            i, j = q.popleft()
            for k in range(4):
                if 0 <= i+di[k] < N and 0 <= j+dj[k] < M and tomato[i+di[k]][j+dj[k]] == '0':
                    tomato[i+di[k]][j+dj[k]] = '1'
                    new_q.append([i+di[k],j+dj[k]])
        if new_q:
            day += 1
        q = new_q
                        
    for i in range(N):
        if '0' in tomato[i]:
            return -1
    return day
    

import sys
input = sys.stdin.readline

M, N = map(int,input().split()) # 가로 세로

tomato = [list(input().split()) for _ in range(N)]

# 익은 토마토 찾기
q = deque()
for i in range(N):
    for j in range(M):
        if tomato[i][j] == '1': 
            q.append([i,j]) 
print(bfs(q))