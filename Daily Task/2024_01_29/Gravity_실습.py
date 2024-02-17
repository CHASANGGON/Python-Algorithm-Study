t = int(input())

for test_case in range(1,t+1):
    n = int(input())
    lst = list(map(int,input().split()))

    max_cnt = 0
    for i in range(n-1):
        now_cnt = 0
        for j in range(i+1,n):
            if lst[i] > lst[j]:
                now_cnt += 1
        max_cnt = max(max_cnt, now_cnt)
    print(f'#{test_case} {max_cnt}')