def f(i, start):
    if i == M:
        print(*lst)

    else:
        for j in range(start,N+1):
            lst.append(j)
            f(i+1, j)
            lst.pop()

import sys
input = sys.stdin.readline
N, M = map(int,input().split())
lst = []
f(0, 1)