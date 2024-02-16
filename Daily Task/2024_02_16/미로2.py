T = 10
for test_case in range(1,T+1):
    input()

    # 방문 체크를 위한 수정이 가능해야 하므로 각 행입력을 list로 만들기
    maze = [list(input()) for _ in range(100)]

    # 시작 위치 잡기
    for i in range(100):
        for j in range(100):
            if maze[i][j] == '2':
                stack = [[i,j]] # 스택 생성 및 출발 위치 저장
                break

    arrival = 0 # 도달 가능 여부 - default 값은 0
    di = [1,-1,0,0]
    dj = [0,0,1,-1]
    # 방문 가능 여부만 따지기 때문에 stack이든 queue든 상관 없음
    while stack: # stack이 비워질 때까지 실행 = 방문 가능한 위치가 존재할 때 까지
        i, j = stack.pop()
    
        for k in range(4):
            if 0<=i+di[k]<100 and 0<=j+dj[k]<100: # 인덱스를 초과하지 않는 다면 조사
                if maze[i+di[k]][j+dj[k]] == '0': # 길이라면
                    stack.append([i+di[k],j+dj[k]]) # stack에 추가
                    maze[i+di[k]][j+dj[k]] = '1' # 방문 표시로 1
                
                elif maze[i+di[k]][j+dj[k]] == '3': # 도착
                    arrival = 1
                    stack = [] # while문 종료를 위해
                    break # for 문 종료

    print(f'#{test_case} {arrival}')