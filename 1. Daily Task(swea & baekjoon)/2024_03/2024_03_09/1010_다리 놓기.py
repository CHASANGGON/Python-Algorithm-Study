import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    r, n = map(int,input().split())
    nn = 1
    for i in range(n,n-r,-1):
        nn *= i
    rr = 1
    for j in range(1,r+1):
        rr *= j
    
    print(nn//rr)