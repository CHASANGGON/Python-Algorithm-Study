from heapq import heappush, heappop
import sys
sys.stdin = open('C:/Users/yg961/OneDrive/Documents/GitHub/Algorithm/1. Daily Task(swea & baekjoon)/2024_03/2024_03_24/input1.txt', 'r')

INF = int(1e9) # 엄청 큰 값 10억

V, E = map(int, input().split())
start = 0 # 시작 노드 번호

# 인접 리스트
graph = [[] for _ in range(V)]
# 누적 거리를 저장할 변수
distance = [INF] * V

# 간선 정보 저장
for _ in range(E):
    s, e, w = map(int, input().split())
    graph[s].append([w, e])
    
    
def dijkstra(start):
    pq = []
    # 시작점의 weight, node 번호를 한 번에 저장
    heappush(pq, (0, start))
    # 시작 노드 초기화
    distance[start] = 0
    
    while pq:
        # 최단 거리 노드에 대한 정보 pop
        dist, now = heappop(pq)
        
        # pq의 특성 때문에 더 긴거리가 미리 저장되어 있다!!
        # now가 이미 더 짧은 거리로 온 적이 있다면 pass
        if distance[now] < dist:
            continue
        
        # now에서 인접합 다른 노드 확인
        for to in graph[now]:
            next_dist = to[0]
            next_node = to[1]
            
            # 누적 거리 계산
            new_dist = distance[now] + next_dist
            
            if new_dist < distance[next_node]:
                distance[next_node] = new_dist # 누적 거리를 최단 거리로 갱신
                heappush(pq,(new_dist, next_node)) # next_node의 인접 노드들을 pq에 추가
    

dijkstra(start)
print(distance)