def bfs():
    global cnt
    dq = deque()
    dq.append([n,cnt])
    while dq:
        num, cnt = dq.popleft()
        
        if num == m:
            break
        for nxt in (num+1, num-1, num*2, num-10):
            # 중복 검사 방지 및 인덱스 에러 방지
            if not visited[nxt] and 1 <= nxt <= 1000000:
                visited[nxt] = cnt + 1
                dq.append([nxt, cnt + 1])
    
from collections import deque

t = int(input())

for tc in range(1,t+1):
    n, m = map(int, input().split())
    
    visited = [0] * 10000001
    cnt = 0
    bfs()    
    
    print(f'#{tc} {cnt}')