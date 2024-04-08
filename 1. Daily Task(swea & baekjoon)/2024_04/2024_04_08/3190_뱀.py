# 단순 구현 문제
# 1. 입력(사과), 방향 전환(왼쪽 = 'L', 오른쪽 = 'D')
# 2. 헤드와 테일을 visited 배열
#   -> 헤드 = 테일 or 벽을 만나면 종료

import sys
input = sys.stdin.readline

N = int(input())
board = [[0]*N for _ in range(N)]

K = int(input())
for _ in range(K):
    i, j = map(int, input().split())
    i -= 1
    j -= 1
    board[i][j] = 'apple'

L = int(input())
info = []
for _ in range(L):
    t, d = input().split() # time, direction
    t = int(t) + 1
    info.append([t, d])
info_index = 0

direction = [[0,1], [1,0], [0,-1], [-1,0]]
direction_index = 0 # 처음 방향은 오른쪽

hi, hj = 0, 0 # head
ti, tj = 0, 0 # tail
now_time = 0

board[hi][hj] = 'snake'

while True:
    now_time += 1 # 시간 증가
    if info_index < L and now_time == info[info_index][0]: # 방향 전환할 시간이 됐으면
        if info[info_index][1] == 'D': # 방향에 맞게
            direction_index = (direction_index + 1)%4 # 전환
        else:
            direction_index = (direction_index - 1)%4 # 전환
        info_index += 1 # 다음 방향 전환 시간 체크를 위해 인덱스 증가

    hi += direction[direction_index][0]
    hj += direction[direction_index][1] # 이동
    
    if hi >= N or hi < 0 or hj >=N or hj < 0: # 벽과 부딪혔으면
        print(now_time)
        break
    
    if board[hi][hj] != 'apple': # 사과가 있으면 몸 길이 증가
        board[ti][tj] = 0 # 지나온 길 지우기
        for di, dj in [[1,0], [0,1], [-1,0], [0,-1]]:
            ni = ti + di
            nj = tj + dj
            if 0 <= ni < N and 0 <= nj < N and board[ni][nj] == 'snake':
                ti = ni
                tj = nj
                break
    
    if board[hi][hj] =='snake': # 자신의 몸과 부딪혔으면
        print(now_time)
        break
    
    board[hi][hj] ='snake'
    