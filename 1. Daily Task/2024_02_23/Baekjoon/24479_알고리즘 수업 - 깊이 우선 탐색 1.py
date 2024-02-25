def dfs(now):
    global cnt
    visited[now] = cnt
    for can_visit in edge[now]:
        if visited[can_visit] == 0:
            cnt += 1
            dfs(can_visit)

        
import sys
sys.setrecursionlimit(150000)
input = sys.stdin.readline

n, m, r = map(int,input().split())
visited = [0]*(n+1) # 방문 순서 표시
edge = [[] for _ in range(n+1)] # 간선 정보
cnt = 1

for _ in range(m):
    s, e = map(int,input().split())
    edge[s].append(e)
    edge[e].append(s)

for i in range(1,n+1):
    edge[i].sort()

dfs(r)
for i in range(1,n+1):
    print(visited[i])
    