def bfs():
    global cnt
    dq = deque([n,cnt])
    while dq:
        num, cnt = dq.popleft()
        
        if n == m:
            break
        for nxt in (num+1, num-1, num*2, num-10):
            if not visited[nxt]:
                visited[nxt] = cnt + 1
                dq.append([nxt, cnt + 1])
    
from collections import deque

t = int(input())

for tc in range(1,t+1):
    n, m = map(int, input().split())
    
    visited = [0] * 10000001
    
    bfs()    
    
    cnt = 0
    
    print(f'#{tc} {cnt}')