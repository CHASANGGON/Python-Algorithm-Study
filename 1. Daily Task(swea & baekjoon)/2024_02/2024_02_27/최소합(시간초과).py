from collections import deque

def bfs(q):
    di = [1,0]
    dj = [0,1]

    while q:
        n_q = deque()

        while q:
            i, j = q.popleft()
            
            # 방향 전환
            for k in range(2):
                
                # 인덱스 체크
                if 0 <= i + di[k] < n and 0 <= j + dj[k] < n:
                
                    # 방문한 적 없다면 대입
                    if visited[i+di[k]][j+dj[k]] == False:
                        sum_arr[i+di[k]][j+dj[k]] = sum_arr[i][j] + arr[i+di[k]][j+dj[k]]
                        visited[i+di[k]][j+dj[k]] = True

                    # 방문한 적 있으면
                    else:
                
                        # 현재 값이 더 작으면 대입
                        if sum_arr[i+di[k]][j+dj[k]] > sum_arr[i][j] + arr[i+di[k]][j+dj[k]]:
                            sum_arr[i+di[k]][j+dj[k]] = sum_arr[i][j] + arr[i+di[k]][j+dj[k]]
                    n_q.append([i+di[k],j+dj[k]])
        q = n_q


t = int(input())

for tc in range(1,t+1):
    n = int(input())


    arr = [list(map(int,input().split())) for _ in range(n)]
    visited = [[False]*n for _ in range(n)]
    sum_arr = [[0]*n for _ in range(n)]
    sum_arr[0][0] = arr[0][0]
    
    
    q = deque()
    q.append([0,0])
    bfs(q)

    print(f'#{tc} {sum_arr[n-1][n-1]}')