def bfs():
    di = [1,-1,0,0]
    dj = [0,0,1,-1]
    
    def fire(dq):
        for i in range(r):
            for j in range(c):
                if arr[i][j] == 'F':
                    dq.append([i,j,'F',0])
        return dq
        
    def jihoon(dq):
        for i in range(r):
            for j in range(c):
                if arr[i][j] == 'J':
                    dq.append([i,j,'J',0])
        return dq
    
    dq = deque()
    dq = fire(dq)
    dq = jihoon(dq)

    def escape(dq):
        while dq:
            i, j, obj, day = dq.popleft()
            
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                # 인덱스를 벗어나지 않고, 벽이 아니라면 탐색
                if 0 <= ni < r and 0 <= nj < c:
                        if obj == 'J' and arr[ni][nj] =='.': # 지훈이가 길을 만나면
                            arr[ni][nj] = 'J' # 지훈 기록
                            dq.append([ni,nj,'J',day+1]) # 해당 좌표를 하루 추가해서 dq append
                        elif obj == 'F' and (arr[ni][nj] == '.' or arr[ni][nj] == 'J'): # 불이면
                            arr[ni][nj] = 'F'
                            dq.append([ni,nj,'F',0])
                        
                # 인덱스를 벗어났는데 지훈이라면 다음 날 탈출 가능
                else:
                    if obj == 'J':
                        print(day + 1)
                        return
        
        print('IMPOSSIBLE') # 방문 가능한 곳을 다 돌았는데 아직 탈출 못 했다면 탈출 불가
                    
    escape(dq)
    
from collections import deque
import sys
input = sys.stdin.readline

r, c = map(int, input().split())

arr = [list(input().rstrip()) for _ in range(r)]

bfs()