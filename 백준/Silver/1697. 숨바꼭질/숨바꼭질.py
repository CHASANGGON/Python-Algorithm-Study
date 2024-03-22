def bfs(now, cnt):
    
    dq = deque()
    dq.append([now,cnt])
    
    while dq:
        now, cnt = dq.popleft()
        if now == k:
            print(cnt)
            return
        
        for nxt in now - 1, now + 1, now * 2:
            if 0 <= nxt <= 100000 and visited[nxt]:
                visited[nxt] = 0
                dq.append([nxt,cnt+1])
    
from collections import deque
import sys
input = sys.stdin.readline

visited = [1] * 100001

n , k = map(int, input().split())

bfs(n, 0)
