def f(i, k):
    if i == k:
        global min_s
        s = 0
        for j in range(N):
            s += arr[j][P[j]]
        if s < min_s:
            min_s = s
    else:
        for j in range(i, k):
            P[i], P[j] = P[j], P[i] # P[i] <-> P[j]
            f(i+1,k)
            P[i], P[j] = P[j], P[i] # 복구

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    P = list(range(N)) # 각 행(index)에서 참조할 열
    min_s = 9999
    f(0, N)
    print(f'#{test_case} {min_s}')