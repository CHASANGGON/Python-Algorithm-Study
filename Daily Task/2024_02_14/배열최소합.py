def f(i, k, s):
    global cnt 
    global min_v
    cnt += 1

    if i == k:
        # print(*P)
        if min_v > s:
            min_v = s
    elif s >= min_v:
        return
    else:
        for j in range(i, k):   # P[i]자리에 올 원소 P[j]
            P[i], P[j] = P[j], P[i] # p[i]<->P[j]
            f(i+1, k, s+arr[i][P[i]])
            P[i], P[j] = P[j], P[i] # 교환전으로 복구

T = int(input())    

for test_case in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    P = [i for i in range(N)]
    min_v = 9999
    cnt = 0
    f(0, N, 0)
    print(f'#{test_case} {min_v}')