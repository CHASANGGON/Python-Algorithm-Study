T = int(input())

for test_case in range(1,1+T):
    N,M = map(int,input().split())
    lst =  [list(map(int,input().split())) for _ in range(N)]
    max_total = 0

    for i in range(N):
        for j in range(M): 
            total = lst[i][j]
            if i != 0:
                total += lst[i-1][j]
            if i != N-1:
                total += lst[i+1][j]
            if j != 0:
                total += lst[i][j-1]
            if j != M-1:
                total += lst[i][j+1]
            # print(i,j,total)
            max_total = max(max_total, total)

    print(f'#{test_case} {max_total}')