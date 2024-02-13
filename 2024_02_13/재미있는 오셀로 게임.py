T = int(input())
# 오셀로 겜이 뭔지 몰랐기도 한데, 문제 잘못 읽어서 3시간 가까이 뻘짓했네요,,,
# 처음에 돌 네 개 놓고 시작하는 거였네요..ㅠㅠㅠㅠ
for test_case in range(1,T+1):
    N, M = map(int,input().split())
    board = [[0]*N for _ in range(N)]
    board[N//2 -1][N//2 -1] = board[N//2][N//2] = 2
    board[N//2][N//2 -1] = board[N//2 -1][N//2] = 1
    di = [-1,-1,-1, 0, 0, 1, 1, 1]
    dj = [-1, 0, 1,-1, 1,-1, 0, 1]

    for _ in range(M):
        i, j, stone = map(int,input().split())
        # 좌표 보정
        i -= 1 
        j -= 1
        board[i][j] = stone
            
        for k in range(8): 
            stack = []
            m = 1
            while 0 <= i + m*di[k] < N and 0 <= j + m*dj[k] < N:
                stack.append((i+m*di[k],j+m*dj[k]))
                if board[i+m*di[k]][j+m*dj[k]] == stone:
                    for y, x in stack:
                        board[y][x] = stone
                    break
                elif board[i+m*di[k]][j+m*dj[k]] == 0:
                    break
                m += 1
    black, white = 0, 0  
    for b in board:
        black += b.count(1)
        white += b.count(2)
    print(f'#{test_case} {black} {white}')