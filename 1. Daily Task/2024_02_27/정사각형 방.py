# 모든 점에서 DFS
def dfs(i,j):
    di = [1,-1,0,0]
    dj = [0,0,1,-1]
    stack = [[i,j,1]]
    max_cnt = 1

    while stack:
        i,j,cnt = stack.pop()
        if cnt > max_cnt:
            max_cnt = cnt
        for k in range(4):
            if 0 <= i+di[k] < n and 0 <= j+dj[k] < n and arr[i][j] + 1 == arr[i+di[k]][j+dj[k]]:
                stack.append([i+di[k], j+dj[k], cnt+1])

    return cnt

t = int(input())

for tc in range(1,t+1):
    n = int(input())

    arr = [list(map(int,input().split())) for _ in range(n)]
    

    cnt_lst = []
    for i in range(n):
        for j in range(n):
            # 방번호 & 이동할 수 있는 방의 수
            cnt_lst.append([arr[i][j], dfs(i,j)])

    result = sorted(cnt_lst, key = lambda x : (-x[1],x[0]))
    print(f'#{tc} {result[0][0]} {result[0][1]}')