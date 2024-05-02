from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

touched = [[0]*n for _ in range(n)] # 해당 방의 스위치를 건드린 적 있는지 - 0: not visit / 1: visit
light = [[0]*n for _ in range(n)] # 해당 방의 불이 켜져 있는지 - 0: off / 1: on

switch = [[[] for _ in range(n)] for _ in range(n)] # 해당 방에 어떤 방의 스위치가 있는지
for _ in range(m):
    x, y, a, b = map(int ,input().split())
    switch[x-1][y-1].append([a-1,b-1])

dq = deque()
dq.append([0,0])

light[0][0] = 1 # 시작 위치 방의 불 켜기
touched[0][0] = 1 # 스위치 조작 기록
cnt = 1

while dq:
    x,y = dq.popleft()

    for nx, ny in switch[x][y]: # 현재 방에 있는 스위치들을 확인
        if light[nx][ny] == 0: # 해당 방의 불이 꺼져 있었다면
            light[nx][ny] = 1 # 불을 켜고
            cnt += 1 # 카운트
    
    # 인접한 위치에 있는지 방문해본다.
    visited = [[1]*n for _ in range(n)] # 방문한 곳을 기록하기 위한 인접 방문 배열을 만들고
    visited[x][y] = 0 # 현재 위치 방문 기록
    visited_dq = deque()
    visited_dq.append([x,y])
    
    # 방문 시작
    while visited_dq:
        x, y = visited_dq.popleft()
        
        for nx, ny in (x+1,y), (x-1,y), (x,y+1), (x,y-1): # 인접위치의 방들을 방문할 수 있는지
             # 불이 켜져 있고, 해당 방의 스위치를 건드린 적 없다면
            if 0 <= nx < n and 0 <= ny < n and light[nx][ny] and visited[nx][ny]:
                visited[nx][ny] = 0 # 방문 기록
                visited_dq.append([nx,ny]) # 다음 방문을 위해 push
                
                if touched[nx][ny] == 0: # 해당 방의 스위치들을 건드린 적 없다면
                    touched[nx][ny] = 1 # 스위치 조작 기록
                    dq.append([nx,ny])

print(cnt)