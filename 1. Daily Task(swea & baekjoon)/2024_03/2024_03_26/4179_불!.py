                
 
from collections import deque
import sys
from copy import deepcopy
input = sys.stdin.readline


def bfs():
    
    def fire():
        for i in range(r):
            for j in range(c):
                if maze[i][j] == 'F': # 불이 존재하면
                    fq.append([i, j]) # fq에 푸쉬
                    maze[i][j] = 0
                elif maze[i][j] == 'J':
                    maze[i][j] = 0
                    jq.append([i,j])
                    visited[i][j] = 0
                    return

    fq = deque()
    fire()
    while fq:
        i,j = fq.popleft()
        for k in range(4): # 델타 탐색
            ni = i + di[k] 
            nj = j + dj[k]
            if 0 <= ni < r and 0 <= nj < c:
                if maze[ni][nj] == '.': # 길이라면
                    maze[ni][nj] = maze[i][j] + 1 # 불의 도착 시간을 기록
                    fq.append([ni,nj]) # 큐에 푸쉬

    
    jq = deque()
    visited = [[1] * c for _ in range(r)]
    jihoon()
    while jq: # q가 존재하는 동안 실행
        i,j = jq.popleft()
        for k in range(4): # 델타 탐색
            ni = i + di[k] 
            nj = j + dj[k]
            if 0 <= ni < r and 0 <= nj < c:
                if visited[ni][nj] and maze[ni][nj] != '#' and maze[ni][nj] > maze[i][j] + 1: # 지훈이의 도달 시간보다 오래 걸린다면 지나갈 수 있다
                    maze[ni][nj] = maze[i][j] + 1
                    fq.append([ni,nj]) # 큐에 푸쉬
            else: # 인덱스를 벗어났다면 탈출
                print(maze[i][j] + 1)
                return

    print('IMPOSSIBLE')     
                


r, c = map(int, input().split())
maze = [list(input().rstrip()) for _ in range(r)]

di = [1,-1,0,0]
dj = [0,0,1,-1]

bfs()