def kruskal():
    def find(x):
        if parent[x] == x:
            return x
        parent[x] = find(parent[x]) # 경로 압축
        return parent[x]

    def union(x, y):
        root_x = find(x)
        root_y = find(y)
    
        if root_x > root_y:
            parent[root_y] = root_x
        else:
            parent[root_x] = root_y
        parent[x] = find(x)

    min_weight = 0
    parent = list(range(V)) # 소년 가장

    for s, e, w in edges:
        if find(s) == find(e): # 같은 집합에 속하면 pass -> cycle 방지
            print(s, e, w, '싸이클 탈락!')
            continue
        else:
            print(s, e)
            union(s, e) # 같은 집합으로 합치기
            parent[s] = find(s) # 방문 처리
            parent[e] = find(e) 
            min_weight += w
    
    print(f'최소 가중치 : {min_weight}')    
   
 
import sys
sys.stdin = open('input.txt', 'r')

V, E = map(int, input().split())
edges = []
for _ in range(E):
    s, e, w = map(int, input().split())
    edges.append([s, e, w])
    
edges.sort(key = lambda x : x[2])
    
kruskal()