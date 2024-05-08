from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]


for _ in range(m):
    e, s = map(int, input().split())
    graph[s].append(e)
    
def bfs(now):
    visited = [1]*(n+1)
    visited[now] = 0
    dq = deque()
    dq.append(now)
    cnt = 0
    
    while dq:
        now = dq.popleft()
        cnt += 1
        
        for nxt in graph[now]:
            if visited[nxt]:
                visited[nxt] = 0
                dq.append(nxt)
    
    return cnt

ans = []
max_cnt = 0
for start in range(1,n+1):
    cnt = bfs(start)
    if cnt > max_cnt:
        max_cnt = cnt
        ans = [start] # clear
    elif cnt == max_cnt:
        ans.append(start)

print(*ans)