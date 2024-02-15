T = int(input())

for test_case in range(1,T+1):
    n = int(input())
    
    maze = [list(input()) for _ in range(n)] # list로 만들어야 나중에 수정 가능
    
    # 출발 도착 위치 찾기
    for i in range(n):
        for j in range(n):
            if maze[i][j] == '2':
                queue = [[i,j,0]] # 매번 count를 하면 거리가 누적돼서 안 됨
                                  # 그래서 queue에 enqueue(push)할 때, 현재까지 온 거리도 같이 추가
                
    di = [0,0,1,-1]
    dj = [1,-1,0,0]
    cnt = 0
    escape = False
    while queue:
        back = True
        r,c,cnt = queue.pop(0) # 큐를 사용해야함 -> DFS를 위해서
							   # 스택을 사용하면 -> BFS가 됨 -> visited의 의미로 maze에 1을 넣어서 길을 지워버림
                               # 그 결과 정상적인 길도 지워질 가능성이 존재하기에, 최단거리를 보장할 수 없음

                               # 만약 BFS를 하면서 가능한 모든 경우의 수를 고려한 다음 최단 거리를 찾으려고 할 수도 있지만
                               # 대부분의 사람들이 visited의 의미로 1을 체크하면서 왔던 길을 지웠고, 그렇게 해야만 뒤로 가지 않고 앞으로 진행 가능
                               # 그렇기에 visited를 사용하면서 BFS로 최단 거리를 찾는 경우는 불가능
        for k in range(4):
            if 0 <= r+di[k] < n and 0 <= c+dj[k] < n:
                if maze[r+di[k]][c+dj[k]] == '0':
                    queue.append((r+di[k],c+dj[k],cnt+1)) # 해당 위치에서의 거리 추가
                                                          # 그러나 count 변수를 직접 증가시키면 안됨
                    maze[r+di[k]][c+dj[k]] = '1'
                    back = False
                elif maze[r+di[k]][c+dj[k]] == '3':
                    escape = True
                    queue = [] # while문 탈출
                    break # for문 탈출
    
    if not escape: # 도착할 수 없다면 cnt = 0
        cnt = 0
        
    print(f'#{test_case} {cnt}')