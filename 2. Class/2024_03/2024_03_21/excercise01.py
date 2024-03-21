'''
7 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''

# 정점의 개수 V, 간선의 개수 E
V, E = map(int, input().split())

# 그래프 저장 : 인접 리스트
graph = [[] for _ in range(V)]

# 간선 정보를 인접 리스트에 저장
for _ in range(E):
    u, v, w = map(int, input().split()) # u -> v 간선의 가중치가 w    
    graph[u].append((v,w)) # u에서 v로 가는 간선의 가중치가 w (단방향)
    graph[v].append((u,w)) # u에서 v로 가는 간선의 가중치가 w (단방향)
    
import heapq # 최소힙    

# 프림 알고리즘 함수 정의
# graph: 인접 리스트, start: 시작정점
def prim(graph, start):
    
    # 정점에 대해 방문 체크 배열
    visited = [False] * V 
    mheap = [] # 최소힙 : 지금까지 연결된 간선들 중에 최소 비용 간선을 선택
    
    # 최소신장트리를 저장할 리스트
    mst = []
    
    # 시작 정점으로부터 간선을 선택 시작하도록 초기값을 넣어준다...
    # (가중치, 다음으로가는 정점)
    heapq.heappush(mheap, (0, start))
    total_weight = 0
    while mheap:
        # 최소 비용을 가진 간선을 하나씩 꺼내면서 진행
        weight, node = heapq.heappop(mheap)
        
        # 방문 체크 (이미 연결한 노드라면 무시)
        if visited[node]:
            continue
        
        visited[node] = True # 해당 정점에 방문 표시
        mst.append((weight, node)) # 최소신장트리에 해당 간선 정보를 추가
        total_weight += weight
        
        # 해당 node와 연결되어 있는 모든 간선 정보를 최소힙에 추가
        for nxt, weight in graph[node]:
            if not visited[nxt]:
                heapq.heappush(mheap, (weight, nxt)) # 연결된 간선 정보를 최소힙에 추가
    print(total_weight)
    return mst


mst = prim(graph, 0)
print(mst)