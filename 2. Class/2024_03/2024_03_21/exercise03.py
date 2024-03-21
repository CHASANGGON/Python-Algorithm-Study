#  kruskal
# 6 8
# 0 1 2
# 0 2 4
# 1 2 1
# 1 3 7
# 2 4 3
# 3 4 2
# 3 5 1
# 4 5 5

import heapq

# 정점의 갯수 V, 간선의 갯수 E
V, E = map(int, input().split())

# 그래프 저장 : 인접 리스트 
graph = [[] for _ in range(V)]

# 간선 정보를 인접 리스트에 저장
for _ in range(E):
    u, v, w = map(int, input().split()) # u -> v 간선의 가중치가 w!
    graph[u].append((v, w)) # v로 가는 간선의 가중치가 w.
    
    
    
def dijsktra(graph, start):
    # 시작 정점에서 각 정점까지의 최소 거리(비용)을 계산하는 배열 dist
    dist = [float('inf')] * V # 이렇게 사용하면 파이썬에서 최댓값
    
    # 방문체크를 위한 visited 배열
    visited = [False] * V
    # 시작 정점에 대해서 방문체크와 dist 거리를 0으로 초기화
    dist[start] = 0
    # 우선순위 큐를 사용해서 정점을 (최소비용을 갖고 있는 정점을 선택)
    # 시작 정점으로부터 진행
    mheap = [(0, start)]
    
    while mheap:
        cost, node = heapq.heappop(mheap)
        
        # 이미 계산되어 있는 dist 보다 더 거리가 긴 노드라면 패스
        if cost > dist[node]:
            continue
        
        # 인접해 있는 노드와 거리를 순차적으로 뽑아서 큐에 넣어주고, dist를 갱신
        for nxt, w in graph[node]:
            # 새로 갱신될 거리값
            new_dist = dist[node] + w
            if new_dist < dist[nxt]:
                dist[nxt] = new_dist
                heapq.heappush(mheap, (new_dist, nxt))
                
    return dist
    
# 다익스트라를 사용하여 0번 노드로부터 모든 노드까지의 최소 경로 비용을 출력
start = 0
dist = dijsktra(graph, 0)
print(dist)