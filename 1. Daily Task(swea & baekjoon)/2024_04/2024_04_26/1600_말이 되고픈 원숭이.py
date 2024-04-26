from collections import deque
from pprint import pprint
from copy import deepcopy
import sys
input = sys.stdin.readline

k = int(input())
w, h = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(h)]

ans = -1

dq = deque()
dq.append((0,0,0,0)) # 차원(k), 좌표(i,j)

visited = [[[1]*w for _ in range(h)] for _ in range(k+1)]
visited[0][0][0] = 0

while dq:
    z,i,j,time = dq.popleft()
    
    if i == h-1 and j == w-1: # 끝에 도착했으면 값 갱신
        ans = time
        break
    
    if z < k: # 말처럼 이동 가능하면
        for ni, nj in (i+2,j+1), (i+2,j-1), (i-2,j+1), (i-2,j-1), (i+1,j+2), (i+1,j-2), (i-1,j+2), (i-1,j-2):
            if 0 <= ni < h and 0 <= nj < w and visited[z+1][ni][nj] and arr[ni][nj] == 0: # 인덱스 검사 및 방문 체크
                visited[z+1][ni][nj] = 0 # 방문체크
                dq.append([z+1,ni,nj,time+1]) # remain_k 1 감소
    
    for ni, nj in (i+1,j), (i-1,j), (i,j+1), (i,j-1): # 그냥 이동 - 같은 차원 내에서 이동
        if 0 <= ni < h and 0 <= nj < w and visited[z][ni][nj] and arr[ni][nj] == 0: # 인덱스 검사 및 방문 체크
            visited[z][ni][nj] = 0
            dq.append([z,ni,nj,time+1]) # remain_k 감소 x

# for ar in arr: # 답 체크
#     for a in ar:
#         pprint(a)
        
print(ans)