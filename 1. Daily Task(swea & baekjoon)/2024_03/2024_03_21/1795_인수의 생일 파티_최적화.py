def dijkstra(graph, start):
    pq = []
    heappush(pq, (0, start))
    distance = [inf] * (N+1)
    distance[start] = 0
    
    while pq:
        dist, now = heappop(pq)
        
        if dist > distance[now]:
            continue
        
        for next_dist, next_node in graph[now]:
            new_dist = dist + next_dist
            if new_dist < distance[next_node]:
                distance[next_node] = new_dist
                heappush(pq, (new_dist, next_node))
    return distance
                
from heapq import heappush, heappop
inf = float('inf')
t = int(input())

for tc in range(1, t+1):
    N, M, X = map(int, input().split())
    forward_graph = [[] for _ in range(N+1)]
    reverse_graph = [[] for _ in range(N+1)]
    for _ in range(M):
        s, e, w = map(int, input().split())
        forward_graph[s].append((w, e))
        reverse_graph[e].append((w, s))
    
    forward_distance = dijkstra(forward_graph, X)
    reverse_distance = dijkstra(reverse_graph, X)
    max_distance = 0
    for home in range(1, N+1):
        if home != X:
            max_distance = max(max_distance, 
                               forward_distance[home] +
                               reverse_distance[home])

    print(f'#{tc} {max_distance}')