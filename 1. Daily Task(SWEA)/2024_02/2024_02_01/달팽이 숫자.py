# 달팽이
T = int(input())
for test_case in range(1,T+1):

    N = int(input())
    
    arr = [[0]*N for _ in range(N)]
    cnt = 1
    dr = i = j = 0
    arr[i][j] = cnt
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    
    while cnt < N**2:
        if 0 <= i+di[dr] <= N - 1 and 0 <= j+dj[dr] <= N - 1 and arr[i+di[dr]][j+dj[dr]] == 0: # 해당 방향 진행 불가
            cnt += 1
            i += di[dr]
            j += dj[dr]
            arr[i][j] = cnt
        else:
            dr += 1 
            dr %= 4
    print(f'#{test_case}')
    for a in arr:
        print(*a)