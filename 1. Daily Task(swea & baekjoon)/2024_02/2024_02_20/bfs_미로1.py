def bfs():
    while q:
        i, j = q.pop(0)
        
        for k in range(4):
            if 0 <= i + di[k] < N and 0 <= i + di[k] < N and maze[i+di[k]][j+dj[k]] == '0':
                q.append([i+di[k],j+dj[k]])
                maze[i+di[k]][j+dj[k]] = '1'
            
            elif 0 <= i+di[k] < N and 0 <= i+di[k] < N and maze[i+di[k]][j+dj[k]] == '3':
                print(f'#{test_case} {1}')
                return
    
    print(f'#{test_case} {0}')


T = 10
for test_case in range(1,1+T):
    int(input())
    N = 16
    maze = [list(input()) for _ in range(N)]
    di = [1,-1,0,0]
    dj = [0,0,1,-1]
    
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                q = [[i,j]]       
                break
            
    bfs()