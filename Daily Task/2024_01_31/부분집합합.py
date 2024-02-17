T = int(input())

for test_case in range(1,T+1):
    N, K = map(int,input().split())
    lst = [i for i in range(1,13)]
    subset_lst = []
    

    for i in range(1<<12):
        temp_lst = []
        for j in range(12):
            if i & (1<<j):
                temp_lst += [lst[j]]
        subset_lst.append(temp_lst)
    
    count = 0
    for subset in subset_lst:
        if len(subset) == N and sum(subset) == K:
            count += 1
    print(f'#{test_case} {count}')