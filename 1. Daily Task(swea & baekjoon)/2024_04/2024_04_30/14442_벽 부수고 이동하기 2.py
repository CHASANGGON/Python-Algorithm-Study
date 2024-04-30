from collections import deque
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

arr = [list(input()) for _ in range(n)]

visited = [[[0]*m for _ in range(n)] for _ in range(k+1)] # k차원 생성

dq = deque()
dq.append((0,0,0)) # 출발점 push
visited[0][0][0] = 1 # 방문 처리
ans = -1 # 답 초기화

while dq:
    now_k,i,j, = dq.popleft()
    if i == n-1 and j == m-1:
        ans = visited[now_k][i][j]
        break
    
    for ni,nj in (i+1,j), (i,j+1), (i-1,j), (i,j-1):
        # 아직 방문하지 않았고, 벽이 아니라면
        if 0 <= ni < n and 0 <= nj < m:
            
            # 벽을 부수지 않고 이동
            if arr[ni][nj] == '0' and visited[now_k][ni][nj] == 0: # 길이고, 방문한 적 없다면
                visited[now_k][ni][nj] = visited[now_k][i][j] + 1 # 거리 기록
                dq.append((now_k,ni,nj))
            
            
            elif arr[ni][nj] == '1' and now_k < k and visited[now_k+1][ni][nj] == 0: # 벽을 부수고 이동할 수 있으면
                visited[now_k+1][ni][nj] = visited[now_k][i][j] + 1
                dq.append((now_k+1,ni,nj))

print(ans)