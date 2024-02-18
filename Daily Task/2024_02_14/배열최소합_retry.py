def func(i, k, s):
    if i == N:
        global min_s
        if min_s > s:
            min_s = s
    
    if s >= min_s: # 가지치기
        return
    
    for j in range(i,N):
        col_lst[j], col_lst[i] = col_lst[i], col_lst[j]
        func(i+1, k, s+arr[i][col_lst[i]])
        col_lst[j], col_lst[i] = col_lst[i], col_lst[j] # 복구

T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    
    min_s = 9999
    col_lst = list(range(N))
    func(0, N, 0)
    print(min_s)