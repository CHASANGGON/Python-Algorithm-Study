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

import heapq

# 정점의 갯수 V, 간선의 갯수 E
V, E = map(int, input().split())

# 그래프 저장 : 인접 리스트
graph = [[] for _ in range(V)]

# 간선 정보를 인접 리스트에 저장
for _ in range(E):
    u, v, w = map(int, input().split()) # u -> v 간선의 가중치가 w!
    graph[u].append((v, w)) # v로 가는 간선의 가중치가 w.


# 벨만-포드 알고리즘 함수 정의
def bellman_ford(graph, start):
    # 최단 거리를 저장할 리스트 dist, (초기화를 무한대)
    dist = [float('inf')] * V
    # 시작 정점의 최단 거리는 0
    dist[start] = 0

    # 모든 간선의 정보를 가지고 있는 배열
    edges = []
    for v in range(V):
        for u, w in graph[v]:
            # 간선의 정보를 (가중치 w, 정점 v, 정점 u) 형태로 저장
            edges.append((w, v, u))


    # 정점의 수 - 1 번만큼 반복
    # + 이 이후로 추가적인 갱신을 진행하게 되었을 때! 갱신이 만약 이루어지면, 음의 사이클이 존재한다!
    for _ in range(V - 1):
        # 모든 간선의 정보를 사용하여 최단 거리를 갱신
        for w, u, v in edges:
            # start -> u 거리와 u -> v 거리의 합이
            new_dist = dist[u] + w
            # start -> v 거리보다 더 작다면...? 갱신!
            if new_dist < dist[v]:
                dist[v] = new_dist


    return dist # 최단 경로 리스트를 반환

# 벨만포드를 사용하여 0번 노드로 부터 모든 노드까지의 최소 경로 비용을 출력
start = 0
dist = bellman_ford(graph, start)
print(dist)