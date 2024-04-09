from collections import deque
import sys
input = sys.stdin.readline

# 보드의 크기 입력
N = int(input())
board = [[0]*N for _ in range(N)]

# 사과 정보 입력
K = int(input())
for _ in range(K):
    i, j = map(int, input().split())
    i -= 1
    j -= 1
    board[i][j] = 'apple'

# 방향 전환 정보 입력
L = int(input())
info = []
for _ in range(L):
    t, d = input().split() # time, direction
    t = int(t) + 1
    info.append([t, d])

info_index = 0 # 방향 배열 인덱스

direction = [[0,1], [1,0], [0,-1], [-1,0]] # →  ↓  ←  ↑
direction_index = 0 # 처음 방향은 오른쪽


now_time = 0 # 현재 시간 -> 방향 전환과 출력에 사용
i, j = 0, 0 # 현재 위치
dq = deque()
dq.append([i,j]) # 지나온 경로를 추가

while True:
    now_time += 1 # 시간 증가
    
    # 방향 전환
    if info_index < L and now_time == info[info_index][0]: # 방향 전환할 시간이 됐으면
        if info[info_index][1] == 'D': # 방향에 맞게
            direction_index = (direction_index + 1)%4 # 전환
        else:
            direction_index = (direction_index - 1)%4 # 전환
        info_index += 1 # 다음 방향 전환을 위해 인덱스 증가

    # 방향에 맞게 이동
    i += direction[direction_index][0]
    j += direction[direction_index][1]
    
    if [i,j] in dq: # 몸과 부딪혔으면 종료
        print(now_time)
        break
    
    # 몸과 부딪힌 게 아니라면 새로운 위치 dq에 추가
    dq.append([i,j])
    
    if i >= N or i < 0 or j >=N or j < 0: # 벽과 부딪혔으면 종료
        print(now_time)
        break
    
    
    if board[i][j] == 'apple': # 사과를 먹으면 몸 길이 유지
        board[i][j] = 0
        continue
    
    # 사과를 만나지 않았으면 꼬리를 dq에서 삭제
    dq.popleft()
