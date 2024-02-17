for test_case in range(1,11):
    input()
    lst = [list(map(int,input().split())) for _ in range(100)]
    
    sum = [0]*202
    for i in range(100): 
        sum[200] += lst[i][i]       # 대각선1
        sum[201] += lst[i][99-i]    # 대각선2
        for j in range(100):
            sum[i] += lst[i][j]     # 가로
            sum[i+100] += lst[j][i] # 세로

    print(f'#{test_case} {max(sum)}')