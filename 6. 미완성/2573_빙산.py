
import copy
import sys
input = sys.stdin.readline

n, m  = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(n)]

di = [1,-1,0,0]
dj = [0,0,1,-1]
cnt = 1
i, j = 0, 0
