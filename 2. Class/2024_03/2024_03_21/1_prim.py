from pprint import pprint
import sys
sys.stdin = open("input_1.txt", "r")

# 우선순위큐를 활용
from heapq import heappush, heappop

def prim(start):
    pq = []
    MST = [0] * V # visited로 사용
    
    # 최소 비용
    sum_weight = 0
    
    # 시작점 추가
    # [기존 BFS] 노드 번호만 관리
    # [PRIM] 가중치가 낮으면 먼저 나와야 한다.
    # -> 관리해야할 데이터: 가중치, 노드 번호 2가지
    # -> 동시에 두 가지 데이터 다루기
    #       1. class 로 만들기
    #       2. 튜플로 관리
    # 2차원 배열 + 가중치 + 높이
    heappush(pq, (0, start))
    
    while pq:
        weight, now = heappop(pq)
        
        # 우선순위 큐의 특성 상
        # 더 먼거리로 가는 방법이 큐에 저장이 되어 있기 때문에
        # 기존에 이미 더 짧은 거리로 방문했다면, continue
        if MST[now]:
            continue
        
        # 방문 처리
        MST[now] = 1
        # 누적합 추가
        sum_weight += weight
        
        # 갈 수 있는 노드들을 보면서
        for to in range(V):
            # 갈 수 없거나 이미 방문했다면 pass
            if graph[now][to] == 0 or MST[to]:
                continue
            
            heappush(pq, (graph[now][to], to))
            
    print(f'최소 비용: {sum_weight}')
        

# 입력
V, E = map(int, input().split())
# 인접 행렬로 저장
# - [실습] 인접 리스트로 저장
graph = [[0] * V for _ in range(V)]
for _ in range(E):
    # 가중치 저장
    
    # [기존] 3 -> 4로 갈 수 있다.
    # graph[3][4] = 1

    # [가중치 그래프] 3 -> 4로 가는 데 31이라는 비용이 든다
    # graph[3][4] = 31
    s, e, w = map(int, input().split())
    graph[s][e] = w
    graph[e][s] = w # 무방향(양방향) 그래프
    
pprint(graph)
prim(0)