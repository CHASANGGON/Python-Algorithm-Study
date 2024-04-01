# union-find 로 쉽게 구현 가능
# 주어지는 연결정보를 통해서 대표자를 결정지어주면 됨
def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    root_x = find(x)
    root_y = find(y)
    
    parent[root_x] = root_y

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
parent = list(range(n+1)) # 자기 자신을 부모로 갖는 집합 생성(1~n)
for _ in range(m):
    s, e = map(int, input().split())
    union(s, e)

for i in range(1,n+1):
    find(i)

print(len(list(set(parent[1:]))))