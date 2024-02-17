T = int(input())

for test_case in range(1,T+1):
    N, M = map(int,input().split())
    
    words = [input() for _ in range(N)]

    print(f'#{test_case} ',end='')


    # 가로 검증    
    for i in range(N): # N = 13 -> range(13) : 0~12
        for k in range(N-M+1): # range(4) : 0~3
            horizontal =''
            for j in range(M):
                horizontal += words[i][k+M-1-j]
            if horizontal == words[i][k:k+M]:
                print(horizontal)


    # 세로 검증
    for i in range(N):
        for k in range(N-M+1): # N = 13, M = 10 -> range(4) : 0~3
            vertical_1 = ''
            vertical_2 = ''
            for j in range(M): # range(10) : 0~9 -> 0 ~ 12 = k+j
                vertical_1 += words[k+j][i]      # 0~3 + 0~9 
                vertical_2 += words[k+M-1-j][i]  # 0~3 + 9 - 0~9
            if vertical_1 == vertical_2:
                print(vertical_1)