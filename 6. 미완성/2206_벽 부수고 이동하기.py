import sys
input = sys.stdin.readline

n, m = map(int,input().split())

arr = [list(map(int,input())) for _ in range(n)]

arr[0][0] = 1
stack = [0,0]
di = [1,-1,0,0]
dj = [0,0,1,-1]

while stack:
    pass