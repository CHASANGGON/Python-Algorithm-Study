T = int(input())

for test_case in range(1,1+T):
    N,M = map(int,input().split())
    lst =  [list(map(int,input().split())) for _ in range(N)]
    max_total = 0

    for i in range(N):
        for j in range(M): 
            flower = total = lst[i][j]         # 본인 값
            for k in range(1,flower+1):
                if i - k >= 0:                # 왼쪽 값
                    total += lst[i-k][j]
                if i + k <= N-1:              # 오른쪽 값
                    total += lst[i+k][j]
                if j - k >= 0:                # 위 값
                    total += lst[i][j-k]
                if j + k <= M-1:              # 아래 값
                    total += lst[i][j+k]

            max_total = max(max_total, total)

    print(f'#{test_case} {max_total}')