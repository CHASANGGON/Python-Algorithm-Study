"""
6 8
0 1 2
0 2 4
1 2 1
1 3 7
2 4 3
3 4 2
3 5 1
4 5 5
"""

# 정점의 갯수 V, 간선의 갯수 E
V, E = map(int, input().split())

# 그래프 저장 : 인접 리스트
graph = [[] for _ in range(V)]

# 간선 정보를 인접 리스트에 저장
for _ in range(E):
    u, v, w = map(int, input().split())  # u -> v 간선의 가중치가 w!
    graph[u].append((v, w))  # v로 가는 간선의 가중치가 w.


# 모든 정점에 대해서 모든 정점의 최소 경로(비용)을 계산하는 알고리즘
# 모든 정점(N) 개에 대해서 모든 정점(N)의 최단 비용을 계산...!
def floyd_warshall(graph):
    # 최단 거리를 저장할 N x N 리스트 dist, (초기화를 무한대)
    dist = [[float('inf')] * V for _ in range(V)]

    # 초기화...
    # 1. 자기 자신으로 가는 노드의 최단 경로는 0으로 초기화
    for i in range(V):
        dist[i][i] = 0
    # 2. 인접리스트에 저장되어 있는 가중치의 간선값으로 dist 초기화
    for v in range(V):
        for u, w in graph[v]:
            dist[v][u] = w  # v -> u, 비용: w.

    # i ---------> j 연결하는 최단 거리(비용) 계산
    #      k  라는 노드를 징검다리 역할로 부여하여 최단 거리를 갱신
    # i  ---> k ---> j 로 가는 최단 거리로 갱신할 수 있다..!
    for k in range(V):
        for i in range(V):
            for j in range(V):
                # i ---------> j vs i  ---> k ---> j 갱신!
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


import pprint

dist = floyd_warshall(graph)
pprint.pprint(dist)
