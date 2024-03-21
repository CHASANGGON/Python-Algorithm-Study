#  kruskal
"""
7 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
"""

# 정점의 갯수 V, 간선의 갯수 E
V, E = map(int, input().split())

# 그래프 저장 : 인접 리스트 
graph = [[] for _ in range(V)]

# 간선 정보를 인접 리스트에 저장
for _ in range(E):
    u, v, w = map(int, input().split()) # u -> v 간선의 가중치가 w!
    graph[u].append((v, w)) # v로 가는 간선의 가중치가 w.
    graph[v].append((u, w))





# 크루스칼(kruskal): 크루스칼 알고리즘을 통해 최소 신장 트리 구하기
def kruskal(graph):
    # union-find 알고리즘 : find 함수 - x가 속하는 해당 그룹의 대표자를 반환
    def find_set(x):
        if x == parent[x]:
            return x
        return find_set(parent[x])

    # union-find 알고리즘 : union 함수 - x와 y가 속하는 두 그룹을 통합
    def union(x, y):
        root_x = find_set(x)
        root_y = find_set(y)

        parent[root_x] = root_y


    # 간선의 정보를 가지고 있는 배열
    edges = []
    for v in range(V):
        for u, w in graph[v]:
            # 간선의 정보를 (가중치 w, 정점 u, 정점 v) 형태로 저장
            edges.append((w, u, v))

    # 가중치에 대해서 오름차순 정렬
    edges.sort() # 간선을 가중치 기준으로 정렬
    mst = [] # 최소신장트리를 저장할 리스트
    parent = list(range(V)) # make_set 초기화 : 각 정점을 자기 자신을 부모로 같느 형태로 초기화

    for w, u, v in edges:
        # 사이클이 발생하지 않는 간선 V - 1 개를 선택과정 진행
        if find_set(u) != find_set(v):
            union(u, v)
            mst.append((u, v, w))

    return mst


mst = kruskal(graph)
print(mst)