def f(i, start):
    if i == M+1:
        print(*lst)

    else:
        for j in range(start,N+1):
            if j not in lst:
                lst.append(j)
                f(i+1, j)
                lst.pop()
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
lst = []
f(1, 1)