def backtrack(i,j,cns): # 좌표, 소비량
    global ans
    if cns >= ans:
        return
    if i == N - 1 and j == N -1:
        ans = cns
    
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < N and 0 <= nj < N:
            backtrack(ni, nj, max(0, arr[ni][nj] - arr[i][j]))
                

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    
    arr = [list(map(int,input().split())) for _ in range(n)]
    
    di = [1,-1,0,0]
    dj = [0,0,1,-1]
    
    ans = 9999
    backtrack(0,0,0) # 좌표, 소비량
    
    print(f'#{tc} {ans}')