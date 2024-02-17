for test_case in range(1,11):
    N = int(input())
    height_lst = list(map(int,input().split()))
    counting_lst = [0]*101 # 높이 1 ~ 100
    for height in height_lst:
        counting_lst[height] += 1
    i = 1
    j = 100
    while N > 0:
        while counting_lst[i] == 0:
            i += 1
        while counting_lst[j] == 0:
            j -= 1
        dump = min(counting_lst[i], counting_lst[j], N)
        counting_lst[i] -= dump
        counting_lst[i+1] += dump
        counting_lst[j] -= dump
        counting_lst[j-1] += dump
        N -= dump
    if counting_lst[i] == 0:
        i += 1
    if counting_lst[j] == 0:
        j -= 1
    print(f'#{test_case} {j-i}')