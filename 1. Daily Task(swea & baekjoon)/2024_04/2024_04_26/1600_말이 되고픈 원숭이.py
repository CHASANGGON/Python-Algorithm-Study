from collections import deque
import sys
input = sys.stdin.readline

k = int(input())
w, h = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(h)]
ans = -1

dq = deque()
dq.append((0,0,k))


while dq:
    i,j,remain_k = dq.popleft()
    
    if remain_k: # 말처럼 이동 가능하면
        for ni, nj in (i+2,j+1), (i+2,j-1), (i-2,j+1), (i-2,j-1), (i+1,j+2), (i+1,j-2), (i-1,j+2), (i-1,j-2):
            if 0 <= ni < h and 0 <= nj < w and arr[ni][nj] == 0: # 인덱스 검사 및 방문 체크
                arr[ni][nj] = arr[i][j] + 1
                dq.append([ni,nj,remain_k-1]) # remain_k 1 감소
    
    for ni, nj in (i+1,j), (i-1,j), (i,j+1), (i,j-1): # 그냥 이동
        if 0 <= ni < h and 0 <= nj < w and arr[ni][nj] == 0: # 인덱스 검사 및 방문 체크
            arr[ni][nj] = arr[i][j] + 1
            dq.append([ni,nj,remain_k]) # remain_k 감소 x
            
    if arr[h-1][w-1]:
        ans = arr[h-1][w-1]
        break

print(ans)