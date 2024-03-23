def dfs():
    global cnt
    
    while stack:
        is_blank = False
        i, j, d = stack.pop()
        origin_d = d
        for offset_d in range(4):
            d = (offset_d + d) % 4
            ni = i + di[d]
            nj = j + dj[d]
            if 0 <= ni < n - 1 and 0 <= nj < m - 1 and arr[ni][nj] == 0: # 현재 칸이 아직 청소되지 않은 경우
                # 현재 칸을 청소한다
                stack.append([ni, nj, d])
                arr[ni][nj] = -1 # 청소 표시
                cnt += 1
                is_blank = True
                break
        # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
        if not is_blank:
            # 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진
            ni = i - di[origin_d]
            nj = j - dj[origin_d]
            if 0 <= ni < n - 1 and 0 <= nj < m - 1 and arr[ni][nj] == 0:
                stack.append([ni,nj,origin_d])
            # 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
            else:
                return

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
i, j, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 0은 청소되지 않은 빈 칸
# 1은 벽
# 0-북쪽 1-동쪽 2-남쪽 3-서쪽
di = [-1,0,1,0]
dj = [0,1,0,-1]
stack = []
stack.append([i, j, d])
arr[i][j] = -1 # 현재 칸 청소
cnt = 1
dfs()

print(cnt)