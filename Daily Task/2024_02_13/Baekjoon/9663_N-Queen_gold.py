def N_Queen(n, row_lst):
    # 기저 조건
    if n == N:
        global cnt
        cnt += 1
        return
    
    check_lst = [True]*N
    for i in range(N):
        if row_lst[i] != -1:
            dif = n - i # 해당 행과 현재 행의 차이

            # 왼쪽 아래 대각선 체크
            if row_lst[i]-dif >= 0:
                check_lst[row_lst[i]-dif] = False
                
            # 오른쪽 아래 대각선 체크
            if row_lst[i]+dif < N:
                check_lst[row_lst[i]+dif] = False
            
            # 열 체크 
            check_lst[row_lst[i]] = False

    for i in range(N):
        if check_lst[i]:
            row_lst[n] = i
            N_Queen(n+1, row_lst)
            row_lst[n] = -1
            # 복구
            


import sys
input = sys.stdin.readline

N = int(input())

row_lst = [-1]*N
cnt = 0
N_Queen(0, row_lst)
print(cnt)

# 현재의 깊이(행)를 인자로 넘겨주기
# 열은 열 리스트를 넘겨주기
# 대각선 판단 방법 -> 넘어온 열 리스트와 현재 행의 차이를 고려해서 체크