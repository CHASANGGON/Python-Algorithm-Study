

from collections import deque

T = int(input())

for tc in range(1,T+1):
    n = int(input())
    
    # 배열의 값을 해당 좌표까지의 최소 비용이라고 생각
    cost = [list(map(int,input().split())) for _ in range(n)]
    
    
    di = [1,-1,0,0]
    dj = [0,0,1,-1]
    
    
    dq = deque()
    dq.append([0,0])
    
    while dq:
        i, j = dq.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < n:
                new_cost = max(1, cost[ni][nj] - cost[i][j] + 1)
                if cost[i][j] + new_cost < cost[ni][nj]: # 현재 진행 경로가 더 최소 비용이라면
                    cost[ni][nj] = cost[i][j] + new_cost # 값을 갱신해주고
                    dq.append([ni,nj]) # 추가 탐색을 위해 append
                
        
    print(f'#{tc} {cost[n-1][n-1]}') # 도착지까지의 최소 비용을 출력