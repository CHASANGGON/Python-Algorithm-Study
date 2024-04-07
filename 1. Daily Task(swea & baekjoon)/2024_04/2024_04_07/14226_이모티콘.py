def bfs():
    dq = deque()
    now = 1 # 시작 위치
    clip = 0 # 시작 클립보드
    time = 0 # 시작 시간
    
    dq.append([now, clip, time])
    
    while dq:
        now, clip, time = dq.popleft()
        
        if now == s: # 도달
            print(time)
            break
        
        for nxt, nxt_clip in (now, now), (now + clip, clip), (now - 1, clip):
            if 0 <= nxt <= 1000 and nxt_clip not in visited[nxt]:
                dq.append([nxt, nxt_clip, time + 1]) # 모든 연산은 1초 소요
                visited[nxt].append(nxt_clip)
        
        
from collections import deque

s = int(input())
visited = [[] for _ in range(1001)]
visited[1].append(0)
bfs()