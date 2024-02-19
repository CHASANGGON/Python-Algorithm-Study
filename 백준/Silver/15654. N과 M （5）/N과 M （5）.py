def f(i):
    if i == M:
        print(*p)

    else:
        for l in lst:
            if l not in p:
                p.append(l)
                f(i+1)
                p.pop()
            
import sys
input = sys.stdin.readline
N, M = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()
p = []
f(0)