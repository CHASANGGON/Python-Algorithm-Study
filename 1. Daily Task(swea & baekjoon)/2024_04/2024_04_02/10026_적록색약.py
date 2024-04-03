def normal_bfs(i, j):
    dq = deque([[i,j]])
    color = arr[i][j]
    arr[i][j] = 0
    while dq:
        i,j = dq.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == color:
                arr[ni][nj] = 0
                dq.append([ni,nj])

def red_green_bfs(i, j):
    dq = deque([[i,j]])
    color = arr_copy[i][j]
    arr_copy[i][j] = 0
    
    if color == 'B':
        while dq:
            i,j = dq.popleft()
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < n and 0 <= nj < n and arr_copy[ni][nj] == 'B':
                    arr_copy[ni][nj] = 0
                    dq.append([ni,nj])
    else:
        while dq:
            i,j = dq.popleft()
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < n and 0 <= nj < n and (arr_copy[ni][nj] == 'R' or arr_copy[ni][nj] == 'G'):
                    arr_copy[ni][nj] = 0
                    dq.append([ni,nj])
                

di = [1,-1,0,0]
dj = [0,0,1,-1]

from collections import deque
import copy
import sys
input = sys.stdin.readline

n = int(input())

arr = [list(input().rstrip()) for _ in range(n)]
arr_copy = copy.deepcopy(arr)
# 정상인
normal = 0
for i in range(n):
    for j in range(n):
        if arr[i][j]:
            normal_bfs(i, j)
            normal += 1

# 적록색약
red_green = 0
for i in range(n):
    for j in range(n):
        if arr_copy[i][j]:
            red_green_bfs(i, j)
            red_green += 1

print(normal, red_green)