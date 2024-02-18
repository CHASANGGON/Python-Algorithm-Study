def f(i, k, s):
    # 기저 조건
    if i == k:
        global min_s
        if s < min_s:
            min_s = s
    
    # 가지치지(backtracking)
    elif s >= min_s:
        return

    # 재귀호출 : P의 인덱스를 조작(교환)하여 순열 생성 -> col 중복 없이 sum
    else:
        for j in range(i,k):
            P[i], P[j] = P[j], P[i] # 교환하여 순열 생성
            f(i+1, k, s+arr[i][P[i]]) # 현재까지 결정된 행(i)과 열(j)의 값을 누적
            P[i], P[j] = P[j], P[i] # 복구

T = int(input())

for test_case in range(1,T+1):
    N = int(input())    
    P = list(range(N))
    arr = [list(map(int,input().split())) for _ in range(N)]
    
    min_s = 9999
    f(0, N, 0) # i(시작), k(종료), sum
    print(f'#{test_case} {min_s}')