def dfs():
    while stack:
        now = stack.pop()
        
        for nxt in graph[now]: # 인접 노드를 살펴보면서
            if color[nxt]: # 인접 노드에 컬러가 있는데(방문한 적 있는데)
                if color[now] == color[nxt]: # 색이 같다면
                    return False
            else: # 컬러가 없다면
                if color[now] == 1: # 현재 노드와 
                    color[nxt] = 2 # 다른 컬러 지정
                else:
                    color[nxt] = 1 # 컬러 지정
                stack.append(nxt)

    return True

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    V, E = map(int, input().split()) # 정점(1~V) 개수, 간선 개수
    graph = [[] for _ in range(V+1)]
    color = [0] * (V+1) # 컬러를 0으로 초기화
    result = 'YES'
    
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    for start in range(1,V+1): # 1~V번 노드를 살펴보면서
        if not color[start]: # 아직 색이 없다면
            stack = [start] # 스택에 출발 노드 저장
            color[start] = 1 # 방문 처리
            if dfs(): # dfs 출발 -> return True -> 계속 탐색
                pass
            else: # return False -> 이분 그래프 x -> for문 탈출
                result = 'NO'
                break
    print(result)