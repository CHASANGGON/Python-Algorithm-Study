for test_case in range(1,11):
    input()
    ladder = [list(map(int,input().split())) for _ in range(100)]
    i = 99
    j = ladder[99].index(2)
 
    while i != 0:
        if 0 <= j-1 and ladder[i][j-1] == 1:
            while j-1 >= 0 and ladder[i][j-1] == 1:
                j -= 1
            i -= 1
        elif j+1 <= 99 and ladder[i][j+1] == 1:
            while j+1 <= 99 and ladder[i][j+1] == 1:
                j += 1
            i -= 1
        else:
            i -= 1
 
    print(f'#{test_case} {j}')