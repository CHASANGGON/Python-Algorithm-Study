def f(i,start):
    if i == M:
        print(*p)
        
    else:
        for j in range(start, N):
            if lst[j] not in p:
                p.append(lst[j])
                f(i+1,j+1)
                p.pop()

import sys
input = sys.stdin.readline
N, M = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()
p = []
f(0,0)