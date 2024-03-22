def dfs(now, now_w):
    global min_w
    
    if now_w >= min_w:
        return
    
    if now == N: # 도착 노드에 도달했으면
        min_w = now_w
        
    for nxt, w in graph[now]:
        dfs(nxt, now_w + w)
        
    

t = int(input())

for tc in range(1, t + 1):

    N, E = map(int, input().split())
    
    graph = [[] for _ in range(N+1)]
    
    for _ in range(E):
        s, e, w = map(int,input().split())
        graph[s].append([e,w])

    min_w = 10000
    dfs(0, 0)

    print(f'#{tc} {min_w}')