T = int(input())
for test_case in range(1,1+T):
    n, m = map(int,input().split())
    bugs = [list(map(int, input().split())) for _ in range(n)]
    max_kill_bugs = 0

    di, dj = [], []
    for i in range(m):
        for j in range(m):
            di.append(i)
            dj.append(j)

    for i in range(n-m+1):
        for j in range(n-m+1):
            kill_bugs = 0
            for k in range(m**2):
                kill_bugs += bugs[i+di[k]][j+dj[k]]
            max_kill_bugs = max(max_kill_bugs, kill_bugs)

    print(f'#{test_case} {max_kill_bugs}')
