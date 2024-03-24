def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x]) # 경로 압축
    return parent[x]

def union(x, y):
    root_x = find(x)
    root_y = find(y)
    
    parent[root_x] = root_y

import sys
sys.stdin = open('input.txt', 'r')

V, E = map(int, input().split())
edges = []
for _ in range(E):
    s, e, w = map(int, input().split())
    edges.append([s, e, w])
    
edges.sort(key = lambda x : x[2])
cnt = 0 # 간선의 개수를 이용한 가지치기!
        # 스패닝 트리의 가지는 V(노드의 개수) - 1개
min_weight = 0
parent = [i for i in range(V)] # 소년 가장
print(parent)
for s, e, w in edges:
    if find(s) == find(e): # 이미 둘이 같은 집합이라면
        print(s, e, w, '싸이클 탈락!!')
        continue
    else:
        print(s, e, w)
        union(s, e)
        min_weight += w
        cnt += 1
        if cnt == V - 1:
            break
    
print(f'최소 가중치 : {min_weight}')