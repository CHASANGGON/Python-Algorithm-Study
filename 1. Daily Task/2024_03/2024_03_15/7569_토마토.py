# 1과 0의 경계 탐색해서 deque에 push
def find_boundary():
    dq = deque()
    
    for h in range(H):
        for i in range(N):
            for j in range(M):
                if arr[h][i][j] == 1: # 익은 토마토
                    for k in range(6):
                        nh = h + dh[k]
                        ni = i + di[k]
                        nj = j + dj[k] 
                        # 인덱스 검사 & 근처에 안 익은 토마토가 있다면
                        if 0 <= nh < H and 0 <= ni < N and 0 <= nj < M and arr[nh][ni][nj] == 0:
                            arr[nh][ni][nj] = 2
                            dq.append([nh,ni,nj])  
    return dq

# 경계선에서부터 bfs
def bfs():
    dq = find_boundary()
    
    while dq:
        h, i, j = dq.popleft()
        for k in range(6):
            nh = h + dh[k]
            ni = i + di[k]
            nj = j + dj[k] 
            # 인덱스 검사 & 근처에 안 익은 토마토가 있다면
            if 0 <= nh < H and 0 <= ni < N and 0 <= nj < M and arr[nh][ni][nj] == 0:
                arr[nh][ni][nj] = arr[h][i][j] + 1
                dq.append([nh,ni,nj])

# 다 익었는지 검사
def check():
    day = 0

    for h in range(H):
        for i in range(N):
            for j in range(M):
                if arr[h][i][j] == 0:
                    print(-1)
                    return
                day = max(day,arr[h][i][j])
                
    print(day-1)
    
from collections import deque
import sys
input = sys.stdin.readline

M, N, H = map(int,input().split())

arr = [[list(map(int,input().split())) for _ in range(N)] for _ in range(H)]

# 위, 아래, 왼쪽, 오른쪽, 앞, 뒤
dh = [0,0,0,0,1,-1]
di = [-1,1,0,0,0,0]
dj = [0,0,-1,1,0,0]

# 정수 1은 익은 토마토
# 정수 0 은 익지 않은 토마토
# 정수 -1은 토마토가 들어있지 않은 칸

bfs()
check()