# 선택 정렬
T = int(input())

for test_case in range(1,1+T):
    N = int(input())

    lst = list(map(int,input().split()))

    for i in range(N-1):
        m = i
        for j in range(i,N):
            if i % 2 == 0:
                if lst[j] > lst[m]:
                    m = j
            else:
                if lst[j] < lst[m]:
                    m = j
        
        lst[i], lst[m] = lst[m], lst[i]
    print(f'#{test_case} ',end='')
    for i in range(10):
        print(lst[i], end=' ')
    print()