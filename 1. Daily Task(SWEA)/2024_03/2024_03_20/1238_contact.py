def bfs(start):
    order[start] = 1
    dq = deque()
    dq.append(start)
    
    while dq:
        now = dq.popleft()
        for next in edge[now]:
            if not order[next]:
                dq.append(next)
                order[next] = order[now] + 1
    

from collections import deque

t = 10

for tc in range(1,t+1):
    
    length, start = map(int, input().split())
    e = list(map(int, input().split()))
    
    edge = [[] for _ in range(101)] # 연락 인원은 최대 100명
    order = [0]*101 # visited 로도 사용할 것
    
    for i in range(length // 2):
        edge[e[2*i]].append(e[2*i + 1])
        
    bfs(start)
    
    last_order = 0
    for i in range(1,101):
        if order[i] >= last_order:
            last_order = order[i]
            last_contact = i
            
    print(f'#{tc} {last_contact}')