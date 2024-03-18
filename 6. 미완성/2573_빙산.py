def any_iceberg(): # 빙산이 남아 있는지
    global si, sj
    for i in range(n):
        for j in range(m):
            if arr[i][j]:
                si = i
                sj = j
                return True
    return False

def in_range(ni,nj):
    return 0 <= ni < n and 0 <= nj < m

def dfs():
    original = copy.deepcopy(arr)
    melt = [[0]*m for _ in range(n)]
    
    while stack:
        i,j = stack.pop()
        cnt = 0 # 인접 바다 카운트
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            # 인덱스 검사 & 방문 체크
            if in_range(ni,nj) and visited[ni][nj]:
                if arr[ni][nj]: # 빙산이면 stack append(다음 탐색 대상)
                    stack.append([ni,nj])
                    visited[ni][nj] = 0 # stack append 중복 방지
                else: # 바다면 카운트
                    cnt += 1
        melt[i][j] = cnt
    
    for i in range(n):
        for j in range(m):
            if arr[i][j] > 0 and melt[i][j] == 0:
                return False
    
    for i in range(n):
        for j in range(m):
            arr[i][j] = max(0,arr[i][j]-melt[i][j]) # 0까지만 감소
    
    return True

import copy
import sys
input = sys.stdin.readline

n, m  = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(n)]

di = [1,-1,0,0]
dj = [0,0,1,-1]
cnt = 1
i, j = 0, 0
while True:
    if any_iceberg(): # 빙산이 남아 있으면
        visited = [[1]*m for _ in range(n)]
        visited[si][sj] = 0
        stack = [[si,sj]]
        if dfs():
            cnt += 1
        else:
            print(cnt)
            exit()
    else:
        print(cnt)
        break