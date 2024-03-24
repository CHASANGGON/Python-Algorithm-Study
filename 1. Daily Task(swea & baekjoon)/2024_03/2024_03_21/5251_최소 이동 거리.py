def dijikstra(start):
    distance = [INF] * (N + 1) # 거리 정보를 저장할 리스트 -> 최솟값을 갱신해야하기 때문에 초기값은 임의의 큰 수
    distance[start] = 0 # 시작 거리 0 으로 초기화
    pq = [] # priority_queue(우선순위 큐)
    heappush(pq, (0, start)) # 가중치, 시작 노드 -> heapify
    
    
    while pq: # 최소 거리를 산정할만한 유망한 노드가 있을 때까지 실행
        dist, now = heappop(pq) # 해당 노드까지 발생한 최소 거리와 노드 정보
        # 꺼낸 거리가 최소 거리가 아니라면 pass
        # 힙큐에 push는 돼 있지만, 그 후 다른 노드에 의해 최소화 되었을 수 있다
        # 아래 코드가 없어도 답을 구하는데 문제는 없지만, 최적화를 위해서...!
        if distance[now] < dist: 
            continue

        for to in graph[now]: # 현재 노드에서 방문 가능한 노드들 중에서
            next_dist = to[0] # 거리 정보
            next_node = to[1] # 방문 가능한 노드 정보
            new_dist = dist + next_dist # 현재까지의 최소 거리 + 추가로 발생하는 거리
            if new_dist < distance[next_node]: # 새로 갱신할 거리정보가 기존의 거리 짧을 때
                distance[next_node] = new_dist # 거리 정보를 갱신해주고
                heappush(pq, (new_dist, next_node)) # 새로 갱신된 최소 거리 -> 앞으로 한 번 더 고려 가능한 유망한 최소 경로
                
    print(f'#{tc} {distance[N]}')
    

from heapq import heappush, heappop
INF = 10**9
t = int(input())

for tc in range(1, t + 1):
    N, E = map(int, input().split())
    
    graph = [[] for _ in range(N + 1)] # 가중치와 도착노드를 함께 담아야 하므로 리스트 형식
    
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append((w, e)) # 단방향 그래프 - 도착 노드, 가중치
        
    start = 0 # 시작 노드 설정
    dijikstra(start) # 다익스트라는 시작노드에서 도착 노드까지의 최소 거리를 dp와 그리디식으로 계속 갱신 -> 시작 노드를 정해주어야함