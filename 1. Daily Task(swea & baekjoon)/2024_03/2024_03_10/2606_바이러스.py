def dfs(now_node):
    visited[now_node] = 0 # 방문 체크
    
    # 간선 리스트에 기록된 정보 = 현재 노드에서 방문 가능한 노드
    for next_node in edge[now_node]:
        if visited[next_node]: # 아직 방문하지 않았다면(1)
            dfs(next_node) # 재귀 호출

import sys
input = sys.stdin.readline

n = int(input()) # 컴퓨터의 개수

edge = [[] for _ in range(n+1)] # 컴퓨터의 간선 정보
visited = [1]*(n+1) # 1로 초기화 : 1은 아직 방문 X / 0은 방문 O

m = int(input()) # 간선의 개수

for _ in range(m): # 간선 정보 입력
    s, e = map(int,input().split())
    edge[s].append(e) # 무방향 그래프라서
    edge[e].append(s) # 양쪽 모두에 입력

dfs(1)
print(visited.count(0) - 1) # 방문한 노드의 개수 - 1(1번 컴퓨터)