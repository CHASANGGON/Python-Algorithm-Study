def bfs(s, cnt):
    dq = deque()
    dq.append([s, cnt])
    while dq:
        now, cnt = dq.popleft()
        
        if now == g:
            visited[now] = cnt
            return
        
        for nxt in now + u, now - d:
            if 0 <= nxt <= f and visited[nxt]:
                visited[nxt] = 0
                dq.append([nxt, cnt + 1])

from collections import deque
import sys
input = sys.stdin.readline

f, s, g, u, d = map(int, input().split())

visited = [1]*(f+1)
visited[0] = 0 # 0층은 존재 x
visited[s] = 0 # 출발점
visited[g] = 'use the stairs'

bfs(s, 0)
print(visited[g])