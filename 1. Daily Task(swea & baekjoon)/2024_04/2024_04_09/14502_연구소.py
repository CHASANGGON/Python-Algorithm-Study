# 0은 빈 칸, 1은 벽, 2는 바이러스
# 벽의 개수는 3개
# 안전 영역 크기의 최댓값
from collections import deque
import copy
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

# 1. 벽 세우기

# 모든 벽 찾기
blank = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            blank.append([i,j])


max_safe = 0

# 벽 세우기
l = len(blank)
for i in range(l-2):
    for j in range(i+1,l-1):
        for k in range(j+1,l):
            arr_copy = copy.deepcopy(arr) # 배열 복사
            
            for idx in i,j,k:
                arr_copy[blank[idx][0]][blank[idx][1]] = 1 # 벽 세우기
            
            # 2. 바이러스 퍼트리기
            
            for iii in range(n):
                for jjj in range(m):
                    if arr_copy[iii][jjj] == 2:
                        dq = deque()
                        dq.append([iii,jjj])
                        while dq:
                            now_i, now_j = dq.popleft()
                            for di, dj in [1,0], [0,1] ,[-1,0], [0,-1]:
                                ni = now_i + di
                                nj = now_j + dj
                                if 0 <= ni < n and 0 <= nj < m and arr_copy[ni][nj] == 0:
                                    arr_copy[ni][nj] = 2
                                    dq.append([ni,nj])
            
            # 3. 안전 영역 구하기
            cnt = 0
            for iii in range(n):
                for jjj in range(m):
                    if arr_copy[iii][jjj] == 0:
                        cnt += 1
                        
            max_safe = max(max_safe, cnt)

# 4. 최댓값 출력
print(max_safe)