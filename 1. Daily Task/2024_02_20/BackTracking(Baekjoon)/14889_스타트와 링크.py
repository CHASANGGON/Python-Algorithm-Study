# 잘 안 풀리네효...
def dfs_bt(depth, start): # 깊이, 시작점, 합
    if depth == M:
        llst = []
        for i in range(N):
            if i not in lst:
                llst.append(i)
        sum
    else:
        for i in range(start,N):
            lst.append(i)
            dfs_bt(depth+1, i)
            lst.pop()

import sys
input = sys.stdin.readline

N = int(input())
M = N // 2
arr = [list(map(int,input().split())) for _ in range(N)]

lst = []
min_s = 1000 # 임의의 값 설정
dfs_bt(0, 0)