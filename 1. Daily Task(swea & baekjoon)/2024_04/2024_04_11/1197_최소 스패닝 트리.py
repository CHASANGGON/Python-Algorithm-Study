def mst():
    
    def find(x):
        if x == parent[x]:
            return x
        parent[x] = find(parent[x])
        return parent[x]
    
    def union(x,y):
        root_x = find(x)
        root_y = find(y)
        
        if root_x < root_y:
            parent[root_x] = root_y
        else:
            parent[root_y] = root_x
    
    
    min_w = 0
    
    for w, a, b in edges:
        if find(a) == find(b): # 같은 부모라면 = 이미 연결되어 있다면 -> pass
            continue
        min_w += w
        union(a,b)

    print(min_w)
    
from heapq import heappush
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
edges = []
for _ in range(E):
    a, b, c = map(int, input().split())
    edges.append([c, a, b]) # 가중치가 작은 순으로 push
edges.sort(key=lambda x : x[0])
parent = list(range(V+1)) # 자기 자신을 부모로 설정
    
mst()   