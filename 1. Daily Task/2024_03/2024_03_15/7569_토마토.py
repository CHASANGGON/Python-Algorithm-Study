def in_range(nh,ni,nj):
    return 0 <= nh < H and 0 <= ni < N and 0 <= nj < M

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
for h in range(H):
    for i in range(N):
        for j in range(M):
            if arr[h][i][j] == 1:
                for k in range(6):
                    nh = h + dh[k]
                    ni = i + di[k]
                    nj = j + dj[k] 
                    if in_range(nh,ni,nj) and arr[nh][ni][nj] == 0:
                        arr[nh][ni][nj] = 1
            