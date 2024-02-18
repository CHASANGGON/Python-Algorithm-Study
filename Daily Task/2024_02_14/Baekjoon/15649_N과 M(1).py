def f(i):
    # 기저 조건
    # 재귀의 깊이를 결정 -> 순열의 길이를 결정
    if i == M:
        print(*lst)

    # 재귀    
    else:
        for j in range(1,N+1):
            if j not in lst:
                lst.append(j)
                f(i+1)
                lst.pop()

import sys
input = sys.stdin.readline

N, M = map(int,input().split())

# 어차피 모든 순열을 출력해야하므로 굳이 재귀 X
# bit 연산을 하는 것이 더 유리하긴 함
# 그러나 일단은 재귀를 통한 DFS & 가지치기를 배웠으니 활용해보자!

lst = []
f(0)