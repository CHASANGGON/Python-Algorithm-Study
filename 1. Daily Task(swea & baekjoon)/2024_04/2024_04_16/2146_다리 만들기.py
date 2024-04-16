from pprint import pprint
from collections import deque
from copy import deepcopy
import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# 1. 테두리 구하기
# 2. 각 섬의 테두리에서 bfs 
# 3. 출력

for i in range(n):
    for j in range(n):
        if arr[i][j]:
            dq = deque()
            while dq:
                i,j = dq.popleft()
                for ni, nj in (i+1,j), (i-1,j), (i,j+1), (i,j-1): 
                    if 0 <= ni < n and 0 <= nj < n:
                        pass