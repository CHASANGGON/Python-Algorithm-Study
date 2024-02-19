def f(i):
    if i == M:
        print(*lst)    

    else:
        for j in range(1,N+1):
            lst.append(j)
            f(i+1)
            lst.pop()

import sys
input = sys.stdin.readline
N, M = map(int,input().split())
lst = []
f(0)