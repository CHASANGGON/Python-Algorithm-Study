def f(i, lst):
    if i == M:
        print(*lst)
    else:
        for j in range(1,N+1):
            if j not in lst:
                lst.append(j)
                f(i+1,lst)
                lst.pop()

import sys
input = sys.stdin.readline

N, M = map(int,input().split())

f(0, []) 