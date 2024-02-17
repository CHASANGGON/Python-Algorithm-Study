def new_func():
    for i in range(N):
        for j in range(N):
            if board[i][j] == 'o':
                for k in range(4):
                    cnt = 1
                    l = 1
                    while 0 <= i+di[k]*l < N and 0 <= j+dj[k]*l < N:
                        if board[i+di[k]*l][j+dj[k]*l] == 'o':
                            cnt += 1
                            l += 1
                            if cnt == 5:
                                return True
                        else:
                            break
    return False


T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    board = [input() for _ in range(N)]
    
    di = [1,0,1,1] #상하좌우대각선
    dj = [0,1,1,-1]
    
    if new_func():
        result = 'YES'
    else:
        result = 'NO' 
    
    print(f'#{test_case} {result}')