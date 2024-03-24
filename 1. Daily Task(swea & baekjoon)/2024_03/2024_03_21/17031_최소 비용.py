def bfs(i, j):
    di = [1,-1,0,0] # 델타
    dj = [0,0,1,-1]
    
    dq = deque() # 큐 생성
    dq.append([i,j])
    dp[0][0] = 0 # 초기 비용 초기화
    
    while dq:
        i, j = dq.popleft() # BFS를 위해 popleft
        for k in range(4): # 델타 탐색
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < n: # 인덱스 검사
                new_cost = max(arr[ni][nj] - arr[i][j] + 1, 1) # 새로운 비용 = 높이차 + 기본 이동 비용(1)
                
                # 이동하려는 곳의 기존 최소 비용 > 현재까지의 최소 비용 + 새로운 비용 
                if dp[ni][nj] > dp[i][j] + new_cost:
                    dp[ni][nj] = dp[i][j] + new_cost # 갱신
                    dq.append([ni,nj]) # 최소 비용을 가진 유망한 노드라서 탐색 후보에 추가
                    
# 최소 비용을 구해야 하기 때문에 bfs
from collections import deque

t = int(input())
INF = 10**9 # 최댓값 초기화

for tc in range(1, t+1):
    
    n = int(input())
    
    arr = [list(map(int, input().split())) for _ in range(n)] # 입력
    dp = [[INF] * n for _ in range(n)] # visited & dp
    
    bfs(0,0) # 시작점에서 출발
    
    print(f'#{tc} {dp[n-1][n-1]}')