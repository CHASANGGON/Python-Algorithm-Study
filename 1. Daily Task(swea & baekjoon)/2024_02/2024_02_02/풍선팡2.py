T = int(input())

for test_case in range(1, 1 + T):
    n, m = map(int, input().split())
    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]

    balloon = [list(map(int, input().split())) for _ in range(n)]

    max_b = 0
    for i in range(n):
        for j in range(m):
            bs = balloon[i][j]
            for k in range(4):
                if 0 <= i + di[k] <= n-1 and 0 <= j + dj[k] <= m-1:
                    bs += balloon[i+di[k]][j+dj[k]]
            max_b = max(max_b,bs)
    
    print(f'#{test_case} {max_b}')