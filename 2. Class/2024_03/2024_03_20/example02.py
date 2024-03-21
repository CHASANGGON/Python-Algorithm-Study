from pprint import pprint

arr = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]

# 정점의 개수, 간선의 개수 E
V = 7
E = 8

# 인전행렬 V * V
graph = [[0] * (V + 1) for _ in range(V + 1)]
for idx in range(0, len(arr), 2):
    # 정점 v, u
    v = arr[idx]
    u = arr[idx + 1]
    graph[v][u] = 1 # v -> u
    graph[u][v] = 1 # u -> v

print(graph)
pprint(graph) # 이렇게 하면 차원의 형태로 표현해줌!


# 인접리스트 : 각 정점에 대해서 연결된 간선 정보
graph = [[] for _ in range(V + 1)]
for idx in range(0, len(arr), 2):
    # 정점 v, u
    v = arr[idx]
    u = arr[idx + 1]
    graph[v].append(u) # v -> u
    graph[u].append(v) # u -> v
    
print(graph)
pprint(graph)

# 시작 정점을 1번부터 dfs 탐색으로 진행
# start : 시작 정점을 기준으로 깊이 우선 탐색...
def dfs(start):
    visited[start] = True # 방문 체크
    print(start,end='-')
    
    # 현재 노드 start에서 인접한 노드를 방문한다...!
    for nxt in graph[start]:
        # 단, 이미 방문한 정점은 방문하지 않는다...!
        if visited[nxt]:
            continue # 반복문 내에서 뒷 내용 모두 생략
        
        dfs(nxt) # 다음 정점 방문
    
visited = [False] * (V + 1)
dfs(1) # 시작 노드에서 출발
