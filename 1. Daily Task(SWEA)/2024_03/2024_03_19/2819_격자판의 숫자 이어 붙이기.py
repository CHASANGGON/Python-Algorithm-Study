def dfs(i, j, depth, num):
    if depth == 7:
        result.append(num)
        return
    
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < 4 and 0 <= nj < 4:
            dfs(ni,nj,depth+1, num+arr[ni][nj])

t = int(input())

for tc in range(1,t+1):
    
    arr = [list(input().split()) for _ in range(4)]

    di = [1,-1,0,0]
    dj = [0,0,1,-1]

    result = []

    for i in range(4):
        for j in range(4):
            num = []
            dfs(i, j, 0, '')
    
    print(f'#{tc} {len(list(set(result)))}')