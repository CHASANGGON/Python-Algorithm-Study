from collections import deque
from pprint import pprint
import copy
import sys
input = sys.stdin.readline

# 0은 빈 칸, 1은 집, 2는 치킨집

# 1. 치킨집과 집의 좌표를 모두 구하기
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
chicken = []
home = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2: # 치킨집 
            chicken.append([i,j])
        elif arr[i][j] == 1: # 집
            home.append([i,j])
C = len(chicken)

def permu(idx, depth):
    if depth == n:
        # print(now_close)
        temp = now_close.copy()
        close_lst.append(temp)
    else:
        for j in range(idx, C - (n - depth - 1)):
            now_close.append(chicken[j])
            permu(j+1, depth+1)
            now_close.pop()
            
n = C-M # 치킨집을 M개(최대로) 남기는 것이 유리함 -> C-M 개 폐업
close_lst = []            
now_close = []
permu(0, 0)

min_distance = 9999999
for close in close_lst:
    arr_copy = copy.deepcopy(arr)
    for i,j in close:
        arr_copy[i][j] = 0 # 폐업    
    
    now_distance = 0
    now_chicken = []
    for i in range(N):
        for j in range(N):
            if arr_copy[i][j] == 2:
                now_chicken.append([i,j])
    now_d = 0
    for i,j in home:
        d = 9999999
        for ii,jj in now_chicken:   
            d = min(d, abs(i-ii) + abs(j-jj))
        now_d += d

        
    min_distance = min(min_distance, now_d)
    
print(min_distance)