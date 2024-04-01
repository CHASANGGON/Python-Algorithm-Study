# 금으로 막혀있어 지나갈 수 없는 칸은 '#'
# 비어있는 칸은 '.'
# 시작 지점은 'S'
# 출구는 'E'
# 각 층 사이에는 빈 줄이 있으며, 입력의 끝은 L, R, C가 모두 0으로 표현
def bfs(i,j,k):
    dq = deque([[i, j, k]])
    while dq:
        i, j, k, = dq.popleft()
        for idx in range(6):
            ni = i + di[idx]
            nj = j + dj[idx]
            nk = k + dk[idx]
            if 0 <= ni < L and 0 <= nj < R and 0 <= nk < C:
                if building[ni][nj][nk] == '.':
                    building[ni][nj][nk] = building[i][j][k] + 1
                    dq.append([ni, nj, nk])
                elif building[ni][nj][nk] == 'E':
                    print('Escaped in', building[i][j][k] + 1, 'minute(s).')
                    return

    print('Trapped!')

from collections import deque
import sys
input = sys.stdin.readline

di = [1,-1,0,0,0,0]
dj = [0,0,1,-1,0,0]
dk = [0,0,0,0,1,-1]

while True:
    L, R, C = map(int, input().split())
    if L == 0 and R == 0 and C == 0:
        break
    building = [] # 빌딩
    for _ in range(L):
        floor = [list(input().rstrip()) for _ in range(R)] # 한 층 입력
        building.append(floor) # 한 층 입력 리스트 어펜드
        input() # 빈 줄

    for i in range(L):
        for j in range(R):
            for k in range(C):
                if building[i][j][k] == 'S':
                    building[i][j][k] = 0
                    bfs(i, j, k)