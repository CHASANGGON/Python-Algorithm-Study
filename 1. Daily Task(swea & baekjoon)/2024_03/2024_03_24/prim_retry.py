# prim 알고리즘
# start 노드로부터 인접한(방문가능한) 노드들 중
# 이미 방문한 노드를 제외하고, 싸이클을 제외하고
# 가중치가 제일 작은 노드를 하나씩 방문하는 방법
# -> 가중치가 작은 노드를 우선으로 탐색하기 때문에 우선순위 큐를 사용

def prim(start):
    min_weight = 0
    pq = []
    heappush(pq, (0, start)) # 가중치, 노드
    visited = [0] * V
    
    while pq:
        w, now = heappop(pq)
        
        if visited[now]:
            continue
        else:
            visited[now] = 1
            min_weight += w
        
        for to in range(V):
            if visited[to] or graph[now][to] == 0:
                continue
            else:
                heappush(pq, (graph[now][to], to))
                
    print(f'최소 가중치 : {min_weight}')
        

from heapq import heappush, heappop
import sys
sys.stdin = open('input.txt', 'r')

V, E = map(int, input().split())
graph = [[0] * V for _ in range(V)]
for _ in range(E):
    s, e, w = map(int, input().split())
    graph[s][e] = w
    graph[e][s] = w
    
start = 0
prim(start)