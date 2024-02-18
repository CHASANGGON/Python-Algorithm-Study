def f(d,start): # 깊이, 리스트,
    if d == m+1:
        print(*lst)
    else:
        for i in range(start, n+1):
            if i not in lst:
                lst.append(i)
                f(d+1,i+1)
                lst.pop()

import sys
input = sys.stdin.readline

n, m = map(int,input().split())
lst = []
f(1,1)