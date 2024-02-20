def dfs(i, start):
    if i == M:
        print(*lst)
    else:
        for j in range(start,N+1):
            if j not in lst:
                lst.append(j)
                dfs(i+1,j)
                lst.pop()
        

N, M = map(int,input().split())
lst = []
dfs(0, 1)