def dfs(i,j, s):
    global min_s

    if i == n-1 and j == n-1:
        if s < min_s:
            min_s = s
    
    # 가지치기
    if s > min_s:
        return
    else:
        for k in range(2):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < n:
                dfs(ni,nj,s+arr[ni][nj])


t = int(input())

for tc in range(1,t+1):

    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    

    di = [1,0]
    dj = [0,1]

    min_s = 9999
    dfs(0,0,arr[0][0])

    print(f'#{tc} {min_s}')