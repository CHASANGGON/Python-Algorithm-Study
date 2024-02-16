T = int(input())
print('hi')
for test_case in range(1,T+1):
    n = int(input())
    
    maze = [list(input()) for _ in range(n)] # list로 만들어야 나중에 수정 가능
    
    # 출발 도착 위치 찾기
    start_end = []
    for i in range(n):
        for j in range(n):
            if maze[i][j] == '2':
                start_end.append([i,j])
                
    di = [1,-1,0,0]
    dj = [0,0,1,-1]
    result = 0
    stack = [start_end[0]] # 시작 좌표
    while stack:
        r,c = stack.pop()
        
        for k in range(4):    
            if 0 <= r+di[k] < n and 0 <= c+dj[k] < n: # index range 체크
                
                if maze[r+di[k]][c+dj[k]] == '0':
                    stack.append((r+di[k],c+dj[k]))
                    maze[r+di[k]][c+dj[k]] = '1' # visited
                
                elif maze[r+di[k]][c+dj[k]] == '3':
                    result = 1 # 도착했을 때의 출력
                    stack = [] # while문 탈출을 위해
                    break
    
    print(f'#{test_case} {result}')