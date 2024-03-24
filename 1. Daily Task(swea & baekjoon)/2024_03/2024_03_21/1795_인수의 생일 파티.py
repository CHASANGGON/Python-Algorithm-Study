# X번 집에서 나머지 집까지의 최소 거리 구하기(시작 노드가 X인 다익스트라)
# 나머지 집에서 X번 집까지의 최소 거리 구하기(해당 노드에서 X번까지의 다익스트라)
# 그것들을 합한 다음에 최솟값을 출력

def dijikstra(start):
    pq = []
    heappush(pq, (0, start)) # 가중치, 시작노드
    distance = [inf] * (N + 1)
    distance[start] = 0

    while pq:
        dist, now = heappop(pq)
        
        if dist > distance[now]: # heappop한 최소 거리가 기존의 거리보다 클 때 pass
            continue
        
        for next_dist, next_node in graph[now]:
            new_dist = dist + next_dist
            if distance[next_node] > new_dist:
                distance[next_node] = new_dist
                heappush(pq, (new_dist, next_node))    
    return distance
                
from heapq import heappush, heappop
inf = float('inf')
t = int(input())

for tc in range(1, t + 1):
    N, M, X = map(int, input().split())
    start = X
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        s, e, w = map(int, input().split())
        graph[s].append((w, e))

    # X번 집에서 나머지 집까지의 최소 거리 구하기(시작 노드가 X인 다익스트라)    
    distance = dijikstra(X)
    max_distance = 0
    # 나머지 집에서 X번 집까지의 최소 거리 구하기(해당 노드에서 X번까지의 다익스트라)
    for rest in range(1,N+1):
        if rest != start:
            distance_rest = dijikstra(rest)
            max_distance = max(max_distance, distance[rest] + distance_rest[X])

    print(f'#{tc} {max_distance}')