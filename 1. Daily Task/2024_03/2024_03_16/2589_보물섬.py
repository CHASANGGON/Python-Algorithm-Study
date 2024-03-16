def in_range(ni,nj):
    return 0 <= ni < N and 0 <= nj < M

def bfs():
    global max_length
    while dq:
        i, j = dq.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if in_range(ni,nj) and map_copy[ni][nj] == 'L':
                dq.append([ni,nj])
                map_copy[ni][nj] = map_copy[i][j] + 1
                max_length = max(max_length, map_copy[ni][nj])

from collections import deque
import copy
import sys
input = sys.stdin.readline

N, M = map(int,input().split())

map = [list(input().rstrip()) for _ in range(N)]

di = [1,-1,0,0]
dj = [0,0,1,-1]

max_length = 0

# 모든 위치에서 bfs
for i in range(N):
    for j in range(M):
        if map[i][j] == 'L':
            map_copy = copy.deepcopy(map)
            map_copy[i][j] = 0
            dq = deque()
            dq.append([i,j])
            bfs()
            
print(max_length)