# 갈 수 있는지 없는지만 판단 -> dfs, bfs 뭘로하든 ㄱㅊ
# 일단, 어디 갈 수 있으면 끝까지 가봐 -> dfs로 할 예정
def dfs():
    while stack:
        i, j = stack.pop()
        
        # 네 방향에 대해서 탐색
        for k in range(4):
            if 0 <= i + di[k] < N and 0 <= j + dj[k] < N and maze[i + di[k]][j + dj[k]] == '0':
                stack.append([i + di[k],j + dj[k]])
                maze[i + di[k]][j + dj[k]] = '1' # 방문 표시로 길 지워버리기 -> 되돌아가는 것도 차단
                
            elif 0 <= i + di[k] < N and 0 <= j + dj[k] < N and maze[i + di[k]][j + dj[k]] == '3':
                print(f'#{test_case} {1}')
                return
    print(f'#{test_case} {0}')



T = 10
for test_case in range(1,T+1):
    int(input())
    N = 16
    maze = [list(input()) for _ in range(N)]
    di = [1,-1,0,0]
    dj = [0,0,1,-1]
    
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                stack = [[i,j]]
                break # 메모리 절약
            
    dfs()