for test_case in range(1,11):
    input()
    lst = [list(map(int,input().split())) for _ in range(100)]
    
    sum = [0]*202
    for i in range(100):
        for j in range(100):
            sum[i] += lst[i][j]
    
    for j in range(100):
        for i in range(100):
            sum[j+100] += lst[i][j]

    for i in range(100):
        sum[200] += lst[i][i]
        sum[201] += lst[i][99-i]

    print(f'#{test_case} {max(sum)}')