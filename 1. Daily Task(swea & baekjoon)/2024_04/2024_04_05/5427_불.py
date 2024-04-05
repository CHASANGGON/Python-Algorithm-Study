# 상근이가 먼저 출발
# 다음으로 불이 출발
def bfs():
    dq = deque()
    # 불 찾기
    for i in range(h):
        for j in range(w):
            if arr[i][j] == '*':
                dq.append([i,j,'*',0])
    
    # 상근이 찾기
    for i in range(h):
        for j in range(w):
            if arr[i][j] == '@':
                dq.append([i,j,'@',0])
    

    di = [1,-1,0,0]
    dj = [0,0,1,-1]

    while dq:
        i, j, obj, t = dq.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < h and 0 <= nj < w:
                if obj == '*':
                    if arr[ni][nj] == '.' or arr[ni][nj] == '@':
                        arr[ni][nj] = '*'
                        dq.append([ni,nj,'*', 0])
                
                else:
                    if arr [ni][nj] == '.':
                        arr[ni][nj] = '@'
                        dq.append([ni,nj,'@',t+1])
            else:
                if obj != '*':
                    print(t + 1)
                    return
    print('IMPOSSIBLE')

from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

for tc in range(1, t+1):
    w, h = map(int, input().split())
    arr = [list(input().rstrip()) for _ in range(h)]
    bfs()