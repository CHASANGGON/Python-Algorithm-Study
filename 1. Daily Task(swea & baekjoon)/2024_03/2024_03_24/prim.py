def prim(start):
    pq = [] # priority_queue
    visited = [0] * V
    
    # 최소 비용
    sum_weight = 0

    heappush(pq, (0, start))
    
    # 방문 가능한 모든 노드들을 pq에 push해보고
    # 최소 가중치와 중복 방문 여부를 고려하며 하나씩 pop하며
    # 최소 가중치를 구하기
    # 따라서 방문가능한 모든 경로를 고려하며 모든 노드를 방문했다면
    # 최종적으로 pq에는 아무 값도 없음
    while pq:
        weight, now = heappop(pq) # 가중치를 먼저 push -> 그래야 가중치를 기준으로 heapify 정렬!!

        # 0 1 10
        # 10 0 2
        # 1 2 0
        # 1. hq = ((1, 2), (10, 1)) / visited = [1, 0, 0]
        #   -> 1. hq = ((10, 1))    / visited = [1, 0, 1]
        # 2. hq = ((2, 1), (10, 2)) / visited = [1, 0, 1]
        #   -> 2. hq = ((10, 2)) / visited = [1, 1, 1]
        # 이제 마지막으로 10, 2 가 pop될텐데
        # 이 때 이미 2번 노드는 방문 한 적 있으므로 continue 해서 생략해야함!!!
        
        # 방문한 적 있다면
        if visited[now]: # 생략
            continue
        else:
            visited[now] = 1 # 방문 처리
        
        # 가중치 누적합(방문한 적 없고, 최소의 가중치를 가지는 간선이 주어진 것이니 바로 누적합)
        sum_weight += weight
        
        # 갈 수 있는 노드들을 pq에 추가(후보 대상에 추가)
        for to in range(V):
            # 갈 수 없거나 이미 방문한 적 있는 노드라면 제외(싸이클을 안 만드는 방법)
            if graph[now][to] == 0 or visited[to]:
                continue
            else:
                heappush(pq, (graph[now][to], to)) # 가중치와 노드 번호를 추가

    print(f'최소 비용 : {sum_weight}')

from heapq import heappush, heappop
from pprint import pprint
import sys
sys.stdin = open('input.txt', 'r')

# 입력(가중치)
V, E = map(int, input().split()) # 노드와 간선의 개수
graph = [[0] * V for _ in range(V)]
for _ in range(E):
    s, e, w = map(int, input().split()) # start, end, weight
    graph[s][e] = w
    graph[e][s] = w # 무방향 그래프

prim(0) # 시작 노드를 지정